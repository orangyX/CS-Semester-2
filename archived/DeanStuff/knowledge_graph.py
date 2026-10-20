
from rdflib import Graph, Namespace, RDF, RDFS, Literal, XSD


MIA = Namespace("http://example.com/made-in-abyss/")

g = Graph()

g.bind("mia", MIA)
g.bind("rdf", RDF)
g.bind("rdfs", RDFS)


# Entity hierarchy
g.add((MIA.Entity, RDF.type, RDFS.Class))
g.add((MIA.Place, RDF.type, RDFS.Class))
g.add((MIA.District, RDF.type, RDFS.Class))
g.add((MIA.Location, RDF.type, RDFS.Class))
g.add((MIA.Object, RDF.type, RDFS.Class))
g.add((MIA.Item, RDF.type, RDFS.Class))
g.add((MIA.Artifact, RDF.type, RDFS.Class))
g.add((MIA.ArtifactGrade, RDF.type, RDFS.Class))
g.add((MIA.Living_Thing, RDF.type, RDFS.Class))
g.add((MIA.Beast, RDF.type, RDFS.Class))
g.add((MIA.Human, RDF.type, RDFS.Class))
g.add((MIA.Narehate, RDF.type, RDFS.Class))

# Sub structures 
g.add((MIA.Place, RDFS.subClassOf, MIA.Entity))
g.add((MIA.Object, RDFS.subClassOf, MIA.Entity))
g.add((MIA.Living_Thing, RDFS.subClassOf, MIA.Entity))

g.add((MIA.Location, RDFS.subClassOf, MIA.Place))
g.add((MIA.District, RDFS.subClassOf, MIA.Place))

g.add((MIA.Item, RDFS.subClassOf, MIA.Object))
g.add((MIA.Artifact, RDFS.subClassOf, MIA.Item))

g.add((MIA.Beast, RDFS.subClassOf, MIA.Living_Thing))
g.add((MIA.Human, RDFS.subClassOf, MIA.Living_Thing))
g.add((MIA.Narehate, RDFS.subClassOf, MIA.Human))

# Meta Data
g.add((MIA.DangerLevel, RDF.type, RDFS.Class))
g.add((MIA.WhistleRank, RDF.type, RDFS.Class))
g.add((MIA.ArtifactGrade, RDF.type, RDFS.Class))

# Labels
class_labels = {
    MIA.Entity: "Entity",
    MIA.Place: "Place",
    MIA.District: "District",
    MIA.Location: "Location",
    MIA.Object: "Object",
    MIA.Item: "Item",
    MIA.Artifact: "Artifact",
    MIA.Living_Thing: "Living Thing",
    MIA.Beast: "Beast",
    MIA.Human: "Human",
    MIA.Narehate: "Narehate",
    MIA.ArtifactGrade: "Artifact Grade",
    MIA.DangerLevel: "Danger Level",
    MIA.WhistleRank: "Whistle Rank",
}

for resource, label in class_labels.items():
    g.add((resource, RDFS.label, Literal(label)))
      
# ===============================
# Predicates
# ===============================
hasDescription = MIA.hasDescription

contains = MIA.contains
locatedIn = MIA.locatedIn
hasWhistleRequirement = MIA.hasWhistleRequirement
hasDepth = MIA.hasDepth
minDepth = MIA.minDepth
maxDepth = MIA.maxDepth

ownedBy = MIA.ownedBy
sourcedFrom = MIA.sourcedFrom
hasGrade = MIA.hasGrade
hasEffect = MIA.hasEffect

lastKnownLocation = MIA.lastKnownLocation
hasGender = MIA.hasGender
hasSpecies = MIA.hasSpecies
hasStatus = MIA.hasStatus
hasOccupation = MIA.hasOccupation
hasWhistleRank = MIA.hasWhistleRank
Unknown_Location = MIA.Unknown_Location
Whistle = MIA.Whistle

livesIn = MIA.livesIn
hasDangerLevel = MIA.hasDangerLevel


# ===============================
# Entities
# ===============================
Unknown_Danger = MIA.Unknown_Danger
Harmless_Danger = MIA.Harmless_Danger
Insignificant_Danger = MIA.Insignificant_Danger
Caution_Danger = MIA.Caution_Danger
Absurd_Danger = MIA.Absurd_Danger
Deadly_Danger = MIA.Deadly_Danger
Serious_Danger = MIA.Serious_Danger
Extraordinary_Danger = MIA.Extraordinary_Danger

danger_levels = {
    Unknown_Danger: "Unknown",
    Harmless_Danger: "Harmless",
    Insignificant_Danger: "Insignificant",
    Caution_Danger: "Caution",
    Absurd_Danger: "Absurd",
    Deadly_Danger: "Deadly",
    Serious_Danger: "Serious",
    Extraordinary_Danger: "Extraordinary",
}

for danger, label in danger_levels.items():
    g.add((danger, RDF.type, MIA.DangerLevel))
    g.add((danger, RDFS.label, Literal(label)))
    
Bell = MIA.Bell                 
RedWhistle = MIA.RedWhistle     
BlueWhistle = MIA.BlueWhistle   
MoonWhistle = MIA.MoonWhistle   
BlackWhistle = MIA.BlackWhistle 
WhiteWhistle = MIA.WhiteWhistle 

whistle_ranks = {
    Bell: "Bell",
    RedWhistle: "Red Whistle",
    BlueWhistle: "Blue Whistle",
    MoonWhistle: "Moon Whistle",
    BlackWhistle: "Black Whistle",
    WhiteWhistle: "White Whistle",
}

for whistle, label in whistle_ranks.items():
    g.add((whistle, RDF.type, MIA.WhistleRank))
    g.add((whistle, RDFS.label, Literal(label)))
 
 
g.add((Bell, RDF.type, MIA.Item))
g.add((RedWhistle, RDF.type, MIA.Item))
g.add((BlueWhistle, RDF.type, MIA.Item))
g.add((MoonWhistle, RDF.type, MIA.Item))
g.add((BlackWhistle, RDF.type, MIA.Item))
g.add((WhiteWhistle, RDF.type, MIA.Item))

Fourth_Grade = MIA.Fourth_Grade
Third_Grade = MIA.Third_Grade
Second_Grade = MIA.Second_Grade
First_Grade = MIA.First_Grade
Special_Grade = MIA.Special_Grade

grades = {
    Fourth_Grade: "Fourth Grade",
    Third_Grade: "Third Grade",
    Second_Grade: "Second Grade",
    First_Grade: "First Grade",
    Special_Grade: "Special Grade",
}

for grade, label in grades.items():
    g.add((grade, RDF.type, MIA.ArtifactGrade))
    g.add((grade, RDFS.label, Literal(label)))
 
g.add((Fourth_Grade, hasDescription, Literal("Fourth Grade Artifacts are common Relics, usually found on the upper layers. They are regarded as insignificant or are of uncertain use and incapable of replacing existing tools")))
g.add((Third_Grade, hasDescription, Literal("Third Grade Artifacts are described as being extremely valuable or useful. They can help with cave raiding.")))
g.add((Second_Grade, hasDescription, Literal("Second Grade Artifacts are very rare and usually have very specialized abilities. They introduce entirely new concepts and can change people's way of life.")))
g.add((First_Grade, hasDescription, Literal("The second most valuable class of Artifact that can be found. These are items that are extremely rare or versatile. They can change the balance of power between countries and are extremely useful when cave raiding in the deeper levels.")))
g.add((Special_Grade, hasDescription, Literal("The most valuable class of Artifacts that can be found. These are items that can change the world and disrupt the balance of power between nations. Retrieving a single one to the surface can guarantee a prosperous future for a whole city or vastly increase the military potential of a country, depending on its use.")))

g.add((Unknown_Location, RDFS.label, Literal("Unknown Location")))
g.add((Whistle, RDFS.label, Literal("Whistle")))


# ===============================
# Overworld Locations
# ===============================
World = MIA.World
Beoluska = MIA.Beoluska
Jisweku = MIA.Jisweku
Sereny = MIA.Sereny

Orth = MIA.Orth
North_Orth = MIA.North_Orth
South_Orth = MIA.South_Orth
East_Orth = MIA.East_Orth
West_Orth = MIA.West_Orth
Central_Orth = MIA.Central_Orth

Gate_to_the_Netherworld = MIA.Gate_to_the_Netherworld
The_Wharf = MIA.The_Wharf 
The_Grand_Pier = MIA.The_Grand_Pier
Orth_Windmills = MIA.Orth_Windmills
Belchero_Orphanage = MIA.Belchero_Orphanage
Delver_Guild_HQ = MIA.Delver_Guild_HQ

The_Abyss = MIA.The_Abyss
Layer_1 = MIA.Layer_1
Layer_2 = MIA.Layer_2
Layer_3 = MIA.Layer_3
Layer_4 = MIA.Layer_4
Layer_5 = MIA.Layer_5
Layer_6 = MIA.Layer_6
Iruburu = MIA.Iruburu
Layer_7 = MIA.Layer_7

# ===============================
# Specific Locations
# ===============================
# Layer 1 specific locations
Abode_of_Trees_and_Fossils = MIA.Abode_of_Trees_and_Fossils
Big_Gondola = MIA.Big_Gondola
Burial_Tower = MIA.Burial_Tower
Gate_to_the_Netherworld = MIA.Gate_to_the_Netherworld
The_Guiding_Tree = MIA.The_Guiding_Tree
Ominaki_Falls = MIA.Ominaki_Falls
Seat_of_the_Waterfall = MIA.Seat_of_the_Waterfall
Stargazing_Hill = MIA.Stargazing_Hill
Stone_Ark = MIA.Stone_Ark
Twisting_Crag = MIA.Twisting_Crag
Wind_Riding_Windmills = MIA.Wind_Riding_Windmills
Wuthering = MIA.Wuthering

# Layer 2 specific locations
Heavens_Waterfall = MIA.Heavens_Waterfall
The_Inverted_Forest = MIA.The_Inverted_Forest
Hells_Crossing = MIA.Hells_Crossing
Joint_Delving_Site = MIA.Joint_Delving_Site
Seeker_Camp = MIA.Seeker_Camp
Sky_Hunting_Grounds = MIA.Sky_Hunting_Grounds
Rohana_Fountainhead = MIA.Rohana_Fountainhead
Sky_Jellyfish = MIA.Sky_Jellyfish
Sleeping_Bed_of_Mushrooms = MIA.Sleeping_Bed_of_Mushrooms

