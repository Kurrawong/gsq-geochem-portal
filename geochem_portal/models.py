from pydantic import BaseModel, constr
from rdflib import SH


class ValidationResult(BaseModel):
    severity: constr(pattern="^(info|warning|violation)$") | None
    focus_node: str | None
    result_path: str | None
    message: str

    def __eq__(self, __value: object) -> bool:
        if (
            type(__value) == type(self)
            and __value.severity == self.severity
            and __value.message == self.message
        ):
            return True
        return False


class ValidationReport(BaseModel):
    conforms: bool
    results: list[ValidationResult]
    results_text: str
    violation_count: int
    warning_count: int
    info_count: int


severity_to_str = {
    SH.Violation: "violation",
    SH.Warning: "warning",
    SH.Info: "info",
}
