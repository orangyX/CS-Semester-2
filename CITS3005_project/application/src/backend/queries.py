


import rdflib

from utility import config
from utility.datasets import Dataset

SCHEMA_NAME = "base"
RULES_NAME = "rules"
DATASET_NAME = "raw"

from rdflib.plugins.sparql import prepareQuery

def headers(dataset, sparql: str) -> list[str]:
    """Column names from the query's SELECT, e.g. ["entity", "title"]"""
    return [str(v) for v in prepareQuery(prefixes(dataset) + sparql).algebra["PV"]]

# =========================
# HELPERS
# =========================
def prefixes(dataset: Dataset) -> str:
    return (
        "PREFIX rdf:   <http://www.w3.org/1999/02/22-rdf-syntax-ns#>\n"
        "PREFIX rdfs:  <http://www.w3.org/2000/01/rdf-schema#>\n"
        f"PREFIX uni:   <{config.SCHEMA_IRI}>\n"
        f"PREFIX rules: <{config.RULES_IRI}>\n"
        f"PREFIX data:  <{dataset.iri}>\n"
    )

def to_graph(world) -> rdflib.Graph:
    """
    Copy owl ready world into an RDF graph
    """
    graph = rdflib.Graph()
    for triple in world.as_rdflib_graph():
        graph.add(triple)
    return graph


def short(term) -> str:
    """
    Split IRI for end result
    """
    text = str(term)
    return text.split("#")[-1] if isinstance(term, rdflib.URIRef) else text


def run(graph, dataset, sparql: str, **bindings) -> list[tuple]:
    """
    Run a query over the graph; keyword arguments fill the ?selected... variables.
    Missing OPTIONAL values come back as "".
    """
    rows = graph.query(prefixes(dataset) + sparql, initBindings=bindings)
    return [tuple("" if v is None else short(v) for v in row) for row in rows]