# Layer 3 specific locations
Baracocha_Corridors = MIA.Baracocha_Corridors
Cumulonimbus_Point = MIA.Cumulonimbus_Point
Ghostly_Roots = MIA.Ghostly_Roots
Greenery_Layer = MIA.Greenery_Layer
The_Imprisoned_Pirate_Ship = MIA.The_Imprisoned_Pirate_Ship
Rumbling_Grounds_of_the_Strong = MIA.Rumbling_Grounds_of_the_Strong
Tallowstone_Layer = MIA.Tallowstone_Layer

# Layer 4 specific locations
Acid_Waterfall = MIA.Acid_Waterfall
Dead_Crystal_Cave = MIA.Dead_Crystal_Cave
Eternal_Wave_Crests = MIA.Eternal_Wave_Crests
Flat_Creeper_Spike_Stretch = MIA.Flat_Creeper_Spike_Stretch
Forest_of_Crooked_Stone_Columns = MIA.Forest_of_Crooked_Stone_Columns
Gas_Plume_Deposit = MIA.Gas_Plume_Deposit
Flat_Creeper_Squid_Spawning_Grounds = MIA.Flat_Creeper_Squid_Spawning_Grounds
Garden_of_the_Flowers_of_Fortitude = MIA.Garden_of_the_Flowers_of_Fortitude
Nanachis_Hideout = MIA.Nanachis_Hideout
Old_Beasts_Hidden_Hot_Spring = MIA.Old_Beasts_Hidden_Hot_Spring
Spiral_Ice_Pillars = MIA.Spiral_Ice_Pillars
Steel_Fossil_Assemblage = MIA.Steel_Fossil_Assemblage
Sticky_Clouds = MIA.Sticky_Clouds

# Layer 5 specific locations
Crystallized_Water_Supports = MIA.Crystallized_Water_Supports
Frost_Dragonbones = MIA.Frost_Dragonbones
Ido_Front = MIA.Ido_Front
Altar_of_the_Absolute_Boundary = MIA.Altar_of_the_Absolute_Boundary
Sandstone_Region = MIA.Sandstone_Region

# ===============================
# Artifacts
# ===============================
Princess_Bosom = MIA.Princess_Bosom
Rock_Top = MIA.Rock_Top 
Star_Compass = MIA.Star_Compass
Sun_Sphere = MIA.Sun_Sphere
Curse_Warding_Box = MIA.Curse_Warding_Box
Forgetter = MIA.Forgetter
Thousand_Men_Pins = MIA.Thousand_Men_Pins
Gentle_Knock = MIA.Gentle_Knock
Blaze_Reap = MIA.Blaze_Reap 
Fog_Weave = MIA.Fog_Weave 
Unheard_Bell = MIA.Unheard_Bell
Altar_of_the_Absolute_Boundary_Relic = MIA.Altar_of_the_Absolute_Boundary_Relic
Canopy_Unto_Dawn = MIA.Canopy_Unto_Dawn
Far_Caress = MIA.Far_Caress
Gangway = MIA.Gangway
Shaker = MIA.Shaker
Sparagmos = MIA.Sparagmos
Third_Works = MIA.Third_Works
Zoaholic = MIA.Zoaholic

# ===============================
# Inhabitants
# ===============================
Belchero = MIA.Belchero  
Bellmore = MIA.Bellmore 
Bido = MIA.Bido 
Bondrewd = MIA.Bondrewd 
Cravagli = MIA.Cravagli
Gallice = MIA.Gallice 
Gueira = MIA.Gueira 
Hablog = MIA.Hablog 
Irumyuui = MIA.Irumyuui 
Jiruo = MIA.Jiruo  
Kiyui = MIA.Kiyui  
Laffi = MIA.Laffi  
Lyza = MIA.Lyza 
Marulk = MIA.Marulk  
Mitty = MIA.Mitty  
Nishagora = MIA.Nishagora 
Nat = MIA.Nat  
Nanachi = MIA.Nanachi  
Neyozel = MIA.Neyozel 
Ozen = MIA.Ozen 
Prushka = MIA.Prushka 
Reg = MIA.Reg
Remayo = MIA.Remayo 
Riko = MIA.Riko 
Shiggy = MIA.Shiggy  
Simred = MIA.Simred 
Srajo = MIA.Srajo
Torka = MIA.Torka  
Wakuna = MIA.Wakuna 
Yataramar = MIA.Yataramar 
Yelme = MIA.Yelme 
Zapo = MIA.Zapo 

# ===============================
# Beasiary
# ===============================
Amakagame = MIA.Amakagame
Amaranthine_Deceptor = MIA.Amaranthine_Deceptor
Crimson_Splitjaw = MIA.Crimson_Splitjaw 
Corpse_Weeper = MIA.Corpse_Weeper
Demonfish = MIA.Demonfish
Hamashirama = MIA.Hamashirama
Hammerbeak = MIA.Hammerbeak 
Inbyo = MIA.Inbyo
Kazura_Squid = MIA.Kazura_Squid
Madokajack = MIA.Madokajack
Meinastilim = MIA.Meinastilim
Neritantan = MIA.Neritantan
Orb_Piercer = MIA.Orb_Piercer
Ottobas = MIA.Ottobas  
Rohana = MIA.Rohana 
Shroombear = MIA.Shroombear
Silkfang = MIA.Silkfang
Stingerhead = MIA.Stingerhead


# ===============================
# Artifact Entities
# ===============================

g.add((Princess_Bosom, RDF.type, MIA.Artifact))
g.add((Princess_Bosom, RDFS.label, Literal("Princess Bosom")))
g.add((Princess_Bosom, hasDescription, Literal("An egg-shaped Artifact with patterns on its surface and a soft texture that squishes when pressure is applied.")))
g.add((Princess_Bosom, hasEffect, Literal("Squishy Material")))
g.add((Princess_Bosom, ownedBy, Orth))
g.add((Princess_Bosom, hasGrade, Third_Grade))
g.add((Princess_Bosom, sourcedFrom, Layer_1))

g.add((Rock_Top, RDF.type, MIA.Artifact))
g.add((Rock_Top, RDFS.label, Literal("Rock Top")))
g.add((Rock_Top, hasDescription, Literal("An Artifact found in the 1st Layer and mentioned by Nat.")))
g.add((Rock_Top, hasEffect, Literal("Floating and shape-shifting material")))
g.add((Rock_Top, sourcedFrom, Layer_1))

g.add((Star_Compass, RDF.type, MIA.Artifact))
g.add((Star_Compass, RDFS.label, Literal("Star Compass")))
g.add((Star_Compass, hasDescription, Literal("An Artifact found in the 1st Layer by Riko, who named it.")))
g.add((Star_Compass, hasEffect, Literal("Navigation")))
g.add((Star_Compass, ownedBy, Riko))
g.add((Star_Compass, hasGrade, Fourth_Grade))

g.add((Sun_Sphere, RDF.type, MIA.Artifact))
g.add((Sun_Sphere, RDFS.label, Literal("Sun Sphere")))
g.add((Sun_Sphere, hasDescription, Literal("An egg-shaped Artifact with a round structure in its centre and encasements covering its glass-like exterior.")))
g.add((Sun_Sphere, hasEffect, Literal("Light emission")))
g.add((Sun_Sphere, ownedBy, Ozen))
g.add((Sun_Sphere, hasGrade, Fourth_Grade))
g.add((Sun_Sphere, sourcedFrom, Layer_2))
g.add((Sun_Sphere, sourcedFrom, Layer_3))
g.add((Sun_Sphere, sourcedFrom, Layer_4))
g.add((Sun_Sphere, sourcedFrom, Layer_5))

g.add((Curse_Warding_Box, RDF.type, MIA.Artifact))
g.add((Curse_Warding_Box, RDFS.label, Literal("Curse-Warding Box")))
g.add((Curse_Warding_Box, hasDescription, Literal("A unique Artifact initially believed to nullify the effects of the Curse of the Abyss.")))
g.add((Curse_Warding_Box, hasEffect, Literal(" Those inside will still suffer the effects of the curse and possibly die as a result, but whatever is placed inside will come back to life seemingly unaffected and will immediately start crawling towards the center of the Abyss before dying again sometime later.")))
g.add((Curse_Warding_Box, ownedBy, Ozen))
g.add((Curse_Warding_Box, hasGrade, First_Grade))

g.add((Forgetter, RDF.type, MIA.Artifact))
g.add((Forgetter, RDFS.label, Literal("Forgetter")))
g.add((Forgetter, hasDescription, Literal("A rigid Second-Grade Artifact. A large number were found at the Joint Delving Site.")))
g.add((Forgetter, hasEffect, Literal("Storage unit")))
g.add((Forgetter, ownedBy, Orth))
g.add((Forgetter, hasGrade, Second_Grade))
g.add((Forgetter, sourcedFrom, Joint_Delving_Site))

g.add((Thousand_Men_Pins, RDF.type, MIA.Artifact))
g.add((Thousand_Men_Pins, RDFS.label, Literal("Thousand-Men Pins")))
g.add((Thousand_Men_Pins, hasDescription, Literal("Artifacts said to grant the user the strength of a thousand men.")))
g.add((Thousand_Men_Pins, hasEffect, Literal("Enhanced strength")))
g.add((Thousand_Men_Pins, ownedBy, Ozen))
g.add((Thousand_Men_Pins, hasGrade, First_Grade))

g.add((Gentle_Knock, RDF.type, MIA.Artifact))
g.add((Gentle_Knock, RDFS.label, Literal("Gentle Knock")))
g.add((Gentle_Knock, hasDescription, Literal("A manufactured multi-purpose tool made from Thinking Stones, which are excavated in the Great Fault.")))
g.add((Gentle_Knock, hasEffect, Literal("Multi-purpose tool")))
g.add((Gentle_Knock, ownedBy, Reg))
g.add((Gentle_Knock, hasGrade, Third_Grade))
g.add((Gentle_Knock, sourcedFrom, Layer_3))

g.add((Blaze_Reap, RDF.type, MIA.Artifact))
g.add((Blaze_Reap, RDFS.label, Literal("Blaze Reap")))
g.add((Blaze_Reap, hasDescription, Literal("An abnormally large pickaxe containing Everlasting Gunpowder.")))
g.add((Blaze_Reap, hasEffect, Literal("Injects an explosion into a struck object.")))
g.add((Blaze_Reap, ownedBy, Riko))
g.add((Blaze_Reap, hasGrade, First_Grade))

g.add((Fog_Weave, RDF.type, MIA.Artifact))
g.add((Fog_Weave, RDFS.label, Literal("Fog Weave")))
g.add((Fog_Weave, hasDescription, Literal("A very thin and lightweight piece of cloth that floats over the ground.")))
g.add((Fog_Weave, hasEffect, Literal("Lightweight fabric")))
g.add((Fog_Weave, ownedBy, Nanachi))
g.add((Fog_Weave, hasGrade, Third_Grade))

