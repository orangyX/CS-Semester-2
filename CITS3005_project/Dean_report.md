
# Report 

1. Design choices

This assignment was a joint effort with a expectation on learning. In such we took the direction of a flask application as an introductory to application frameworks. 

We took OOP prinicples to apply to our approach, encapulating data and moduarlising function. The intial design handled everything for a draft and was moved into a class based system. The intention was to give availabilty to additional features, which some were lost under time constraints. 

We decided to split the responsibility of each scheama. Having a file be responisble for different parts of the ontology. Asserted facts, Infered fact sand SHACL validation. This allowed us to directly modify conditions, rules, entity hierarchy and relations without interfering with the greater system. We also used 2 name spaces to represent asserted facts vs infered facts. This gave us a clean seperation between the 2 types of facts.

Another key design feature is that we convert the ontology graph into a RDF graph upon loading. This was to support SHACL and familiarity with querying. A nice feature of this decision was allowing a caching, where RDF easily converts into .nt files.

Some rules were pushed into SHACL. This provided us with a greater understanding of the system and inference that occured
|Problem	|Before reasoning|After reasoning|
|---|---|---|
|Degree has no majors|	40	|35|
|Degree is referenced but not in the dataset	|35|	35|
|Unit has no outcomes|	11|	11|
|Unit is its own prerequisite (directly or through a cycle)	|2|	15|
|Unit is referenced but not in the dataset	|193|	193|
|Unit requires (directly or indirectly) a unit that is not in the dataset	|399|	1503|

While some rules were caught and fixed during inference. Some actually increased. Specifically cycled prerequisites. The implication is that once transitivity of units was applied, more cyclic relations appeared. This also affected units outside the dataset, where many units, at some point in the trasitive chain point to a unit outside the data set. The count increases dramatically as every unit inside a chain is included.

(It's slightly annoying to see as it feels like the ontology is incomplete or incorrect and should be handled.)

Discovered during Homework 2, we could bind specific search terms to a query. This allows a user to view any entity under a specific query.

Search as a query was used to find any item, object, relation found inside the knowledge graph. This sometimes returned graph meta data. This was an intended design, we had the idea to provide dynamic filtering to the search so you could find relevant informatio including graph meta information.

2. Tools
There are 3 types of notable tools used during this project. 

"uv" and "Flask"

These provided the frame work for the application. 
uv is a package manager and I find it so helpful for shared projects as it handles the virtual enviroment and dependancies for us. This just reduces the load and understanding needed to set up and contribute to the project. It is recommended. 

Flask is a webframework, on the scale applied it was intutive for setting up quick end points, however i don't think we explored it enough to provide a complete picture of its capabibilities.

The next type of tools were built tools used for specific interactions, this includes Shacl, Regular expression and inspect

pySHACL was described in the project overview by "possibly including pySHACL". We decided to implement this. As discussed in part 1, pySHACL was incredibly useful for the overall understanding of our ruleset. While not nessessarily required it provided an overview of the changes made to the graph and the expectations associated. I would continue to use it in most my ontologies. If more time permitted I would've liked to continue with it and update the ruleset in occordance to the findins.

Regular expression is a built in python library. This is something we are taught but never really shown how it looks in practice, so it was a great opertunity to attempt it. Throughout the project, specifically for parsing and cleaning, I relied on it to help match patterns and resolve larger sets of corrupt data instead of explicitly mapping them. I thought it was useful and aligned with the assumptions we had to make about the dataset.

A small notable tool found was 'inspect'. This turned out to be an extremely elpful tool for a single function. It allows the inspection of classes and retrieve meta information about it. 

Lastly, the use of AI. In general I attempt to keep my AI use to a minimum with my most used being gemini as it appears on google search. Based on recommendation Claude was explored and used for this project. It was mainly used for debugging, checking syntax, explaining new tools and brainstorming. It was helpful but had a few small issue I think need to be managed if you use it. From debugging it gained context and when brainstorming would randomly drop 4 file fixes. Design decisions and specific suggested fixes had to be audited as it would randomly suggest something that didn't fit the idea. It was better to understand the bug and implement based on the suggested ideas. The other issue, is the insitance on fixing minor issues, this could be function descriptions, shared ideas, variable naming and the informal communication in comments left for partner. There's a want to 'fix' those issues but I think would lead to a ship of theseus situtation. Otherwise for the use of quickly being able to understand new tools and actually use them, it was very helpful.

3. Time
Parsing and cleaning data
~5-6 hours. Even importing other attempts, it needs constant revision and refactoring.

Creating ontology and rules (Include shapes)
~2-3 hours. was mostly just thinking and discussing, most was implemented into code by Partner and needed minor corrections as application progressed and seperation was decided on.

Building the graph.
~2 hours. once data was understood and structure was found, it was quick to implement, with small helpers whenever an issue occured.

Intergrating backend pipeline
~20-30 minutes. With everything set up, linking this to a single pipeline was relatively painless.

Implementing flask end points
~5 hours. This isn't indicitive of actual work but enjoyment with partner in trying new ideas and adding new features.

Implementing queries
~ 1-2 hour. Because i was able to import lots of structre and ideas from Homework 2, this was relatively easy and just needed changes to fit the new system and requirements.

Frontend intergration.
0 hours. All front end stuff was handled by my partner. (HTML, CSS)

4. Contributions
My partner and I have a strong relationship, most components were done in tandam with each other, either in person or over discord sharing the sceen. We worked through ideas, bugs and issues, fixes and implementation strategy together. This lead to a strongly connected collaborative effort, when some files were fast we could move on and start the next, this mostly gave us an equal contribution overall. Below is the files we worked on, this is also documented in the user manual.


