from geochemxl.converter import convert as xl_convert
from rdflib import Graph, URIRef

from geochem_portal.validate import to_validation_report


def convert(file):
    conforms, results_graph, results_text = xl_convert(file)
    result_type = URIRef("https://linked.data.gov.au/def/geochem/ConversionResult")
    if conforms:
        return to_validation_report(
            conforms, Graph(), results_graph.serialize(), result_type
        )

    return to_validation_report(conforms, results_graph, results_text, result_type)