g.add((Unheard_Bell, RDF.type, MIA.Artifact))
g.add((Unheard_Bell, RDFS.label, Literal("Unheard Bell")))
g.add((Unheard_Bell, hasDescription, Literal("A large grey bell discovered in an inaccessible location in the 4th Layer.")))
g.add((Unheard_Bell, hasEffect, Literal("Time stop")))
g.add((Unheard_Bell, ownedBy, Orth))
g.add((Unheard_Bell, hasGrade, Special_Grade))
g.add((Unheard_Bell, sourcedFrom, Layer_4))

g.add((Altar_of_the_Absolute_Boundary_Relic, RDF.type, MIA.Artifact))
g.add((Altar_of_the_Absolute_Boundary_Relic, RDFS.label, Literal("Altar of the Absolute Boundary")))
g.add((Altar_of_the_Absolute_Boundary_Relic, hasDescription, Literal("An elevator-like connection between the 5th and 6th Layers and the principal method for White Whistles beginning their Last Dive.")))
g.add((Altar_of_the_Absolute_Boundary_Relic, hasEffect, Literal("Transport device")))
g.add((Altar_of_the_Absolute_Boundary_Relic, ownedBy, Ido_Front))
g.add((Altar_of_the_Absolute_Boundary_Relic, sourcedFrom, Layer_5))

g.add((Canopy_Unto_Dawn, RDF.type, MIA.Artifact))
g.add((Canopy_Unto_Dawn, RDFS.label, Literal("Canopy Unto Dawn")))
g.add((Canopy_Unto_Dawn, hasDescription, Literal("A custom-made set of armour for the Umbra Hands, made from several Artifacts and bio-fibres.")))
g.add((Canopy_Unto_Dawn, hasEffect, Literal("Armour set")))
g.add((Canopy_Unto_Dawn, ownedBy, Bondrewd))

g.add((Far_Caress, RDF.type, MIA.Artifact))
g.add((Far_Caress, RDFS.label, Literal("Far Caress")))
g.add((Far_Caress, hasDescription, Literal("One of Bondrewd's personal Artifacts.")))
g.add((Far_Caress, hasEffect, Literal("Manipulating tendrils")))
g.add((Far_Caress, ownedBy, Bondrewd))
g.add((Far_Caress, hasGrade, Second_Grade))

g.add((Gangway, RDF.type, MIA.Artifact))
g.add((Gangway, RDFS.label, Literal("Gangway")))
g.add((Gangway, hasDescription, Literal("One of Bondrewd's personal Artifacts.")))
g.add((Gangway, hasEffect, Literal("Light projection weapon")))
g.add((Gangway, ownedBy, Bondrewd))

g.add((Shaker, RDF.type, MIA.Artifact))
g.add((Shaker, RDFS.label, Literal("Shaker")))
g.add((Shaker, hasDescription, Literal("A personal Artifact of Bondrewd manufactured from Curse Steel.")))
g.add((Shaker, hasEffect, Literal("Curse infliction")))
g.add((Shaker, ownedBy, Bondrewd))

g.add((Sparagmos, RDF.type, MIA.Artifact))
g.add((Sparagmos, RDFS.label, Literal("Sparagmos")))
g.add((Sparagmos, hasDescription, Literal("One of Bondrewd's personal Artifacts.")))
g.add((Sparagmos, hasEffect, Literal("Destructive light weapon")))
g.add((Sparagmos, ownedBy, Bondrewd))

g.add((Third_Works, RDF.type, MIA.Artifact))
g.add((Third_Works, RDFS.label, Literal("Third Works")))
g.add((Third_Works, hasDescription, Literal("A psychokinetic arm resembling the skeletal forearm of a humanoid being.")))
g.add((Third_Works, hasEffect, Literal("Psychokinetic control")))
g.add((Third_Works, ownedBy, Bondrewd))
g.add((Third_Works, hasGrade, First_Grade))

g.add((Zoaholic, RDF.type, MIA.Artifact))
g.add((Zoaholic, RDFS.label, Literal("Zoaholic")))
g.add((Zoaholic, hasDescription, Literal("An Artifact that transfers the user's mind into other living beings and allows the connected bodies to share thoughts.")))
g.add((Zoaholic, hasEffect, Literal("Consciousness transference")))
g.add((Zoaholic, ownedBy, Bondrewd))
g.add((Zoaholic, hasGrade, Special_Grade))

# ===============================
# Humanoids Entities
# ===============================
g.add((Belchero, RDF.type, MIA.Human))
g.add((Belchero, RDFS.label, Literal("Belchero")))
g.add((Belchero, lastKnownLocation, Belchero_Orphanage))
g.add((Belchero, hasGender, Literal("Female")))
g.add((Belchero, hasSpecies, Literal("Human")))
g.add((Belchero, hasStatus, Literal("Alive")))
g.add((Belchero, hasOccupation, Literal("Director")))

g.add((Bellmore, RDF.type, MIA.Human))
g.add((Bellmore, RDFS.label, Literal("Bellmore")))
g.add((Bellmore, lastKnownLocation, The_Grand_Pier))
g.add((Bellmore, hasGender, Literal("Male")))
g.add((Bellmore, hasSpecies, Literal("Human")))
g.add((Bellmore, hasStatus, Literal("Alive")))
g.add((Bellmore, hasOccupation, Literal("Storyteller/Merchant")))

g.add((Bido, RDF.type, MIA.Human))
g.add((Bido, RDFS.label, Literal("Bido")))
g.add((Bido, lastKnownLocation, Ido_Front))
g.add((Bido, hasGender, Literal("Male")))
g.add((Bido, hasSpecies, Literal("Human")))
g.add((Bido, hasStatus, Literal("Deceased")))
g.add((Bido, hasOccupation, Literal("Umbra Hand")))
g.add((Bido, hasWhistleRank, BlackWhistle))

g.add((Bondrewd, RDF.type, MIA.Human))
g.add((Bondrewd, RDFS.label, Literal("Bondrewd")))
g.add((Bondrewd, lastKnownLocation, Ido_Front))
g.add((Bondrewd, hasGender, Literal("Male")))
g.add((Bondrewd, hasSpecies, Literal("Human")))
g.add((Bondrewd, hasStatus, Literal("Alive")))
g.add((Bondrewd, hasOccupation, Literal("Delver")))
g.add((Bondrewd, hasWhistleRank, WhiteWhistle))

g.add((Cravagli, RDF.type, MIA.Human))
g.add((Cravagli, RDFS.label, Literal("Cravagli")))
g.add((Cravagli, lastKnownLocation, Layer_6))
g.add((Cravagli, hasGender, Literal("Male")))
g.add((Cravagli, hasSpecies, Literal("Human")))
g.add((Cravagli, hasStatus, Literal("Deceased")))
g.add((Cravagli, hasOccupation, Literal("Delver")))
g.add((Cravagli, hasWhistleRank, BlackWhistle))

g.add((Gallice, RDF.type, MIA.Human))
g.add((Gallice, RDFS.label, Literal("Gallice")))
g.add((Gallice, lastKnownLocation, Ido_Front))
g.add((Gallice, hasGender, Literal("Male")))
g.add((Gallice, hasSpecies, Literal("Human")))
g.add((Gallice, hasStatus, Literal("Alive")))
g.add((Gallice, hasOccupation, Literal("Umbra Hand")))
g.add((Gallice, hasWhistleRank, BlackWhistle))

g.add((Gueira, RDF.type, MIA.Human))
g.add((Gueira, RDFS.label, Literal("Gueira")))
g.add((Gueira, lastKnownLocation, Ido_Front))
g.add((Gueira, hasGender, Literal("Male")))
g.add((Gueira, hasSpecies, Literal("Human")))
g.add((Gueira, hasStatus, Literal("Deceased")))
g.add((Gueira, hasOccupation, Literal("Umbra Hand")))
g.add((Gueira, hasWhistleRank, BlackWhistle))

g.add((Hablog, RDF.type, MIA.Human))
g.add((Hablog, RDFS.label, Literal("Hablog")))
g.add((Hablog, lastKnownLocation, Orth))
g.add((Hablog, hasGender, Literal("Male")))
g.add((Hablog, hasSpecies, Literal("Human")))
g.add((Hablog, hasStatus, Literal("Alive")))
g.add((Hablog, hasOccupation, Literal("Delver")))
g.add((Hablog, hasWhistleRank, BlackWhistle))

g.add((Irumyuui, RDF.type, MIA.Human))
g.add((Irumyuui, RDFS.label, Literal("Irumyuui")))
g.add((Irumyuui, lastKnownLocation, Iruburu))
g.add((Irumyuui, hasGender, Literal("Female")))
g.add((Irumyuui, hasSpecies, Literal("Human")))
g.add((Irumyuui, hasStatus, Literal("Deceased")))
g.add((Irumyuui, hasOccupation, Literal("Delver")))

g.add((Jiruo, RDF.type, MIA.Human))
g.add((Jiruo, RDFS.label, Literal("Jiruo")))
g.add((Jiruo, lastKnownLocation, Belchero_Orphanage))
g.add((Jiruo, hasGender, Literal("Male")))
g.add((Jiruo, hasSpecies, Literal("Human")))
g.add((Jiruo, hasStatus, Literal("Alive")))
g.add((Jiruo, hasOccupation, Literal("Instructor")))
g.add((Jiruo, hasWhistleRank, MoonWhistle))

g.add((Kiyui, RDF.type, MIA.Human))
g.add((Kiyui, RDFS.label, Literal("Kiyui")))
g.add((Kiyui, lastKnownLocation, Belchero_Orphanage))
g.add((Kiyui, hasGender, Literal("Male")))
g.add((Kiyui, hasSpecies, Literal("Human")))
g.add((Kiyui, hasStatus, Literal("Alive")))
g.add((Kiyui, hasOccupation, Literal("Delver Apprentice")))
g.add((Kiyui, hasWhistleRank, Bell))

g.add((Laffi, RDF.type, MIA.Human))
g.add((Laffi, RDFS.label, Literal("Laffi")))
g.add((Laffi, lastKnownLocation, Orth))
g.add((Laffi, hasGender, Literal("Female")))
g.add((Laffi, hasSpecies, Literal("Human")))
g.add((Laffi, hasStatus, Literal("Alive")))
g.add((Laffi, hasOccupation, Literal("Shopkeeper")))

g.add((Lyza, RDF.type, MIA.Human))
g.add((Lyza, RDFS.label, Literal("Lyza")))
g.add((Lyza, lastKnownLocation, Unknown_Location))
g.add((Lyza, hasGender, Literal("Female")))
g.add((Lyza, hasSpecies, Literal("Human")))
g.add((Lyza, hasStatus, Literal("Unknown")))
g.add((Lyza, hasOccupation, Literal("Delver")))
g.add((Lyza, hasWhistleRank, WhiteWhistle))

