"""
Some quick notes, alot of this ive done for fun with some basic I/O
for exploring the graph, it may crash if inputs are invalid, I havent
fully implemented valiation of inputs, but for the most part 
if you explore using a happy path should function as intended and 
interact with the graph.

I've mostly left as an integer based input system so that its easier to use
but yeah, definely crashes if you do weird things hahahahha

Luckily, adding increased functionality is relatively sane and queries can be
added with relative ease. Currently, its extremely buggy lmao

I initially tried a web scraper to do the whole world, but it presented itself
as too much of a challenge
I also wanted full command line control but i think time constraints limit 
so me to exact hardcoded queries/graph for the time being.

It's fun but also a homework task so.
"""

from rdflib import Graph, Namespace, RDF, RDFS, Literal

g = Graph()
g.parse("made_in_abyss_graph.rdf", format="xml")

MIA = Namespace("http://example.com/made-in-abyss/")

# ===============================
# SPARQL Query Functions
# ===============================

# ===============================
# FILTER Query Functions
# ===============================

def filter_by_name():
    query = """
    SELECT ?entity
    WHERE {
        ?entity rdfs:label ?label .
        FILTER(CONTAINS(LCASE(STR(?label)), LCASE(?searchTerm)))
    }
    ORDER BY ?label
    """
    return query

def filter_by_danger():
    return """
    SELECT DISTINCT ?entity
    WHERE {
        ?entity mia:hasDangerLevel ?danger .
        ?danger rdfs:label ?dangerLabel .
    }
    ORDER BY ?entity
    """

def filter_by_status():
    return """
    SELECT DISTINCT ?entity
    WHERE {
        ?entity mia:hasStatus ?status .
        FILTER(LCASE(STR(?status)) = LCASE(STR(?selectedStatus)))
    }
    ORDER BY ?entity
    """

def filter_by_depth():
    return """
    SELECT DISTINCT ?entity ?depth
    WHERE {
        ?entity mia:hasDepth ?depth .
        FILTER(?depth >= ?minimumDepth)
    }
    ORDER BY ?depth
    """
    
# ===============================
# Aggregation Query Functions
# ===============================
def count_by_type():
    return """
    SELECT ?type (COUNT(?entity) AS ?count)
    WHERE {
        ?entity rdf:type ?type .
        ?type rdfs:label ?typeLabel .
    }
    GROUP BY ?type
    ORDER BY DESC(?count)
    """

def count_beasts_by_layer():
    return """
    SELECT ?layer (COUNT(?beast) AS ?count)
    WHERE {
        ?beast rdf:type/rdfs:subClassOf* mia:Beast .
        ?beast mia:livesIn ?layer .
    }
    GROUP BY ?layer
    ORDER BY DESC(?count)
    """

def count_artifacts_by_grade():
    return """
    SELECT ?grade (COUNT(?artifact) AS ?count)
    WHERE {
        ?artifact rdf:type/rdfs:subClassOf* mia:Artifact .
        ?artifact mia:hasGrade ?grade .
    }
    GROUP BY ?grade
    ORDER BY DESC(?count)
    """

def count_by_danger():
    return """
    SELECT ?danger (COUNT(?entity) AS ?count)
    WHERE {
        ?entity mia:hasDangerLevel ?danger .
    }
    GROUP BY ?danger
    ORDER BY DESC(?count)
    """
# ===============================
# UTILITY Query Functions
# ===============================
def get_label():
    query = """
    SELECT ?label
    WHERE {
        ?selectedObject rdfs:label ?label .
    }
    """
    return query

def list_entities():
    return """
    SELECT DISTINCT ?entity ?label
    WHERE {
        {?entity ?predicate ?object .}
        UNION {?subject ?predicate ?entity .}
        FILTER(isIRI(?entity))
        OPTIONAL {?entity rdfs:label ?label .}
    }
    ORDER BY ?entity
    """
def list_entity_types():
    query = """
    SELECT DISTINCT ?type
    WHERE {
        ?entity rdf:type ?type .
        ?type rdfs:label ?label.
    }
    ORDER BY ?type
    """
    return query

def list_by_entity_type():
    query = """ SELECT ?entity
    WHERE {
        ?entity rdf:type/rdfs:subClassOf* ?selectedType .
    }
    ORDER BY ?entity
    """
    return query

def list_relations():
    query = """
    SELECT DISTINCT ?relation
    WHERE {
        ?subject ?relation ?object .
        FILTER(?relation != rdf:type)
        FILTER(?relation != rdfs:label)
    }
    ORDER BY ?relation
    """
    return query

def query_by_relation():
    return """
    SELECT ?subject ?object
    WHERE {
        ?subject ?selectedRelation ?object .
    }
    ORDER BY ?subject ?object
    """
    
    
# ===============================
# Command-Line Interface
# ===============================

class GraphUtility:
    """
    Basic graph functions for I/O
    """
    def __init__(self, graph):
        self.graph = graph
    
    def get_input_int(self, message, upperBound):
        while True:
            try:
                choice = int(input(f"{message} (1-{upperBound}, 0 to go back): "))

            except ValueError:
                print("Invalid choice")
                continue
            
            if choice == 0:
                return None

            if 1 <= choice <= upperBound:
                return choice - 1
            
            print("Invalid choice.")
    
    def get_string_input(self, message):
        return input(f"{message}: ").strip()
    
    def run(self, query, init_bindings=None):
        return list(self.graph.query(query, initNs={"mia": MIA, "rdf": RDF, "rdfs": RDFS}, initBindings=init_bindings or {}))
    
    def display_value(self, value):
        if value is None:
            return ""

        text = str(value)

        if text.startswith(str(MIA)):
            return text.removeprefix(str(MIA)).replace("_", " ")

        if text.startswith(str(RDFS)):
            return text.removeprefix(str(RDFS)).replace("_", " ")

        return text

    def print_single(self, query, init_bindings=None):
        results = self.run(query, init_bindings)
        
        for row_number, row in enumerate(results, start=1):
            print(f"{row_number}. {self.display_value(row[0])}")

        return results
    
    def print_two(self, query, relation, init_bindings=None):
        results = self.run(query, init_bindings)
        
        for row_number, row in enumerate(results, start=1):
            subject = self.display_value(row[0])
            object_value = self.display_value(row[1])
            print(f"{row_number}. {subject} {relation} {object_value}")

