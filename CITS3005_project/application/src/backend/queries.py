
"""
Alot of these queries have been imported over from homework 2 and just intergrated to fit the system
With a few additions project requirements.

"""

import rdflib

from utility import config
from utility.datasets import Dataset
from rdflib.plugins.sparql import prepareQuery   

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


def headers(dataset, sparql: str) -> list[str]:
    """
    Now this is neat. 
    Because we allow dynamic querying, the outcome doent know
    what the headers of each column will be in advance. 
    
    This plug in just allows us to pull the selected objects
    and return the names to be used as queries.
    """
    parsed = prepareQuery(prefixes(dataset) + sparql)
    names = []
    for variable in parsed.algebra["PV"]:
        names.append(str(variable))
    return names

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
        
        Filter for strings that start with string type of OWNED schema
        Not rdflib just our made items.
        """
        query = """
        SELECT ?type (COUNT(*) AS ?count)
        WHERE {
            ?entity rdf:type ?type .
            FILTER(STRSTARTS(STR(?type), STR(uni:)) || STRSTARTS(STR(?type), STR(rules:)))
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
        """
        bind: selectedRelation 
        
        return a subject object pair from graph
        subject <relation chosen> object
        """
        query = """
        SELECT ?subject ?object
        WHERE {
            ?subject ?selectedRelation ?object .
        }
        ORDER BY ?subject ?object
        """
        return query

    @staticmethod
    def filter_contains():
        """
        bind: selectedPredicate 
        
        Entities whose field contains selected predicate.
        """
        query = """
        SELECT DISTINCT ?entity
        WHERE {
            ?entity ?selectedPredicate ?value .
            BIND(IF(isIRI(?value), REPLACE(STR(?value), "^.*#", ""), STR(?value)) AS ?text)
            FILTER(CONTAINS(LCASE(?text), LCASE(?searchTerm)))
        }
        """
        return query
    
    @staticmethod
    def get_parents():
        """
        bind: selectedEntity
        
        return every class the entity belongs to.
        """
    
        query = """
        SELECT DISTINCT ?type
        WHERE {
            ?selectedEntity rdf:type ?directType .
            ?directType rdfs:subClassOf* ?type .
            FILTER(STRSTARTS(STR(?type), STR(uni:)) || STRSTARTS(STR(?type), STR(rules:)))
        }
        """
        return query
    
    # ===============================
    # Spec Query Functions
    # Queries required by specification of project
    # ===============================
    @staticmethod
    def foundational_units():
        """
        bind: selectedDegree 
        
        return all units in every major of the degree.
        
        Note in called version it binds to a premade degree from the project outline
        
        We want an intersection of majors such that the units are available to all majors
        under a specific degree. 
        """
        query = """
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
        return query

    @staticmethod
    def average_majors():
        """
        Average majors per study type, BPhil excluded.
        """
        query =  """
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
        return query

    @staticmethod
    def majors_in_location():
        """
        bind: selectedLocation 
        
        Every unit of the major is at that location.
        """
        return """
        SELECT DISTINCT ?major ?title
        WHERE {
            ?major a uni:Major;
                   uni:hasTitle ?title ;
                   uni:hasUnit ?any.
            FILTER NOT EXISTS {
                ?major uni:hasUnit ?unit .
                FILTER NOT EXISTS { ?unit uni:locatedIn ?selectedLocation }
            }
        }
        ORDER BY ?title
        """

    @staticmethod
    def outcome_search():
        """
        bind: searchTerm 
        Major outcomes plus its units' outcomes.
        """
        query = """
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
        return query
    