g.add((Marulk, RDF.type, MIA.Human))
g.add((Marulk, RDFS.label, Literal("Marulk")))
g.add((Marulk, lastKnownLocation, Seeker_Camp))
g.add((Marulk, hasGender, Literal("Male")))
g.add((Marulk, hasSpecies, Literal("Human")))
g.add((Marulk, hasStatus, Literal("Alive")))
g.add((Marulk, hasOccupation, Literal("Delver")))
g.add((Marulk, hasWhistleRank, BlueWhistle))

g.add((Mitty, RDF.type, MIA.Narehate))
g.add((Mitty, RDFS.label, Literal("Mitty")))
g.add((Mitty, lastKnownLocation, Nanachis_Hideout))
g.add((Mitty, hasGender, Literal("Female")))
g.add((Mitty, hasSpecies, Literal("Narehate")))
g.add((Mitty, hasStatus, Literal("Deceased")))
g.add((Mitty, hasOccupation, Literal("Companion")))

g.add((Nishagora, RDF.type, MIA.Human))
g.add((Nishagora, RDFS.label, Literal("Nishagora")))
g.add((Nishagora, lastKnownLocation, Layer_6))
g.add((Nishagora, hasGender, Literal("Female")))
g.add((Nishagora, hasSpecies, Literal("Human")))
g.add((Nishagora, hasStatus, Literal("Alive")))
g.add((Nishagora, hasOccupation, Literal("Delver")))
g.add((Nishagora, hasWhistleRank, BlackWhistle))

g.add((Nat, RDF.type, MIA.Human))
g.add((Nat, RDFS.label, Literal("Nat")))
g.add((Nat, lastKnownLocation, Belchero_Orphanage))
g.add((Nat, hasGender, Literal("Male")))
g.add((Nat, hasSpecies, Literal("Human")))
g.add((Nat, hasStatus, Literal("Alive")))
g.add((Nat, hasOccupation, Literal("Delver")))
g.add((Nat, hasWhistleRank, RedWhistle))

g.add((Nanachi, RDF.type, MIA.Narehate))
g.add((Nanachi, RDFS.label, Literal("Nanachi")))
g.add((Nanachi, lastKnownLocation, Layer_7))
g.add((Nanachi, hasGender, Literal("Unknown")))
g.add((Nanachi, hasSpecies, Literal("Narehate")))
g.add((Nanachi, hasStatus, Literal("Alive")))
g.add((Nanachi, hasOccupation, Literal("Delver")))

g.add((Neyozel, RDF.type, MIA.Narehate))
g.add((Neyozel, RDFS.label, Literal("Neyozel")))
g.add((Neyozel, lastKnownLocation, Layer_6))
g.add((Neyozel, hasGender, Literal("Male")))
g.add((Neyozel, hasSpecies, Literal("Narehate")))
g.add((Neyozel, hasStatus, Literal("Alive")))
g.add((Neyozel, hasOccupation, Literal("Delver")))
g.add((Neyozel, hasWhistleRank, BlackWhistle))

g.add((Ozen, RDF.type, MIA.Human))
g.add((Ozen, RDFS.label, Literal("Ozen")))
g.add((Ozen, lastKnownLocation, Seeker_Camp))
g.add((Ozen, hasGender, Literal("Female")))
g.add((Ozen, hasSpecies, Literal("Human")))
g.add((Ozen, hasStatus, Literal("Alive")))
g.add((Ozen, hasOccupation, Literal("Delver")))
g.add((Ozen, hasWhistleRank, WhiteWhistle))

g.add((Prushka, RDF.type, MIA.Human))
g.add((Prushka, RDFS.label, Literal("Prushka")))
g.add((Prushka, lastKnownLocation, Ido_Front))
g.add((Prushka, hasGender, Literal("Female")))
g.add((Prushka, hasSpecies, Literal("Human")))
g.add((Prushka, hasStatus, Literal("Deceased")))
g.add((Prushka, hasOccupation, Literal("Whistle")))

g.add((Reg, RDF.type, MIA.Living_Thing))
g.add((Reg, RDFS.label, Literal("Reg")))
g.add((Reg, lastKnownLocation, Layer_7))
g.add((Reg, hasGender, Literal("Male")))
g.add((Reg, hasSpecies, Literal("Unknown")))
g.add((Reg, hasStatus, Literal("Alive")))
g.add((Reg, hasOccupation, Literal("Delver")))
g.add((Reg, hasWhistleRank, RedWhistle))

g.add((Remayo, RDF.type, MIA.Human))
g.add((Remayo, RDFS.label, Literal("Remayo")))
g.add((Remayo, lastKnownLocation, Layer_6))
g.add((Remayo, hasGender, Literal("Female")))
g.add((Remayo, hasSpecies, Literal("Human")))
g.add((Remayo, hasStatus, Literal("Alive")))
g.add((Remayo, hasOccupation, Literal("Delver")))
g.add((Remayo, hasWhistleRank, BlackWhistle))

g.add((Riko, RDF.type, MIA.Human))
g.add((Riko, RDFS.label, Literal("Riko")))
g.add((Riko, lastKnownLocation, Layer_7))
g.add((Riko, hasGender, Literal("Female")))
g.add((Riko, hasSpecies, Literal("Human")))
g.add((Riko, hasStatus, Literal("Alive")))
g.add((Riko, hasOccupation, Literal("Delver")))
g.add((Riko, hasWhistleRank, WhiteWhistle))

g.add((Shiggy, RDF.type, MIA.Human))
g.add((Shiggy, RDFS.label, Literal("Shiggy")))
g.add((Shiggy, lastKnownLocation, Belchero_Orphanage))
g.add((Shiggy, hasGender, Literal("Male")))
g.add((Shiggy, hasSpecies, Literal("Human")))
g.add((Shiggy, hasStatus, Literal("Alive")))
g.add((Shiggy, hasOccupation, Literal("Delver")))
g.add((Shiggy, hasWhistleRank, RedWhistle))

g.add((Simred, RDF.type, MIA.Human))
g.add((Simred, RDFS.label, Literal("Simred")))
g.add((Simred, lastKnownLocation, Seeker_Camp))
g.add((Simred, hasGender, Literal("Male")))
g.add((Simred, hasSpecies, Literal("Human")))
g.add((Simred, hasStatus, Literal("Alive")))
g.add((Simred, hasOccupation, Literal("Delver")))
g.add((Simred, hasWhistleRank, BlackWhistle))

g.add((Srajo, RDF.type, MIA.Human))
g.add((Srajo, RDFS.label, Literal("Srajo")))
g.add((Srajo, lastKnownLocation, Layer_5))
g.add((Srajo, hasGender, Literal("Female")))
g.add((Srajo, hasSpecies, Literal("Human")))
g.add((Srajo, hasStatus, Literal("Alive")))
g.add((Srajo, hasOccupation, Literal("Delver")))
g.add((Srajo, hasWhistleRank, WhiteWhistle))

g.add((Torka, RDF.type, MIA.Human))
g.add((Torka, RDFS.label, Literal("Torka")))
g.add((Torka, lastKnownLocation, Layer_4))
g.add((Torka, hasGender, Literal("Male")))
g.add((Torka, hasSpecies, Literal("Human")))
g.add((Torka, hasStatus, Literal("Deceased")))
g.add((Torka, hasOccupation, Literal("Delver")))
g.add((Torka, hasWhistleRank, BlackWhistle))

g.add((Wakuna, RDF.type, MIA.Human))
g.add((Wakuna, RDFS.label, Literal("Wakuna")))
g.add((Wakuna, lastKnownLocation, Layer_6))
g.add((Wakuna, hasGender, Literal("Unknown")))
g.add((Wakuna, hasSpecies, Literal("Human")))
g.add((Wakuna, hasStatus, Literal("Unknown")))
g.add((Wakuna, hasOccupation, Literal("Delver")))
g.add((Wakuna, hasWhistleRank, WhiteWhistle))

g.add((Yataramar, RDF.type, MIA.Narehate))
g.add((Yataramar, RDFS.label, Literal("Yataramar")))
g.add((Yataramar, lastKnownLocation, Layer_6))
g.add((Yataramar, hasGender, Literal("Male")))
g.add((Yataramar, hasSpecies, Literal("Narehate")))
g.add((Yataramar, hasStatus, Literal("Alive")))
g.add((Yataramar, hasOccupation, Literal("Delver")))
g.add((Yataramar, hasWhistleRank, BlackWhistle))

g.add((Yelme, RDF.type, MIA.Human))
g.add((Yelme, RDFS.label, Literal("Yelme")))
g.add((Yelme, lastKnownLocation, Seeker_Camp))
g.add((Yelme, hasGender, Literal("Male")))
g.add((Yelme, hasSpecies, Literal("Human")))
g.add((Yelme, hasStatus, Literal("Alive")))
g.add((Yelme, hasOccupation, Literal("Delver")))
g.add((Yelme, hasWhistleRank, MoonWhistle))

g.add((Zapo, RDF.type, MIA.Human))
g.add((Zapo, RDFS.label, Literal("Zapo")))
g.add((Zapo, lastKnownLocation, Seeker_Camp))
g.add((Zapo, hasGender, Literal("Male")))
g.add((Zapo, hasSpecies, Literal("Human")))
g.add((Zapo, hasStatus, Literal("Alive")))
g.add((Zapo, hasOccupation, Literal("Delver")))
g.add((Zapo, hasWhistleRank, MoonWhistle))

# ===============================
# Bestiary Entities
# ===============================

g.add((Amakagame, RDF.type, MIA.Beast))
g.add((Amakagame, RDFS.label, Literal("Amakagame")))
g.add((Amakagame, hasSpecies, Literal("Unknown")))
g.add((Amakagame, livesIn, Layer_3))
g.add((Amakagame, hasDangerLevel, Serious_Danger))
g.add((Amakagame, hasDescription, Literal("Amakagame (甘花瓶アマカガメ, lit. Sweet-Smelling Vase) are bulbous creatures that live in the cave systems of the 3rd Layer.")))

g.add((Amaranthine_Deceptor, RDF.type, MIA.Beast))
g.add((Amaranthine_Deceptor, RDFS.label, Literal("Amaranthine-Deceptor")))
g.add((Amaranthine_Deceptor, hasSpecies, Literal("Insect")))
g.add((Amaranthine_Deceptor, livesIn, Layer_4))
g.add((Amaranthine_Deceptor, hasDangerLevel, Absurd_Danger))
g.add((Amaranthine_Deceptor, hasDescription, Literal("The Amaranthine-Deceptor (クオンガタリ, Kuongatari) are insects native to the impenetrable 6th Layer of The Abyss, where return becomes impossible for humans.")))