# ===============================
# SPARQL Query Functions
# ===============================
class MakeQueries:

    # ===============================
    # FILTER Query Functions
    # ===============================
    @staticmethod
    def filter_by_name():
        """bind: searchTerm (Literal)"""
        return """
        SELECT ?entity ?title
        WHERE {
            ?entity uni:hasTitle ?title .
            FILTER(CONTAINS(LCASE(STR(?title)), LCASE(?searchTerm)))
        }
        ORDER BY ?title
        """

    @staticmethod
    def filter_by_property_value():
        """bind: selectedPredicate (URIRef), selectedValue (URIRef or Literal)"""
        return """
        SELECT DISTINCT ?entity
        WHERE {
            ?entity ?selectedPredicate ?selectedValue .
        }
        ORDER BY ?entity
        """

    # ===============================
    # Aggregation Query Functions
    # ===============================
    @staticmethod
    def count_all_entities():
        return """
        SELECT ?type (COUNT(*) AS ?count)
        WHERE {
            ?entity rdf:type ?type .
        }
        GROUP BY ?type
        ORDER BY DESC(?count)
        """

    @staticmethod
    def count_all_properties():
        return """
        SELECT ?property (COUNT(*) AS ?count)
        WHERE {
            ?subject ?property ?object .
            FILTER(?property != rdf:type)
        }
        GROUP BY ?property
        ORDER BY DESC(?count)
        """

    # ===============================
    # UTILITY Query Functions
    # ===============================
    @staticmethod
    def list_property_values():
        """bind: selectedPredicate (URIRef)"""
        return """
        SELECT DISTINCT ?value
        WHERE {
            ?entity ?selectedPredicate ?value .
        }
        ORDER BY ?value
        """

    @staticmethod
    def get_label():
        """bind: selectedObject (URIRef)"""
        return """
        SELECT ?label
        WHERE {
            ?selectedObject uni:hasTitle ?label .
        }
        """

    @staticmethod
    def get_parents():
        """bind: selectedEntity (URIRef)"""
        return """
        SELECT DISTINCT ?type
        WHERE {
            ?selectedEntity rdf:type ?directType .
            ?directType rdfs:subClassOf* ?type .
        }
        """

    @staticmethod
    def get_properties():
        """bind: selectedEntity (URIRef) - every fact about one entity (detail pages)"""
        return """
        SELECT ?property ?value
        WHERE {
            ?selectedEntity ?property ?value .
        }
        ORDER BY ?property
        """

    # ===============================
    # List Query Functions
    # ===============================
    @staticmethod
    def list_entities():
        return """
        SELECT DISTINCT ?entity ?label
        WHERE {
            { ?entity ?predicate ?object . }
            UNION { ?subject ?predicate ?entity . }
            FILTER(isIRI(?entity))
            OPTIONAL { ?entity uni:hasTitle ?label . }
        }
        ORDER BY ?entity
        """

    @staticmethod
    def list_entity_types():
        return """
        SELECT DISTINCT ?type
        WHERE {
            ?entity rdf:type ?type .
        }
        ORDER BY ?type
        """

    @staticmethod
    def list_by_entity_type():
        """bind: selectedType (URIRef) e.g. uni:Unit"""
        return """
        SELECT ?entity ?code ?title
        WHERE {
            ?entity rdf:type/rdfs:subClassOf* ?selectedType ;
                    uni:hasCode ?code .
            OPTIONAL { ?entity uni:hasTitle ?title . }
        }
        ORDER BY ?code
        """

    @staticmethod
    def list_relations():
        return """
        SELECT DISTINCT ?relation
        WHERE {
            ?subject ?relation ?object .
            FILTER(?relation != rdf:type)
        }
        ORDER BY ?relation
        """

    @staticmethod
    def query_by_relation():
        """bind: selectedRelation (URIRef)"""
        return """
        SELECT ?subject ?object
        WHERE {
            ?subject ?selectedRelation ?object .
        }
        ORDER BY ?subject ?object
        """

    # ===============================
    # Spec Query Functions
    # ===============================
    @staticmethod
    def foundational_units():
        """optional bind: selectedDegree (URIRef). Unit in every major of the degree."""
        return """
        SELECT DISTINCT ?selectedDegree ?unit
        WHERE {
            ?selectedDegree uni:hasMajor ?anyMajor .
            ?anyMajor uni:hasUnit ?unit .
            FILTER NOT EXISTS {
                ?selectedDegree uni:hasMajor ?major .
                FILTER NOT EXISTS { ?major uni:hasUnit ?unit }
            }
        }
        ORDER BY ?selectedDegree ?unit
        """

    @staticmethod
    def average_majors():
        """Average majors per study type, BPhil excluded."""
        return """
        SELECT ?type (AVG(?count) AS ?average)
        WHERE {
            {
                SELECT ?degree ?type (COUNT(DISTINCT ?major) AS ?count)
                WHERE {
                    ?degree uni:hasStudyType ?type .
                    OPTIONAL { ?degree uni:hasMajor ?major }
                    FILTER NOT EXISTS { ?degree a rules:BachelorOfPhilosophy }
                }
                GROUP BY ?degree ?type
            }
        }
        GROUP BY ?type
        """

    @staticmethod
    def majors_in_location():
        """bind: selectedLocation (URIRef). Every unit of the major is at that location."""
        return """
        SELECT DISTINCT ?major ?title
        WHERE {
            ?major a uni:Major ;
                   uni:hasTitle ?title ;
                   uni:hasUnit ?any .
            FILTER NOT EXISTS {
                ?major uni:hasUnit ?unit .
                FILTER NOT EXISTS { ?unit uni:locatedIn ?selectedLocation }
            }
        }
        ORDER BY ?title
        """

    @staticmethod
    def outcome_search():
        """bind: searchTerm (Literal). Major outcomes plus its units' outcomes."""
        return """
        SELECT DISTINCT ?major ?title ?outcome
        WHERE {
            ?major a uni:Major ;
                   uni:hasTitle ?title .
            { ?major uni:hasOutcome ?outcome }
            UNION
            { ?major uni:hasUnit ?unit . ?unit uni:hasOutcome ?outcome }
            FILTER(CONTAINS(LCASE(STR(?outcome)), LCASE(?searchTerm)))
        }
        ORDER BY ?title
        """
