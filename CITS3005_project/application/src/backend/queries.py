"""
queries.py - query layer for the UWA handbook knowledge graph.

PURPOSE
    Everything that *asks the graph a question* lives here, so the Flask app
    (app.py) never contains SPARQL itself. The app only:
      1. creates a QueryEngine around the loaded World,
      2. looks up queries in NAMED_QUERIES / ERROR_CHECKS,
      3. displays the QueryResult it gets back.

STATUS
    Framework only. Every function marked TODO is ours to implement.
    Unimplemented queries raise NotImplementedError; run_named() catches this
    and returns a "not implemented yet" message, so the app runs from day one.

HOW TO ADD A QUERY
    Write a function that takes the engine (plus any parameters) and returns a
    QueryResult, then decorate it with @query(...) or @error_check(...).
    It appears in the app automatically.

EXPECTED IN config.py
    SCHEMA_IRI, DATA_IRI            used to build the SPARQL prefixes
    optional: EXTRA_PREFIXES        dict of prefix -> IRI (e.g. one per data module)

NOTE (spec)
    The spec says the SPARQL queries are submitted with the KG script.
    DISCUSS: either build_kg.py imports and runs these, or we confirm that a
    separate queries.py is acceptable.
"""

# =========================
# IMPORTS
# =========================
from dataclasses import dataclass, field
from typing import Callable, Optional

from rdflib.term import URIRef

import backend.utility.config as config


# =========================
# PREFIXES
# =========================
STANDARD_PREFIXES = {
    "rdf":  "http://www.w3.org/1999/02/22-rdf-syntax-ns#",
    "rdfs": "http://www.w3.org/2000/01/rdf-schema#",
    "owl":  "http://www.w3.org/2002/07/owl#",
    "xsd":  "http://www.w3.org/2001/XMLSchema#",
}


def build_prefixes() -> dict[str, str]:
    """All prefixes added to every query. Built from config so swapping the
    dataset namespace never requires editing a query."""
    prefixes = dict(STANDARD_PREFIXES)
    prefixes["uni"] = config.SCHEMA_IRI    # OPEN: agree final prefix names
    prefixes["data"] = config.DATA_IRI
    prefixes.update(getattr(config, "EXTRA_PREFIXES", {}))
    return prefixes


# =========================
# RESULTS
# =========================
# A cell is (display text, full IRI or None). The IRI lets the app turn
# entity values into links to their detail page.
Cell = tuple[str, Optional[str]]


@dataclass
class QueryResult:
    headers: list[str] = field(default_factory=list)
    rows: list[list[Cell]] = field(default_factory=list)
    message: Optional[str] = None   # e.g. ASK answer, row count, error text
    ok: bool = True


# =========================
# ENGINE
# =========================
class QueryEngine:
    """Runs SPARQL over the loaded owlready2 World through rdflib.

    DECISION: rdflib rather than owlready2's native SPARQL.
      Why: full SPARQL support, and results carry variable names, which the
      app needs for table headers. Spec also lists RDFLib for SPARQL.
    """

    def __init__(self, world):
        self.world = world
        self.graph = world.as_rdflib_graph()
        self.prefixes = build_prefixes()

    def prefix_block(self) -> str:
        return "\n".join(f"PREFIX {p}: <{iri}>" for p, iri in self.prefixes.items())

    def run(self, sparql: str, add_prefixes: bool = True) -> QueryResult:
        text = f"{self.prefix_block()}\n{sparql}" if add_prefixes else sparql
        try:
            result = self.graph.query(text)
        except Exception as exc:
            return QueryResult(ok=False, message=f"Query failed: {exc}")

        if result.type == "ASK":
            return QueryResult(message=f"Answer: {result.askAnswer}")

        if result.type == "SELECT":
            headers = [str(v) for v in result.vars]
            rows = [[self.cell(value) for value in row] for row in result]
            return QueryResult(headers=headers, rows=rows, message=f"{len(rows)} result(s)")

        # CONSTRUCT / DESCRIBE return triples
        rows = [[self.cell(s), self.cell(p), self.cell(o)] for s, p, o in result]
        return QueryResult(headers=["subject", "predicate", "object"], rows=rows,
                           message=f"{len(rows)} triple(s)")

    def cell(self, value) -> Cell:
        if value is None:
            return ("", None)
        if isinstance(value, URIRef):
            return (self.shorten(str(value)), str(value))
        return (str(value), None)

    def shorten(self, iri: str) -> str:
        """Full IRI -> prefix:local, using the longest matching namespace."""
        for prefix, base in sorted(self.prefixes.items(), key=lambda kv: -len(kv[1])):
            if iri.startswith(base):
                return f"{prefix}:{iri[len(base):]}"
        return iri