g.add((Crimson_Splitjaw, RDF.type, MIA.Beast))
g.add((Crimson_Splitjaw, RDFS.label, Literal("Crimson Splitjaw")))
g.add((Crimson_Splitjaw, hasSpecies, Literal("Reptile")))
g.add((Crimson_Splitjaw, livesIn, Layer_3))
g.add((Crimson_Splitjaw, hasDangerLevel, Deadly_Danger))
g.add((Crimson_Splitjaw, hasDescription, Literal("The Crimson Splitjaw (ベニクチナワ, Benikuchinawa) is a giant scarlet red reptile with a serpentine body that primarily lives in the steep cliffs of the 3rd Layer of The Abyss")))

g.add((Corpse_Weeper, RDF.type, MIA.Beast))
g.add((Corpse_Weeper, RDFS.label, Literal("Corpse-Weeper")))
g.add((Corpse_Weeper, hasSpecies, Literal("Bird")))
g.add((Corpse_Weeper, livesIn, Layer_2))
g.add((Corpse_Weeper, hasDangerLevel, Serious_Danger))
g.add((Corpse_Weeper, hasDescription, Literal("Corpse-Weepers (ナキカバネ, Nakikabane) are large birds that live in the ruthless 2nd Layer of The Abyss, in the Forest of Temptation. Corpse-Weepers are carnivorous and quite violent at that. They are notorious for their capability to mimic sounds and use it for hunting.")))

g.add((Demonfish, RDF.type, MIA.Beast))
g.add((Demonfish, RDFS.label, Literal("Demonfish")))
g.add((Demonfish, hasSpecies, Literal("Fish")))
g.add((Demonfish, livesIn, Layer_1))
g.add((Demonfish, livesIn, Layer_2))
g.add((Demonfish, livesIn, Layer_3))
g.add((Demonfish, livesIn, Layer_4))
g.add((Demonfish, hasDangerLevel, Unknown_Danger))
g.add((Demonfish, hasDescription, Literal("Demonfish (ガンキマス, Gankimasu) are fish that can be found in abundance in the 1st through 4th layers of The Abyss.")))

g.add((Hamashirama, RDF.type, MIA.Beast))
g.add((Hamashirama, RDFS.label, Literal("Hamashirama")))
g.add((Hamashirama, hasSpecies, Literal("Fish")))
g.add((Hamashirama, livesIn, Layer_5))
g.add((Hamashirama, hasDangerLevel, Insignificant_Danger))
g.add((Hamashirama, hasDescription, Literal("The Hamashirama (ハマシラマ) is a strange fish that lives in large numbers in the 5th Layer of The Abyss, the Sea of Corpses. It's one of the creatures documented in Lyza's Notes.")))

g.add((Hammerbeak, RDF.type, MIA.Beast))
g.add((Hammerbeak, RDFS.label, Literal("Hammerbeak")))
g.add((Hammerbeak, hasSpecies, Literal("Bird")))
g.add((Hammerbeak, livesIn, Layer_1))
g.add((Hammerbeak, livesIn, Layer_2))
g.add((Hammerbeak, livesIn, Layer_3))
g.add((Hammerbeak, livesIn, Layer_4))
g.add((Hammerbeak, hasDangerLevel, Insignificant_Danger))
g.add((Hammerbeak, hasDescription, Literal("The Hammerbeak (ツチバシ, Tsuchibashi) is an avian species whose habitat extends from the surface down to the 4th Layer of The Abyss.")))

g.add((Inbyo, RDF.type, MIA.Beast))
g.add((Inbyo, RDFS.label, Literal("Inbyo")))
g.add((Inbyo, hasSpecies, Literal("Mammal")))
g.add((Inbyo, livesIn, The_Inverted_Forest))
g.add((Inbyo, hasDangerLevel, Caution_Danger))
g.add((Inbyo, hasDescription, Literal("Inbyos (インビョウ, Inbyō) are gibbon-like primates inhabiting the Inverted Forest")))

g.add((Kazura_Squid, RDF.type, MIA.Beast))
g.add((Kazura_Squid, RDFS.label, Literal("Kazura Squid")))
g.add((Kazura_Squid, hasSpecies, Literal("Cephalopod")))
g.add((Kazura_Squid, livesIn, Layer_3))
g.add((Kazura_Squid, livesIn, Layer_4))
g.add((Kazura_Squid, hasDangerLevel, Unknown_Danger))
g.add((Kazura_Squid, hasDescription, Literal("The Kazura Squid (カズライカ, Kazuraika) is a species seen inhabiting the 3rd and 4th layers of The Abyss.")))

g.add((Madokajack, RDF.type, MIA.Beast))
g.add((Madokajack, RDFS.label, Literal("Madokajack")))
g.add((Madokajack, hasSpecies, Literal("Reptile")))
g.add((Madokajack, livesIn, Layer_3))
g.add((Madokajack, hasDangerLevel, Deadly_Danger))
g.add((Madokajack, hasDescription, Literal("Madokajacks (マドカジャク, Madokajaku) are large reptilian creatures that live in the 3rd Layer.")))

g.add((Meinastilim, RDF.type, MIA.Beast))
g.add((Meinastilim, RDFS.label, Literal("Meinastilim")))
g.add((Meinastilim, hasSpecies, Literal("Mammal")))
g.add((Meinastilim, hasDangerLevel, Unknown_Danger))
g.add((Meinastilim, hasDescription, Literal("Meinastilim (メイナストイリム, Meinasutoirimu), also called a 'Child of Change' (変化へんかの子こ, Henka no Ko), are a species found in The Abyss. Not much is known about the species as a whole, due to there being only one known specimen, Meinya.")))

g.add((Neritantan, RDF.type, MIA.Beast))
g.add((Neritantan, RDFS.label, Literal("Neritantan")))
g.add((Neritantan, hasSpecies, Literal("Mammal")))
g.add((Neritantan, livesIn, Layer_3))
g.add((Neritantan, hasDangerLevel, Harmless_Danger))
g.add((Neritantan, hasDescription, Literal("The Neritantan (ネリタンタン) is a species that inhabits the vast cave system within the walls of the 3rd Layer of The Abyss and live in the roots of the plants that grow haphazardly within it.")))

g.add((Orb_Piercer, RDF.type, MIA.Beast))
g.add((Orb_Piercer, RDFS.label, Literal("Orb Piercer")))
g.add((Orb_Piercer, hasSpecies, Literal("Mammal")))
g.add((Orb_Piercer, livesIn, Layer_4))
g.add((Orb_Piercer, hasDangerLevel, Absurd_Danger))
g.add((Orb_Piercer, hasDescription, Literal("Orb Piercers (タマウガチ, Tamaugachi) are dangerous creatures inhabiting the 4th Layer of The Abyss. They are covered with long, sharpened and venomous spines that can pierce through metal, as if was paper. ")))

g.add((Ottobas, RDF.type, MIA.Beast))
g.add((Ottobas, RDFS.label, Literal("Ottobas")))
g.add((Ottobas, hasSpecies, Literal("Mammal")))
g.add((Ottobas, livesIn, Layer_2))
g.add((Ottobas, hasDangerLevel, Serious_Danger))
g.add((Ottobas, hasDescription, Literal("The Ottobas (オットバス, Ottobasu) are large amphibious animals that live deep within the bottom of the 2nd Layer of The Abyss, in the area around the borders of the Inverted Forest.")))

g.add((Rohana, RDF.type, MIA.Beast))
g.add((Rohana, RDFS.label, Literal("Rohana")))
g.add((Rohana, hasSpecies, Literal("Insect")))
g.add((Rohana, livesIn, Layer_2))
g.add((Rohana, hasDangerLevel, Unknown_Danger))
g.add((Rohana, hasDescription, Literal("Rohana (ロオハナ, Rōhana), or Waxwing, are a species of aquatic insect found in the 2nd Layer.")))

g.add((Shroombear, RDF.type, MIA.Beast))
g.add((Shroombear, RDFS.label, Literal("Shroombear")))
g.add((Shroombear, hasSpecies, Literal("Mammal")))
g.add((Shroombear, livesIn, Layer_4))
g.add((Shroombear, hasDangerLevel, Harmless_Danger))
g.add((Shroombear, hasDescription, Literal("Shroombears (タケグマ, Takeguma) are creatures which can be found at the 4th Layer of The Abyss. Their danger classification is unknown, but they seem to lack offensive capabilities and appear to be docile")))

g.add((Silkfang, RDF.type, MIA.Beast))
g.add((Silkfang, RDFS.label, Literal("Silkfang")))
g.add((Silkfang, hasSpecies, Literal("Insect")))
g.add((Silkfang, livesIn, Layer_1))
g.add((Silkfang, hasDangerLevel, Caution_Danger))
g.add((Silkfang, hasDescription, Literal("The Silkfang (ゴコウゲ, Gokōge) is a large insect that is occasionally seen within the 1st Layer of The Abyss.")))

g.add((Stingerhead, RDF.type, MIA.Beast))
g.add((Stingerhead, RDFS.label, Literal("Stingerhead")))
g.add((Stingerhead, hasSpecies, Literal("Arthropod")))
g.add((Stingerhead, livesIn, Layer_5))
g.add((Stingerhead, hasDangerLevel, Extraordinary_Danger))
g.add((Stingerhead, hasDescription, Literal("Stingerheads (カッショウガシラ, Kasshōgashira) are dangerous creatures that live in the sandstone area in the 5th Layer of The Abyss, first officially documented by the White Whistle Delver Lyza 'The Annihilator' and named by her")))

# ===============================
# Overworld Based Entities
# ===============================
g.add((World, RDF.type, MIA.Entity))
g.add((World, hasDescription, Literal("The complete world of Made in Abyss")))
g.add((Sereny, RDF.type, MIA.Place))
g.add((Sereny, hasDescription, Literal("Sereny (セレニの地ち, Sereni no Chi) is a country outside of Orth. It is the most powerful nation of the world's northern territories and has a cold, snowy climate.")))
g.add((Jisweku, RDF.type, MIA.Place))
g.add((Jisweku, hasDescription, Literal("Jisweku (ジスェクー, Jisuekū) is a remote western country outside of Orth")))
g.add((Beoluska, RDF.type, MIA.Place))
g.add((Beoluska, hasDescription, Literal("Beoluska (ベオルスカ, Beorusuka) is an archipelago country encompassing the entirety of Orth, which refers to some isolated islands and towns that encompass The Abyss, plus other islands and territories.")))