class KnowledgeGraphCLI:
    def __init__(self, utility):
        self.utility = utility
        self.running = True
        self.menu_stack = ["main"]

        self.main_menu = [
            ("1", "Browse the graph", self.open_browse),
            ("2", "Search by filers", self.open_filter),
            ("3", "Search by aggregation", self.open_aggregate),
            ("4", "Advanced searches", self.open_advanced),
            ("0", "Exit", self.exit_cli)
        ]
        
        self.browse_graph = [
            ("1", "List entities", self.list_entities),
            ("2", "List entity types", self.list_entity_types),
            ("3", "List by entity type", self.list_by_entity_type),
            ("4", "List relations", self.list_relations),
            ("5", "Query relations", self.query_relation),
            ("0", "Return", self.go_back)
        ]
        
        self.filter_graph = [
            ("1", "Filter by entity name", self.filter_by_entity_name),
            ("2", "Filter by danger level", self.filter_by_danger_level),
            ("3", "Filter by status", self.filter_by_status),
            ("4", "Filter by layer", self.filter_by_layer),
            ("5", "Filter by depth", self.filter_by_depth),
            ("0", "Return", self.go_back)
        ]
        
        self.aggregate_graph = [
            ("1", "Count entites by type", self.count_entities_by_type),
            ("2", "Count beasts by layer", self.count_beasts_by_layer),
            ("3", "Count artifacts", self.count_artifacts),
            ("4", "Count entities by danger level", self.count_entities_by_danger_level),
            ("5", "Count locations in each layer", self.count_locations_in_layer),
            ("0", "Return", self.go_back)        
        ]
        
        self.advanced_search =[
            # Can be for nested objects
            ("0", "Return", self.go_back)  
        ]


    # ===============================
    # Command-Line Display
    # ===============================

    def start(self):
        while self.running:
            
            current_menu = self.menu_stack[-1]
            
            if current_menu == "main":
                self.display_commands(self.main_menu)
            elif current_menu == "browse":
                self.display_commands(self.browse_graph)
            elif current_menu == "filter":
                self.display_commands(self.filter_graph)
            elif current_menu == "aggregate":
                self.display_commands(self.aggregate_graph)
            elif current_menu == "advanced":
                self.display_commands(self.advanced_search)

    def display_commands(self, commands):
        print("\n==============================")
        print("Made in Abyss Knowledge Graph")
        print("==============================\n")
        
        for number, description, _ in commands:
            print(f"{number}. {description}")

        choice = input("Choose an option as integer input: ").strip()

        for number, _, command in commands:
            if choice == number:
                command()
                return

    print("Invalid option.")

    # ===============================
    # Menu Navigation
    # ===============================
    def open_browse(self):
        self.menu_stack.append("browse")
    def open_filter(self):
        self.menu_stack.append("filter")
    def open_aggregate(self):
        self.menu_stack.append("aggregate")
    def open_advanced(self):
        self.menu_stack.append("advanced")
        
    def go_back(self):
        if len(self.menu_stack) > 1:
            self.menu_stack.pop()
    def exit_cli(self):
        self.running = False
        print("Exiting.")
    
    # ===============================
    # Utility Queries
    # ===============================
    
    # ===============================
    # List Queries 
    # ===============================

    def list_entities(self):
        query = list_entities()
        return self.utility.print_single(query)
    
    def list_entity_types(self):
        query = list_entity_types()
        return self.utility.print_single(query)
    
    def list_relations(self):
        query = list_relations()
        return self.utility.print_single(query)
        
    def list_by_entity_type(self):
        types = self.list_entity_types()
        choice = self.utility.get_input_int("Pick an entity type by integer input: ", len(types))
        if choice is None:
            return
        selected_type = types[int(choice)][0]
        
        print(selected_type)
        
        query = list_by_entity_type()
        return self.utility.print_single(query, init_bindings={"selectedType": selected_type})

    def query_relation(self):
        relations = self.list_relations()
        choice = self.utility.get_input_int("Pick a relation by integer input: ", len(relations))
        if choice is None:
            return
        selected_relation = relations[int(choice)][0]
        relation = self.utility.display_value(selected_relation)
        
        query = query_by_relation()
        self.utility.print_two(query, relation, init_bindings={"selectedRelation": selected_relation})

    # ===============================
    # Filter Queries
    # ===============================
    def filter_by_entity_name(self):
        search_term = self.utility.get_input_sting("Enter part of an entity name: ")
        self.utility.print_single(filter_by_name(), init_bindings={ "searchTerm": Literal(search_term)})

    def filter_by_danger_level(self):
        pass
    
    def filter_by_status(self):
        pass

    def filter_by_layer(self):
        pass

    def filter_by_depth(self):
        pass

    # ===============================
    # Counting Queries
    # ===============================
    def count_entities_by_type(self):
        pass
    def count_beasts_by_layer(self):
        pass
    def count_artifacts(self):
        pass
    def count_entities_by_danger_level(self):
        pass
    def count_locations_in_layer(self):
        pass
    
if __name__ == "__main__":
    utility = GraphUtility(g)
    cli = KnowledgeGraphCLI(utility)
    cli.start()