# =========================
# HELPERS
# =========================
def sparql_string(text: str) -> str:
    """Escape user text for safe use as a SPARQL string literal.
    Always use this when putting user input into a query."""
    escaped = text.replace("\\", "\\\\").replace('"', '\\"').replace("\n", " ")
    return f'"{escaped}"'


# =========================
# REGISTRY
# =========================
@dataclass
class NamedQuery:
    key: str
    title: str
    description: str
    func: Callable[..., QueryResult]
    params: tuple[str, ...] = ()


NAMED_QUERIES: dict[str, NamedQuery] = {}   # shown on the app's Query page
ERROR_CHECKS: dict[str, NamedQuery] = {}    # shown on the app's Errors page


def query(key, title, description, params=(), registry=None):
    """Decorator: register a function as a named query."""
    def wrap(func):
        target = NAMED_QUERIES if registry is None else registry
        target[key] = NamedQuery(key, title, description, func, tuple(params))
        return func
    return wrap


def error_check(key, title, description):
    """Decorator: register a function as a data error check (no parameters)."""
    return query(key, title, description, registry=ERROR_CHECKS)


def run_named(registry, key, engine, **params) -> QueryResult:
    """Run a registered query safely; never raises, always returns a QueryResult."""
    nq = registry.get(key)
    if nq is None:
        return QueryResult(ok=False, message=f"Unknown query: {key}")
    missing = [p for p in nq.params if not params.get(p)]
    if missing:
        return QueryResult(ok=False, message=f"Missing parameter(s): {', '.join(missing)}")
    try:
        return nq.func(engine, **{p: params[p] for p in nq.params})
    except NotImplementedError:
        return QueryResult(ok=False, message=f"'{nq.title}' is not implemented yet.")
    except Exception as exc:
        return QueryResult(ok=False, message=f"'{nq.title}' failed: {exc}")


# =========================
# REQUIRED QUERIES (spec, deliverable 2)
# =========================
@query("foundational", "Foundational units",
       "Degree and unit pairs where the unit is required in all majors of that degree.")
def foundational_units(engine: QueryEngine) -> QueryResult:
    # TODO: write SPARQL, then: return engine.run(SPARQL)
    raise NotImplementedError


@query("avg_majors", "Average major options per degree type",
       "Standard / Combined / Honours, excluding the Bachelor of Philosophy.")
def average_majors(engine: QueryEngine) -> QueryResult:
    # TODO
    raise NotImplementedError


@query("albany_majors", "Majors completable in Albany",
       "Majors that can be completed in Albany.")
def albany_majors(engine: QueryEngine) -> QueryResult:
    # TODO
    raise NotImplementedError


@query("outcome_search", "Search major outcomes",
       "Majors whose outcomes contain the given text (e.g. 'data analysis').",
       params=("text",))
def outcome_search(engine: QueryEngine, text: str) -> QueryResult:
    # TODO: use sparql_string(text) when inserting the user's text
    raise NotImplementedError


# =========================
# OUR OWN QUERIES
# =========================
# TODO: add more @query functions here (filters, aggregations, nested queries...)


# =========================
# ERROR CHECKS (shown on the app's Errors page)
# =========================
@error_check("self_prerequisite", "Units that are their own prerequisite",
             "A unit can't be its own prerequisite.")
def self_prerequisite(engine: QueryEngine) -> QueryResult:
    # TODO
    raise NotImplementedError


@error_check("prerequisite_cycles", "Prerequisite cycles",
             "Units that indirectly require themselves (A -> B -> A).")
def prerequisite_cycles(engine: QueryEngine) -> QueryResult:
    # TODO: SPARQL, or an SCC algorithm in Python over engine.world
    raise NotImplementedError


@error_check("level1_credit_limit", "Majors over the level 1 credit limit",
             "No major should exceed 48 credit points at level 1.")
def level1_credit_limit(engine: QueryEngine) -> QueryResult:
    # TODO
    raise NotImplementedError


@error_check("degree_without_major", "Degrees without a major",
             "A degree must have at least one major.")
def degree_without_major(engine: QueryEngine) -> QueryResult:
    # TODO
    raise NotImplementedError