g.add((Orth, RDF.type, MIA.Place))
g.add((Orth, hasDescription, Literal("Orth (オース, Ōsu), also known as the City of the Giant Pit (大穴おおあなの街まち, Ōana no Machi), is a large town on the edge of The Abyss, formed as a result of the many explorers traveling to the island located in the southern sea of Beoluska.")))
g.add((North_Orth, RDF.type, MIA.District))
g.add((South_Orth, RDF.type, MIA.District))
g.add((East_Orth, RDF.type, MIA.District))
g.add((West_Orth, RDF.type, MIA.District))
g.add((Central_Orth, RDF.type, MIA.District))

g.add((Orth_Windmills, RDF.type, MIA.Location))
g.add((Gate_to_the_Netherworld, RDF.type, MIA.Location))
g.add((Gate_to_the_Netherworld, hasDescription, Literal("The Gate to the Netherworld (奈落ならく門もん, Narakumon) is a stone archway, overgrown with flora. It appears to be one of the primary entrances for Delvers entering The Abyss down into the 1st Layer.")))
g.add((The_Wharf, RDF.type, MIA.Location))
g.add((The_Wharf, hasDescription, Literal("The Wharf (岸壁街がんぺきがい, Ganpekigai) is a section of the South District of Orth")))
g.add((The_Grand_Pier, RDF.type, MIA.Location))
g.add((The_Grand_Pier, hasDescription, Literal("The Grand Pier (大桟橋おおさんばし, Ōsanbashi) is an ornate gondola station located in the lowest area of the West District. It is used for triumphant returns of Delver teams.")))
g.add((Belchero_Orphanage, RDF.type, MIA.Location))
g.add((Belchero_Orphanage, hasDescription, Literal("Belchero Orphanage (ベルチェロ孤児院こじいん, Beruchero Kojiin) is an orphanage in Orth run by Belchero, who is sometimes assisted by Jiruo. It is completed with a school, where the children there learn to be Delvers.")))
g.add((Delver_Guild_HQ, RDF.type, MIA.Location))
g.add((Delver_Guild_HQ, hasDescription, Literal("The Delver Guild HQ (探窟たんくつ組合くみあい本部ほんぶ, Tankutsu Kumiai Honbu) is the headquarters of the organization in charge of regulating delving processes, as well as managing the Delvers and giving them ranks according to their achievements.")))

# The Abyss Locations
g.add((The_Abyss, RDF.type, MIA.Place)) 
g.add((The_Abyss, hasDepth, Literal("0 - Unknown meters")))
g.add((The_Abyss, minDepth, Literal(0, datatype=XSD.integer)))
g.add((The_Abyss, hasDescription, Literal("The Abyss (奈落アビス, Netherworld) is a colossal pit discovered 1,900 years ago around the islands of the southern ocean of Beoluska; a vertical hole with an opening diameter of around 1,000 meters and speculated to be over 20,000 meters deep.")))

# ===============================
# Layer 1 Entities
# ===============================
g.add((Layer_1, RDF.type, MIA.Place)) 
g.add((Layer_1, hasDepth, Literal("0 - 1350 meters")))
g.add((Layer_1, minDepth, Literal(0, datatype=XSD.integer)))
g.add((Layer_1, maxDepth, Literal(1350, datatype=XSD.integer)))
g.add((Layer_1, hasDescription, Literal("The 1st Layer is the most shallow section of The Abyss, right below the town of Orth. The environment is consistent and sunny, full of hollows in the grassy rock faces and petrified trees. The wildlife consists of fantastical and mostly harmless animals. Scattered and hidden all across the 1st Layer are Praying Skeletons.")))
g.add((Layer_1, hasEffect, Literal("Strains of Ascent: Light dizziness and nausea.")))
g.add((Layer_1, hasWhistleRequirement, RedWhistle))

# Locations
g.add((Abode_of_Trees_and_Fossils, RDF.type, MIA.Location))
g.add((Abode_of_Trees_and_Fossils, hasDepth, Literal(200, datatype=XSD.integer)))
g.add((Big_Gondola, RDF.type, MIA.Location))
g.add((Big_Gondola, hasDepth, Literal(55, datatype=XSD.integer)))
g.add((Burial_Tower, RDF.type, MIA.Location))
g.add((Burial_Tower, hasDepth, Literal(300, datatype=XSD.integer)))
g.add((Gate_to_the_Netherworld, RDF.type, MIA.Location))
g.add((Gate_to_the_Netherworld, hasDepth, Literal(50, datatype=XSD.integer)))
g.add((The_Guiding_Tree, RDF.type, MIA.Location))
g.add((Ominaki_Falls, RDF.type, MIA.Location))
g.add((Seat_of_the_Waterfall, RDF.type, MIA.Location))
g.add((Stargazing_Hill, RDF.type, MIA.Location))
g.add((Stone_Ark, RDF.type, MIA.Location))
g.add((Stone_Ark, hasDepth, Literal(600, datatype=XSD.integer)))
g.add((Twisting_Crag, RDF.type, MIA.Location))
g.add((Wind_Riding_Windmills, RDF.type, MIA.Location))
g.add((Wind_Riding_Windmills, hasDepth, Literal(1000, datatype=XSD.integer)))
g.add((Wuthering, RDF.type, MIA.Location))

# ===============================
# Layer 2 Entities
# ===============================
g.add((Layer_2, RDF.type, MIA.Place)) 
g.add((Layer_2, hasDepth, Literal("1,350 - 2,600 meters.")))
g.add((Layer_2, minDepth, Literal(1350, datatype=XSD.integer)))
g.add((Layer_2, maxDepth, Literal(2600, datatype=XSD.integer)))
g.add((Layer_2, hasDescription, Literal("The Forest of Temptation is the first truly dangerous section of The Abyss. The fauna and environment suddenly change, shifting into a forest with large vegetation. The creatures that inhabit this layer are much more dangerous. Deeper in, there is an area known as the 'Inverted Forest', where the trees grow upside-down and the updraft wind blows hard, with even water flows upward. An outpost known as Seeker Camp has been established here to serve as a resting point for Delvers.")))
g.add((Layer_2, hasEffect, Literal("Strains of Ascent: Intense nausea, headaches, and numbness of limbs.")))
g.add((Layer_2, hasWhistleRequirement, BlueWhistle))

# Layer 2 locations
g.add((Heavens_Waterfall, RDF.type, MIA.Location))
g.add((Heavens_Waterfall, hasDepth, Literal(2600, datatype=XSD.integer)))
g.add((Rohana_Fountainhead, RDF.type, MIA.Location))
g.add((Rohana_Fountainhead, hasDepth, Literal(2550, datatype=XSD.integer)))
g.add((Sky_Jellyfish, RDF.type, MIA.Location))
g.add((Sleeping_Bed_of_Mushrooms, RDF.type, MIA.Location))

# Sub place of layer 2
g.add((The_Inverted_Forest, RDF.type, MIA.Place))
g.add((The_Inverted_Forest, hasDescription, Literal("Deeper in this layer, there is an area known as the 'Inverted Forest.' This is an area where updrafts and wind currents coming from the Abyss are so strong that the environment effectively flips, creating a forest of upside-down platforms that Delvers have to jump across—even water flows upwards.")))
g.add((The_Inverted_Forest, hasDepth, Literal(1700, datatype=XSD.integer)))
g.add((Hells_Crossing, RDF.type, MIA.Location))
g.add((Hells_Crossing, hasDepth, Literal(2000, datatype=XSD.integer)))
g.add((Joint_Delving_Site, RDF.type, MIA.Location))
g.add((Seeker_Camp, RDF.type, MIA.Location))
g.add((Seeker_Camp, hasDepth, Literal(2540, datatype=XSD.integer)))
g.add((Sky_Hunting_Grounds, RDF.type, MIA.Location))


# ===============================
# Layer 3 Entities
# ===============================
g.add((Layer_3, RDF.type, MIA.Place)) 
g.add((Layer_3, hasDepth, Literal("2,600 - 7,000 meters.")))
g.add((Layer_3, minDepth, Literal(2600, datatype=XSD.integer)))
g.add((Layer_3, maxDepth, Literal(7000, datatype=XSD.integer)))
g.add((Layer_3, hasDescription, Literal("The Great Fault (大断層だいだんそう, Dai-dansō) is The Abyss' third layer (深界しんかい三層さんそう, Shinkai San-sō). A narrow, 4-kilometer-deep gorge surrounded by countless interlocking caverns and with creatures, both harmless and deadly, lurking inside.")))
g.add((Layer_3, hasEffect, Literal("Strains of Ascent: In addition to aforementioned effects, vertigo combined with visual and auditory hallucinations.")))
g.add((Layer_3, hasWhistleRequirement, MoonWhistle))

# Layer 3 locations
g.add((Baracocha_Corridors, RDF.type, MIA.Location))
g.add((Baracocha_Corridors, hasDepth, Literal(3300, datatype=XSD.integer)))
g.add((Cumulonimbus_Point, RDF.type, MIA.Location))
g.add((Ghostly_Roots, RDF.type, MIA.Location))
g.add((Greenery_Layer, RDF.type, MIA.Location))
g.add((The_Imprisoned_Pirate_Ship, RDF.type, MIA.Location))
g.add((The_Imprisoned_Pirate_Ship, hasDepth, Literal(3000, datatype=XSD.integer)))
g.add((Rumbling_Grounds_of_the_Strong, RDF.type, MIA.Location))
g.add((Tallowstone_Layer, RDF.type, MIA.Location))

# ===============================
# Layer 4 Entities
# ===============================
g.add((Layer_4, RDF.type, MIA.Place))
g.add((Layer_4, hasDepth, Literal("7,000 - 12,000 meters")))
g.add((Layer_4, minDepth, Literal(7000, datatype=XSD.integer)))
g.add((Layer_4, maxDepth, Literal(12000, datatype=XSD.integer)))
g.add((Layer_4, hasDescription, Literal("The Goblets of Giants (巨人きょじんの盃さかずき, Kyojin no Sakazuki) is The Abyss' fourth layer (深界しんかい四層よんそう, Shinkai Yon-sō). It is a sprawling jungle of unique, awe-inspiring, and deadly fauna. This layer is characterized by a deceptive fusion of beauty and danger")))
g.add((Layer_4, hasEffect, Literal("Strains of Ascent: Intense pain throughout the body and bleeding from every orifice.")))
g.add((Layer_4, hasWhistleRequirement, BlackWhistle))

