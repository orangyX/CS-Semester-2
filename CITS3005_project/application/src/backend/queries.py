
"""
Alot of these queries have been imported over from homework 2 and just intergrated to fit the system
With a few additions project requirements.

"""

import rdflib

from utility import config
from utility.datasets import Dataset

SCHEMA_NAME = "base"
RULES_NAME = "rules"
DATASET_NAME = "raw"

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
    Run a query over the graph; 
    keyword arguments fill the ?selected... variables.
    
    Missing OPTIONAL values come back as "".
    """
    rows = graph.query(prefixes(dataset) + sparql, initBindings=bindings)
    results = []
    for row in rows:                        
        cells = []
        for value in row:                       
            if value is None:                   
                cells.append("")
            else:
                cells.append(short(value))     
        results.append(tuple(cells))
    return results

# ===============================
# SPARQL Query Functions
# ===============================
class MakeQueries:

    # ===============================
    # FILTER Query Functions
    # ===============================
    @staticmethod
    def search_all():
        """
        bind: searchTerm 
        Should be a literal string. 
        
        Will search for ANYTHING that contains that term.
        
        Filtering can be applied seperately. 
        """
        
        query = """
        SELECT DISTINCT ?entity ?title ?property ?value
        WHERE {
            ?entity ?property ?value .
            BIND(IF(isIRI(?value), REPLACE(STR(?value), "^.*#", ""), STR(?value)) AS ?text)
            FILTER(CONTAINS(LCASE(?text), LCASE(?searchTerm)))
            OPTIONAL { ?entity uni:hasTitle ?title }
        }
        ORDER BY ?entity ?property
        """
        return query
        
    @staticmethod
    def get_incoming():
        """
        bind: selectedEntity (URIRef) - 
        Find facts pointing to that entity.
        """
        query = """
        SELECT ?subject ?property
        WHERE {
            ?subject ?property ?selectedEntity .
        }
        ORDER BY ?property ?subject
        """
        return query
    
    # ===============================
    # Aggregation Query Functions
    # ===============================
    @staticmethod
    def count_all_entities():
        """
        Looks at entites as an rdf type for all rdf types
        return the type and the count of it
        """
        query = """
        SELECT ?type (COUNT(*) AS ?count)
        WHERE {
            ?entity rdf:type ?type .
        }
        GROUP BY ?type
        ORDER BY DESC(?count)
        """
        return query
    
    @staticmethod
    def count_all_relations():
        """
        before it would return embedded graph relations
        so we can filter out relations that are from owl.
        """
        query = """
        SELECT ?relation (COUNT(*) AS ?count)
        WHERE {
            ?subject ?relation ?object .
            FILTER(STRSTARTS(STR(?relation), STR(uni:)))
        }
        GROUP BY ?relation
        ORDER BY DESC(?count)
        """
        return query

    @staticmethod
    def count_property_values():
        """
        Get a propertty value and return 
        count of property.
        """
        query = """
        SELECT DISTINCT ?value (COUNT(*) as ?count)
        WHERE {
            ?entity ?selectedPredicate ?value .
        }
        GROUP BY ?value
        ORDER BY DESC(?count)
        """
        return query

    @staticmethod
    def get_properties():
        """
        bind: selectedEntity 
        return a property value pair 
        """
        query = """
        SELECT ?property ?value
        WHERE {
            ?selectedEntity ?property ?value .
        }
        ORDER BY ?property
        """
        return query
    
    @staticmethod
    def query_by_relation():
        """bind: selectedRelation (URIRef)"""
        query = """
        SELECT ?subject ?object
        WHERE {
            ?subject ?selectedRelation ?object .
        }
        ORDER BY ?subject ?object
        """
        return query


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

