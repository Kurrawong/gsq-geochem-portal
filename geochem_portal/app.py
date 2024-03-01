from textwrap import dedent

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from geochem_portal import router


def register_routers(app: FastAPI) -> None:
    app.include_router(router.system.router, prefix="/api/v1/system", tags=["System"])
    app.include_router(router.validate.router, prefix="/api/v1", tags=["Validation"])
    app.include_router(router.convert.router, prefix="/api/v1", tags=["Conversion"])
    app.include_router(router.ui.router)


def register_middlewares(app: FastAPI) -> None:
    app.add_middleware(
        CORSMiddleware,
        allow_origins=["*"],
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )


def create_app() -> FastAPI:
    app = FastAPI(
        title="Geochemistry Portal API",
        description=dedent(
            """
            GSQ Geochemistry Data Portal API provides functions to validate and submit geochemistry data.
        """
        ),
    )

    register_routers(app)
    register_middlewares(app)

    return app