# Layer 4 locations
g.add((Acid_Waterfall, RDF.type, MIA.Location))
g.add((Dead_Crystal_Cave, RDF.type, MIA.Location))
g.add((Eternal_Wave_Crests, RDF.type, MIA.Location))
g.add((Flat_Creeper_Spike_Stretch, RDF.type, MIA.Location))
g.add((Flat_Creeper_Spike_Stretch, hasDepth, Literal(7100, datatype=XSD.integer)))
g.add((Forest_of_Crooked_Stone_Columns, RDF.type, MIA.Location))
g.add((Gas_Plume_Deposit, RDF.type, MIA.Location))
g.add((Flat_Creeper_Squid_Spawning_Grounds, RDF.type, MIA.Location))
g.add((Flat_Creeper_Squid_Spawning_Grounds, hasDepth, Literal(6750, datatype=XSD.integer)))
g.add((Garden_of_the_Flowers_of_Fortitude, RDF.type, MIA.Location))
g.add((Garden_of_the_Flowers_of_Fortitude, hasDepth, Literal(9000, datatype=XSD.integer)))
g.add((Nanachis_Hideout, RDF.type, MIA.Location))
g.add((Nanachis_Hideout, hasDepth, Literal(7100, datatype=XSD.integer)))
g.add((Old_Beasts_Hidden_Hot_Spring, RDF.type, MIA.Location))
g.add((Old_Beasts_Hidden_Hot_Spring, hasDepth, Literal(7100, datatype=XSD.integer)))
g.add((Spiral_Ice_Pillars, RDF.type, MIA.Location))
g.add((Steel_Fossil_Assemblage, RDF.type, MIA.Location))
g.add((Sticky_Clouds, RDF.type, MIA.Location))

# ===============================
# Layer 5 Entities
# ===============================
g.add((Layer_5, RDF.type, MIA.Place))
g.add((Layer_5, hasDepth, Literal("12,000 - 13,000 meters.")))
g.add((Layer_5, minDepth, Literal(12000, datatype=XSD.integer)))
g.add((Layer_5, maxDepth, Literal(13000, datatype=XSD.integer)))
g.add((Layer_5, hasDescription, Literal("The Sea of Corpses (なきがらの海うみ, Nakigara no Umi) is The Abyss' fifth layer (深界しんかい五ご層そう, Shinkai Go-sō). It consists of a vast frozen wasteland encircling a massive sea.[1] It is also the last layer that it is physically possible for Delvers to return to the surface without loss of humanity or dying")))
g.add((Layer_5, hasEffect, Literal("Strains of Ascent: Complete sensory deprivation, confusion and self-harming behavior.")))
g.add((Layer_5, hasWhistleRequirement, WhiteWhistle))

# Layer 5 locations
g.add((Crystallized_Water_Supports, RDF.type, MIA.Location))
g.add((Crystallized_Water_Supports, hasDepth, Literal(12300, datatype=XSD.integer)))
g.add((Frost_Dragonbones, RDF.type, MIA.Location))
g.add((Sandstone_Region, RDF.type, MIA.Location))
g.add((Sandstone_Region, hasDepth, Literal(12800, datatype=XSD.integer)))

# Sub Place of Layer 5
g.add((Ido_Front, RDF.type, MIA.Place))
g.add((Ido_Front, hasDepth, Literal(13000, datatype=XSD.integer)))
g.add((Altar_of_the_Absolute_Boundary, RDF.type, MIA.Location))
g.add((Altar_of_the_Absolute_Boundary, hasDepth, Literal(13000, datatype=XSD.integer)))


# ===============================
# Layer 6 Entities
# ===============================
g.add((Layer_6, RDF.type, MIA.Place)) 
g.add((Layer_6, hasDepth, Literal("13,000 - 15,500 meters")))
g.add((Layer_6, minDepth, Literal(13000, datatype=XSD.integer)))
g.add((Layer_6, maxDepth, Literal(15500, datatype=XSD.integer)))
g.add((Layer_6, hasDescription, Literal("A White Whistle's 'Last Dive'. A human who tries to ascend from the 6th Layer either succumbs to death, or is deformed beyond recognition, hence the name, 'The Capital of the Unreturned.' In Orth, there is a rumor about a Golden City at the bottom of The Abyss, which supposedly originated from the 6th Layer, where the ruins of a majestic city sleep undisturbed. The buildings spread in every direction and are covered in crystal.It is not uncommon to come across creatures of an irrational danger level here and there even occur geo-thermal explosions that emit poisonous gas and iron rain.Avian species in this layer are unaffected by the bird repellent used on the Mail Balloons that delvers send back up to the surface. In a secluded area of the 6th Layer, an entire village inhabited by Narehate called Iruburu was formed.")))
g.add((Layer_6, hasEffect, Literal("Strains of Ascent: Loss of humanity or death, or under specific conditions, the Blessing.")))

g.add((Iruburu, RDF.type, MIA.Place)) 
# ===============================
# Layer 7 Entities
# ===============================
g.add((Layer_7, RDF.type, MIA.Place)) 
g.add((Layer_7, hasDepth, Literal("15,500 -????? meters.")))
g.add((Layer_7, minDepth, Literal(15500, datatype=XSD.integer)))
g.add((Layer_7, hasDescription, Literal("The final known layer of The Abyss. Not much is known about it, but there are many rumors about it transmitted from the Last Dives of generations of White Whistle Delvers, which are only passed down via word of mouth to none but themselves. These include the claim that there exists in it something shaped like a ring, Ring of the Essence, which only a few White Whistle Delvers have seen, as well as the rumor that along the path to the bottom of The Abyss live mysterious beings called 'Gatekeepers.' It was at the entrance of this layer that Lyza documented the Human-like Silhouette, an unknown entity resembling Reg.")))
g.add((Layer_7, hasEffect, Literal("Unknown")))

# ===============================
# Label Entities
# ===============================
g.add((World, RDFS.label, Literal("World")))
g.add((Sereny, RDFS.label, Literal("Sereny")))
g.add((Jisweku, RDFS.label, Literal("Jisweku")))
g.add((Beoluska, RDFS.label, Literal("Beoluska")))
g.add((Orth, RDFS.label, Literal("Orth")))
g.add((North_Orth, RDFS.label, Literal("North District")))
g.add((South_Orth, RDFS.label, Literal("South District")))
g.add((East_Orth, RDFS.label, Literal("East District")))
g.add((West_Orth, RDFS.label, Literal("West District")))
g.add((Central_Orth, RDFS.label, Literal("Central District")))
g.add((Orth_Windmills, RDFS.label, Literal("Orth Windmills")))
g.add((Gate_to_the_Netherworld, RDFS.label, Literal("Gate to the Netherworld")))
g.add((The_Wharf, RDFS.label, Literal("The Wharf")))
g.add((The_Grand_Pier, RDFS.label, Literal("The Grand Pier")))
g.add((Belchero_Orphanage, RDFS.label, Literal("Belchero Orphanage")))
g.add((Delver_Guild_HQ, RDFS.label, Literal("Delver Guild HQ")))
g.add((The_Abyss, RDFS.label, Literal("The Abyss")))
g.add((Layer_1, RDFS.label, Literal("1st Layer")))
g.add((Layer_2, RDFS.label, Literal("2nd Layer")))
g.add((Layer_3, RDFS.label, Literal("3rd Layer")))
g.add((Layer_4, RDFS.label, Literal("4th Layer")))
g.add((Layer_5, RDFS.label, Literal("5th Layer")))
g.add((Layer_6, RDFS.label, Literal("6th Layer")))
g.add((Layer_7, RDFS.label, Literal("7th Layer")))
g.add((Iruburu, RDFS.label, Literal("Iruburu")))

g.add((Abode_of_Trees_and_Fossils, RDFS.label, Literal("Abode of Trees and Fossils")))
g.add((Big_Gondola, RDFS.label, Literal("Big Gondola")))
g.add((Burial_Tower, RDFS.label, Literal("Burial Tower")))
g.add((The_Guiding_Tree, RDFS.label, Literal("The Guiding Tree")))
g.add((Ominaki_Falls, RDFS.label, Literal("Ominaki Falls")))
g.add((Seat_of_the_Waterfall, RDFS.label, Literal("Seat of the Waterfall")))
g.add((Stargazing_Hill, RDFS.label, Literal("Stargazing Hill")))
g.add((Stone_Ark, RDFS.label, Literal("Stone Ark")))
g.add((Twisting_Crag, RDFS.label, Literal("Twisting Crag")))
g.add((Wind_Riding_Windmills, RDFS.label, Literal("Wind-Riding Windmills")))
g.add((Wuthering, RDFS.label, Literal("Wuthering")))

g.add((Heavens_Waterfall, RDFS.label, Literal("Heaven's Waterfall")))
g.add((Rohana_Fountainhead, RDFS.label, Literal("Rohana Fountainhead")))
g.add((Sky_Jellyfish, RDFS.label, Literal("Sky Jellyfish")))
g.add((Sleeping_Bed_of_Mushrooms, RDFS.label, Literal("Sleeping Bed of Mushrooms")))
g.add((The_Inverted_Forest, RDFS.label, Literal("The Inverted Forest")))
g.add((Hells_Crossing, RDFS.label, Literal("Hell's Crossing")))
g.add((Joint_Delving_Site, RDFS.label, Literal("Joint Delving Site")))
g.add((Seeker_Camp, RDFS.label, Literal("Seeker Camp")))
g.add((Sky_Hunting_Grounds, RDFS.label, Literal("Sky Hunting Grounds")))

g.add((Baracocha_Corridors, RDFS.label, Literal("Baracocha Corridors")))
g.add((Cumulonimbus_Point, RDFS.label, Literal("Cumulonimbus Point")))
g.add((Ghostly_Roots, RDFS.label, Literal("Ghostly Roots")))
g.add((Greenery_Layer, RDFS.label, Literal("Greenery Layer")))
g.add((The_Imprisoned_Pirate_Ship, RDFS.label, Literal("The Imprisoned Pirate Ship")))
g.add((Rumbling_Grounds_of_the_Strong, RDFS.label, Literal("Rumbling Grounds of the Strong")))
g.add((Tallowstone_Layer, RDFS.label, Literal("Tallowstone Layer")))

