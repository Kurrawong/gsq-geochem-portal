import traceback
from io import BytesIO

from fastapi import APIRouter, HTTPException, UploadFile, status
from pydantic import BaseModel

from geochem_portal.convert import convert

router = APIRouter()


class DataIn(BaseModel):
    data: str


@router.post("/convert")
async def convert_route(file: UploadFile):
    try:
        # Using BytesIO object here since the spooled file provided by Starlette does not play well with
        # openpyxl's usage of zipfile.
        # TODO: fixme - the current processing will read all file contents into memory.
        with BytesIO(await file.read()) as buffer:
            buffer.name = file.filename
            buffer.suffix = "xlsx"
            report = convert(buffer)
            return report
    except Exception as err:
        traceback.print_exc()
        raise HTTPException(
            status.HTTP_400_BAD_REQUEST, f"Conversion failed: {err}"
        ) from err
