
# User Manual
The UWA Handbook is a search engine application. It allows for browsing and querying  of a data set through the use of a knowledge graph. The knowledge graph is built from a scraped JSON file containing handbook information. 

It uses OWL ontology, with reasoning rules, SHACL, SPARQL and a small flask web app to search and run queries.

There are some technical design choices and niche interaction / limitation that exist in the system that wont be covered exactly in this document, but if time permits will be afforded as a technical manual for specific details.

There was some initial idea of a larger scope being added into the system, so some code is left abit open and available or has functions that don't get used fully. e.g. upload and use different datasets or schemas. But most are still hardcoded in compliance to project scope.

Design was taken from [PICO](https://picocss.com/) and framework used for front end design. Some code for the back end was also imported from Homework 2 and parsing attempts fitted to this project.

We used an OOP class based design to create the applicaiton with specfic classes having ownership of allocated responsibilities. There are a fair few files completing different 
tasks. The following outlines the basic folder structure and a basic overview of file funtion.

There are some rouge files from initial design before refactoring into a OOP system. However the files outlined below are the most representative of the final outcome.


| Folder | Description |
|---|---|
| `backend/` | `app.py` - Flask application entry point, `main.py` - Initial pipeline for json -> graph `queries.py` - sparql queries for use in application. |
| `backend/builder/` | This takes  parsed and cleaned JSON data and builds a graph using a selected onology schema.|
| `backend/ontology/` | Seperated schema for ontology. Split between `base.py` (basic entities and facts) `rules.py`(Inferred logic). |
| `backend/shapes/` | SHACL validation checks. |
| `backend/utility/` | This covers shared infrastruce + the parser and caching which kind of ended up there.|
| `backend/data/datasets/` | Holds the source data. We named the handbook data 'raw'. Unsure why.|
| `backend/data/schemas/` | This folder contains the generated output schemas |
| `backend/data/graphs/` | This folder contains generated graphs, including cached ones. |
| `frontend/` | Web interface styling and templates in templates/ |


## 2. Installation and running

### Requirements

- **uv** : <https://docs.astral.sh/uv/>
- **python** >= 3.14
- **flask** >= 3.1.3
- **owlready2** >= 0.51
- **pyshacl** >= 0.40.1
- **rdflib** >= 7.6.0

**Notes** Changes are reflected in .toml file if failure occurs.

### Install

Run all commands from `application/` folder:

Sync dependencies
```bash
uv sync
```

Run the application
```bash
uv run python src/backend/app.py
```

Then open <http://127.0.0.1:5001> in a browser.

> Amusingly, port 5000 (standard for flask) kept randomly blocking my macOS computer so had to use port 5001

### Inital Usage constraints

The application doesn't directly load the graph -> loading the reasoner on start stopped design workflow. 

To begin querying, you must build the graph and also load/reason over it so the application can access the knowledge graph. You can click on the corresponding buttons to do this. 

![Homepage](/snapshots/homepage.png)

**Notes** On the first load it can take a while to reason over the graph. This became increasingly annoying so after it is initally reasoned over, it will save a cached version in data/graphs/ as *.nt files. Loading these caches are a lot faster and will be provided so you don't have to sit through the painful reasoning time. 

This only happens when loaded, rebuilding the graph will result in the cache being emptied.

## 2. Schema and Ontology Rules


## 3. Example Queries and how to run them


## 4. Updating schema, graph, ontology, queries. 
I'm under the assumtion theres not an expectation to add and remove 