g.add((Acid_Waterfall, RDFS.label, Literal("Acid Waterfall")))
g.add((Dead_Crystal_Cave, RDFS.label, Literal("Dead Crystal Cave")))
g.add((Eternal_Wave_Crests, RDFS.label, Literal("Eternal Wave Crests")))
g.add((Flat_Creeper_Spike_Stretch, RDFS.label, Literal("Flat-Creeper Spike Stretch")))
g.add((Forest_of_Crooked_Stone_Columns, RDFS.label, Literal("Forest of Crooked Stone Columns")))
g.add((Gas_Plume_Deposit, RDFS.label, Literal("Gas Plume Deposit")))
g.add((Flat_Creeper_Squid_Spawning_Grounds, RDFS.label, Literal("Flat-Creeper Squid Spawning Grounds")))
g.add((Garden_of_the_Flowers_of_Fortitude, RDFS.label, Literal("Garden of the Flowers of Fortitude")))
g.add((Nanachis_Hideout, RDFS.label, Literal("Nanachi's Hideout")))
g.add((Old_Beasts_Hidden_Hot_Spring, RDFS.label, Literal("Old Beasts' Hidden Hot Spring")))
g.add((Spiral_Ice_Pillars, RDFS.label, Literal("Spiral Ice Pillars")))
g.add((Steel_Fossil_Assemblage, RDFS.label, Literal("Steel Fossil Assemblage")))
g.add((Sticky_Clouds, RDFS.label, Literal("Sticky Clouds")))

g.add((Crystallized_Water_Supports, RDFS.label, Literal("Crystallized Water Supports")))
g.add((Frost_Dragonbones, RDFS.label, Literal("Frost Dragonbones")))
g.add((Ido_Front, RDFS.label, Literal("Ido Front")))
g.add((Altar_of_the_Absolute_Boundary, RDFS.label, Literal("Altar of the Absolute Boundary")))
g.add((Sandstone_Region, RDFS.label, Literal("Sandstone Region")))

# ===============================
# Location Relationships
# ===============================

# World structure
g.add((World, contains, Beoluska))
g.add((World, contains, Sereny))
g.add((World, contains, Jisweku))

g.add((Beoluska, locatedIn, World))
g.add((Sereny, locatedIn, World))
g.add((Jisweku, locatedIn, World))

g.add((Beoluska, contains, Orth))
g.add((Orth, locatedIn, Beoluska))

# Orth districts
g.add((Orth, contains, North_Orth))
g.add((Orth, contains, South_Orth))
g.add((Orth, contains, East_Orth))
g.add((Orth, contains, West_Orth))
g.add((Orth, contains, Central_Orth))

g.add((North_Orth, locatedIn, Orth))
g.add((South_Orth, locatedIn, Orth))
g.add((East_Orth, locatedIn, Orth))
g.add((West_Orth, locatedIn, Orth))
g.add((Central_Orth, locatedIn, Orth))

# Orth locations
g.add((North_Orth, contains, Orth_Windmills))
g.add((Central_Orth, contains, Gate_to_the_Netherworld))
g.add((South_Orth, contains, The_Wharf))
g.add((West_Orth, contains, The_Grand_Pier))
g.add((West_Orth, contains, Belchero_Orphanage))
g.add((East_Orth, contains, Delver_Guild_HQ))

g.add((Orth_Windmills, locatedIn, North_Orth))
g.add((Gate_to_the_Netherworld, locatedIn, Central_Orth))
g.add((The_Wharf, locatedIn, South_Orth))
g.add((The_Grand_Pier, locatedIn, West_Orth))
g.add((Belchero_Orphanage, locatedIn, West_Orth))
g.add((Delver_Guild_HQ, locatedIn, East_Orth))

# The Abyss
g.add((Orth, contains, The_Abyss))
g.add((The_Abyss, locatedIn, Orth))

# The Abyss layers
g.add((The_Abyss, contains, Layer_1))
g.add((The_Abyss, contains, Layer_2))
g.add((The_Abyss, contains, Layer_3))
g.add((The_Abyss, contains, Layer_4))
g.add((The_Abyss, contains, Layer_5))
g.add((The_Abyss, contains, Layer_6))
g.add((The_Abyss, contains, Layer_7))

g.add((Layer_1, locatedIn, The_Abyss))
g.add((Layer_2, locatedIn, The_Abyss))
g.add((Layer_3, locatedIn, The_Abyss))
g.add((Layer_4, locatedIn, The_Abyss))
g.add((Layer_5, locatedIn, The_Abyss))
g.add((Layer_6, locatedIn, The_Abyss))
g.add((Layer_7, locatedIn, The_Abyss))

# Layer 1 locations
g.add((Layer_1, contains, Abode_of_Trees_and_Fossils))
g.add((Layer_1, contains, Big_Gondola))
g.add((Layer_1, contains, Burial_Tower))
g.add((Layer_1, contains, Gate_to_the_Netherworld))
g.add((Layer_1, contains, The_Guiding_Tree))
g.add((Layer_1, contains, Ominaki_Falls))
g.add((Layer_1, contains, Seat_of_the_Waterfall))
g.add((Layer_1, contains, Stargazing_Hill))
g.add((Layer_1, contains, Stone_Ark))
g.add((Layer_1, contains, Twisting_Crag))
g.add((Layer_1, contains, Wind_Riding_Windmills))
g.add((Layer_1, contains, Wuthering))

g.add((Abode_of_Trees_and_Fossils, locatedIn, Layer_1))
g.add((Big_Gondola, locatedIn, Layer_1))
g.add((Burial_Tower, locatedIn, Layer_1))
g.add((Gate_to_the_Netherworld, locatedIn, Layer_1))
g.add((The_Guiding_Tree, locatedIn, Layer_1))
g.add((Ominaki_Falls, locatedIn, Layer_1))
g.add((Seat_of_the_Waterfall, locatedIn, Layer_1))
g.add((Stargazing_Hill, locatedIn, Layer_1))
g.add((Stone_Ark, locatedIn, Layer_1))
g.add((Twisting_Crag, locatedIn, Layer_1))
g.add((Wind_Riding_Windmills, locatedIn, Layer_1))
g.add((Wuthering, locatedIn, Layer_1))

# Layer 2 locations
g.add((Layer_2, contains, Heavens_Waterfall))
g.add((Layer_2, contains, Rohana_Fountainhead))
g.add((Layer_2, contains, Sky_Jellyfish))
g.add((Layer_2, contains, Sleeping_Bed_of_Mushrooms))
g.add((Layer_2, contains, The_Inverted_Forest))

g.add((Heavens_Waterfall, locatedIn, Layer_2))
g.add((Rohana_Fountainhead, locatedIn, Layer_2))
g.add((Sky_Jellyfish, locatedIn, Layer_2))
g.add((Sleeping_Bed_of_Mushrooms, locatedIn, Layer_2))
g.add((The_Inverted_Forest, locatedIn, Layer_2))

g.add((The_Inverted_Forest, contains, Hells_Crossing))
g.add((The_Inverted_Forest, contains, Joint_Delving_Site))
g.add((The_Inverted_Forest, contains, Seeker_Camp))
g.add((The_Inverted_Forest, contains, Sky_Hunting_Grounds))

g.add((Hells_Crossing, locatedIn, The_Inverted_Forest))
g.add((Joint_Delving_Site, locatedIn, The_Inverted_Forest))
g.add((Seeker_Camp, locatedIn, The_Inverted_Forest))
g.add((Sky_Hunting_Grounds, locatedIn, The_Inverted_Forest))

# Layer 3 locations
g.add((Layer_3, contains, Baracocha_Corridors))
g.add((Layer_3, contains, Cumulonimbus_Point))
g.add((Layer_3, contains, Ghostly_Roots))
g.add((Layer_3, contains, Greenery_Layer))
g.add((Layer_3, contains, The_Imprisoned_Pirate_Ship))
g.add((Layer_3, contains, Rumbling_Grounds_of_the_Strong))
g.add((Layer_3, contains, Tallowstone_Layer))

g.add((Baracocha_Corridors, locatedIn, Layer_3))
g.add((Cumulonimbus_Point, locatedIn, Layer_3))
g.add((Ghostly_Roots, locatedIn, Layer_3))
g.add((Greenery_Layer, locatedIn, Layer_3))
g.add((The_Imprisoned_Pirate_Ship, locatedIn, Layer_3))
g.add((Rumbling_Grounds_of_the_Strong, locatedIn, Layer_3))
g.add((Tallowstone_Layer, locatedIn, Layer_3))

# Layer 4 locations
g.add((Layer_4, contains, Acid_Waterfall))
g.add((Layer_4, contains, Dead_Crystal_Cave))
g.add((Layer_4, contains, Eternal_Wave_Crests))
g.add((Layer_4, contains, Flat_Creeper_Spike_Stretch))
g.add((Layer_4, contains, Forest_of_Crooked_Stone_Columns))
g.add((Layer_4, contains, Gas_Plume_Deposit))
g.add((Layer_4, contains, Flat_Creeper_Squid_Spawning_Grounds))
g.add((Layer_4, contains, Garden_of_the_Flowers_of_Fortitude))
g.add((Layer_4, contains, Nanachis_Hideout))
g.add((Layer_4, contains, Old_Beasts_Hidden_Hot_Spring))
g.add((Layer_4, contains, Spiral_Ice_Pillars))
g.add((Layer_4, contains, Steel_Fossil_Assemblage))
g.add((Layer_4, contains, Sticky_Clouds))

g.add((Acid_Waterfall, locatedIn, Layer_4))
g.add((Dead_Crystal_Cave, locatedIn, Layer_4))
g.add((Eternal_Wave_Crests, locatedIn, Layer_4))
g.add((Flat_Creeper_Spike_Stretch, locatedIn, Layer_4))
g.add((Forest_of_Crooked_Stone_Columns, locatedIn, Layer_4))
g.add((Gas_Plume_Deposit, locatedIn, Layer_4))
g.add((Flat_Creeper_Squid_Spawning_Grounds, locatedIn, Layer_4))
g.add((Garden_of_the_Flowers_of_Fortitude, locatedIn, Layer_4))
g.add((Nanachis_Hideout, locatedIn, Layer_4))
g.add((Old_Beasts_Hidden_Hot_Spring, locatedIn, Layer_4))
g.add((Spiral_Ice_Pillars, locatedIn, Layer_4))
g.add((Steel_Fossil_Assemblage, locatedIn, Layer_4))
g.add((Sticky_Clouds, locatedIn, Layer_4))

# Layer 5 locations
g.add((Layer_5, contains, Crystallized_Water_Supports))
g.add((Layer_5, contains, Frost_Dragonbones))
g.add((Layer_5, contains, Ido_Front))
g.add((Layer_5, contains, Sandstone_Region))

g.add((Crystallized_Water_Supports, locatedIn, Layer_5))
g.add((Frost_Dragonbones, locatedIn, Layer_5))
g.add((Ido_Front, locatedIn, Layer_5))
g.add((Sandstone_Region, locatedIn, Layer_5))

g.add((Ido_Front, contains, Altar_of_the_Absolute_Boundary))
g.add((Altar_of_the_Absolute_Boundary, locatedIn, Ido_Front))

# Layer 6
g.add((Layer_6, contains, Iruburu))
g.add((Iruburu, locatedIn, Layer_6))

g.serialize("made_in_abyss_graph.rdf", format="xml")
