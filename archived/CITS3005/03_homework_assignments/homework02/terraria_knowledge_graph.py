"""
    Importations:
        - Graph: holds collection of RDF triples
        - Namespace: allows for clean construction of URIref sharing same base URL prefix
        - URIRef: reosurce/property within the RDF graph
        - Literal: raw data
"""

from rdflib import Graph, Namespace, URIRef, Literal
from rdflib.namespace import RDF, RDFS

# Graph instantiation
g = Graph()

# 
TERRARIA = Namespace("http://example.org/terraria/") # Acts as a container; need not type out the full URI
g.bind("terraria", TERRARIA)

BOSS = TERRARIA.Boss
ENEMY = TERRARIA.Enemy
WEAPON = TERRARIA.Weapon
MATERIAL = TERRARIA.Material
CRAFTING = TERRARIA.CraftingSource
LOCATION = TERRARIA.Location
PROGRESSION = TERRARIA.Progression

dropped_from = TERRARIA.dropped_from # if the item is a drop from a boss
crafted_from = TERRARIA.crafted_from # An item, which is crafted from other item(s)
crafted_at = TERRARIA.crafted_at # An item, crafted at a specific station
acquired_from = TERRARIA.acquired_from # Where an item can be acquired, or how
is_a = TERRARIA.is_a  # This is specirfic for the generalized cases; the to-be-generalized items must have a relationship with the generalized entities
game_phase = TERRARIA.game_phase # Denotes a relationship between an entity and what phase of the game it unlocks in
damage = TERRARIA.damage # Added for aggregation purposes
health = TERRARIA.health # Also added for aggregation

"""LOCATIONS/METHODS OF ACQUISITION"""
g.add((TERRARIA.Chest, RDF.type, TERRARIA.Location))
g.add((TERRARIA.Chest, RDFS.label, Literal("Chest")))

g.add((TERRARIA.SwordShrine, RDF.type, TERRARIA.Location))
g.add((TERRARIA.SwordShrine, RDFS.label, Literal("Sword Shrine")))

g.add((TERRARIA.Dungeon, RDF.type, TERRARIA.Location))
g.add((TERRARIA.Dungeon, RDFS.label, Literal("Dungeon")))

"""MAJOR GAME PHASES"""
g.add((TERRARIA.PreHardmode, RDF.type, PROGRESSION))
g.add((TERRARIA.PreHardmode, RDFS.label, Literal("Pre-hardmode")))

g.add((TERRARIA.Hardmode, RDF.type, PROGRESSION))
g.add((TERRARIA.Hardmode, RDFS.label, Literal("Hardmode")))

"""BOSSES - I am only adding the progression-specific bosses, or bosses counting towards the Zenith crafting tree"""
# PRE-HARDMODE
g.add((TERRARIA.EyeOfCthulhu, RDF.type, BOSS))
g.add((TERRARIA.EyeOfCthulhu, RDFS.label, Literal("Eye of Cthulhu")))

g.add((TERRARIA.EaterOfWorlds, RDF.type, BOSS))
g.add((TERRARIA.EaterOfWorlds, RDFS.label, Literal("Eater of Worlds")))

g.add((TERRARIA.BrainOfCthulhu, RDF.type, BOSS))
g.add((TERRARIA.BrainOfCthulhu, RDFS.label, Literal("Brain of Cthulhu")))

g.add((TERRARIA.QueenBee, RDF.type, BOSS))
g.add((TERRARIA.QueenBee, RDFS.label, Literal("Queen Bee")))

g.add((TERRARIA.Skeletron, RDF.type, BOSS))
g.add((TERRARIA.Skeletron, RDFS.label, Literal("Skeletron")))

g.add((TERRARIA.WallOfFlesh, RDF.type, BOSS))
g.add((TERRARIA.WallOfFlesh, RDFS.label, Literal("Wall of Flesh")))

# HARDMODE
g.add((TERRARIA.TheTwins, RDF.type, BOSS))
g.add((TERRARIA.TheTwins, RDFS.label, Literal("The Twins")))

g.add((TERRARIA.TheDestroyer, RDF.type, BOSS))
g.add((TERRARIA.TheDestroyer, RDFS.label, Literal("The Destroyer")))

g.add((TERRARIA.SkeletronPrime, RDF.type, BOSS))
g.add((TERRARIA.SkeletronPrime, RDFS.label, Literal("Skeletron Prime")))

g.add((TERRARIA.Plantera, RDF.type, BOSS))
g.add((TERRARIA.Plantera, RDFS.label, Literal("Plantera")))

g.add((TERRARIA.Pumpking, RDF.type, BOSS))
g.add((TERRARIA.Pumpking, RDFS.label, Literal("Pumpking")))

g.add((TERRARIA.Golem, RDF.type, BOSS))
g.add((TERRARIA.Golem, RDFS.label, Literal("Golem")))

g.add((TERRARIA.LunaticCultist, RDF.type, BOSS))
g.add((TERRARIA.LunaticCultist, RDFS.label, Literal("Lunatic Cultist")))

g.add((TERRARIA.MoonLord, RDF.type, BOSS))
g.add((TERRARIA.MoonLord, RDFS.label, Literal("Moon Lord")))

"""WEAPONS - only doing melee weapons"""
# PRE-HARDMODE
g.add((TERRARIA.CopperShortSword, RDF.type, WEAPON))
g.add((TERRARIA.CopperShortSword, RDFS.label, Literal("Copper Shortsword")))

g.add((TERRARIA.StarFury, RDF.type, WEAPON))
g.add((TERRARIA.StarFury, RDFS.label, Literal("Star Fury")))

g.add((TERRARIA.EnchantedSword, RDF.type, WEAPON))
g.add((TERRARIA.EnchantedSword, RDFS.label, Literal("Enchanted Sword")))

g.add((TERRARIA.BeeKeeper, RDF.type, WEAPON))
g.add((TERRARIA.BeeKeeper, RDFS.label, Literal("Bee Keeper")))

g.add((TERRARIA.Lightsbane, RDF.type, WEAPON))
g.add((TERRARIA.Lightsbane, RDFS.label, Literal("Lightsbane")))

g.add((TERRARIA.BloodButcherer, RDF.type, WEAPON))
g.add((TERRARIA.BloodButcherer, RDFS.label, Literal("Blood Butcherer")))

g.add((TERRARIA.BladeOfGrass, RDF.type, WEAPON))
g.add((TERRARIA.BladeOfGrass, RDFS.label, Literal("Blade of Grass")))

g.add((TERRARIA.Volcano, RDF.type, WEAPON))
g.add((TERRARIA.Volcano, RDFS.label, Literal("Volcano")))

g.add((TERRARIA.Muramasa, RDF.type, WEAPON))
g.add((TERRARIA.Muramasa, RDFS.label, Literal("Muramasa")))

g.add((TERRARIA.NightsEdge, RDF.type, WEAPON))
g.add((TERRARIA.NightsEdge, RDFS.label, Literal("Nights Edge")))

# HARDMODE
g.add((TERRARIA.Excalibur, RDF.type, WEAPON))
g.add((TERRARIA.Excalibur, RDFS.label, Literal("Excalibur")))

g.add((TERRARIA.TrueExcalibur, RDF.type, WEAPON))
g.add((TERRARIA.TrueExcalibur, RDFS.label, Literal("True Excalibur")))

g.add((TERRARIA.TrueNightsEdge, RDF.type, WEAPON))
g.add((TERRARIA.TrueNightsEdge, RDFS.label, Literal("True Nights Edge")))

g.add((TERRARIA.Seedler, RDF.type, WEAPON))
g.add((TERRARIA.Seedler, RDFS.label, Literal("Seedler")))

g.add((TERRARIA.InfluxWaver, RDF.type, WEAPON))
g.add((TERRARIA.InfluxWaver, RDFS.label, Literal("Influx Waver")))

g.add((TERRARIA.Terrablade, RDF.type, WEAPON))
g.add((TERRARIA.Terrablade, RDFS.label, Literal("Terrablade")))

g.add((TERRARIA.TheHorsemansBlade, RDF.type, WEAPON))
g.add((TERRARIA.TheHorsemansBlade, RDFS.label, Literal("The Horseman's blade")))

g.add((TERRARIA.Meowmere, RDF.type, WEAPON))
g.add((TERRARIA.Meowmere, RDFS.label, Literal("Meowmere")))

g.add((TERRARIA.StarWrath, RDF.type, WEAPON))
g.add((TERRARIA.StarWrath, RDFS.label, Literal("Star Wrath")))

g.add((TERRARIA.Zenith, RDF.type, WEAPON))
g.add((TERRARIA.Zenith, RDFS.label, Literal("Zenith")))

"""MATERIALS - only the ones necessary for the melee weapons"""
# These ones are for the crafting stations
# For the workbench, and furnace
g.add((TERRARIA.Gel, RDF.type, MATERIAL))
g.add((TERRARIA.Gel, RDFS.label, Literal("Gel")))

g.add((TERRARIA.AnyWood, RDF.type, MATERIAL))
g.add((TERRARIA.AnyWood, RDFS.label, Literal("Any Wood")))

g.add((TERRARIA.StoneBlock, RDF.type, MATERIAL))
g.add((TERRARIA.StoneBlock, RDFS.label, Literal("Stone Block")))

g.add((TERRARIA.Torch, RDF.type, MATERIAL))
g.add((TERRARIA.Torch, RDFS.label, Literal("Torch")))

# For the anvil; anvil craftable from iron or lead
g.add((TERRARIA.CopperOre, RDF.type, MATERIAL))
g.add((TERRARIA.CopperOre, RDFS.label, Literal("Copper Ore")))

g.add((TERRARIA.CopperBar, RDF.type, MATERIAL))
g.add((TERRARIA.CopperBar, RDFS.label, Literal("Copper Bar")))

g.add((TERRARIA.IronOre, RDF.type, MATERIAL))
g.add((TERRARIA.IronOre, RDFS.label, Literal("Iron Ore")))

g.add((TERRARIA.IronBar, RDF.type, MATERIAL))
g.add((TERRARIA.IronBar, RDFS.label, Literal("Iron Bar")))

g.add((TERRARIA.LeadOre, RDF.type, MATERIAL))
g.add((TERRARIA.LeadOre, RDFS.label, Literal("Lead Ore")))

g.add((TERRARIA.LeadBar, RDF.type, MATERIAL))
g.add((TERRARIA.LeadBar, RDFS.label, Literal("Lead Bar")))

# Lightsbane
g.add((TERRARIA.DemoniteOre, RDF.type, MATERIAL))
g.add((TERRARIA.DemoniteOre, RDFS.label, Literal("Demonite Ore")))

g.add((TERRARIA.DemoniteBar, RDF.type, MATERIAL))
g.add((TERRARIA.DemoniteBar, RDFS.label, Literal("Demonite Bar")))

# Blood butcherer
g.add((TERRARIA.CrimtaneOre, RDF.type, MATERIAL))
g.add((TERRARIA.CrimtaneOre, RDFS.label, Literal("Crimtane Ore")))

g.add((TERRARIA.CrimtaneBar, RDF.type, MATERIAL))
g.add((TERRARIA.CrimtaneBar, RDFS.label, Literal("Crimtane Bar")))

# Blade of grass
g.add((TERRARIA.Stinger, RDF.type, MATERIAL)) 
g.add((TERRARIA.Stinger, RDFS.label, Literal("Stinger")))

g.add((TERRARIA.Vine, RDF.type, MATERIAL)) 
g.add((TERRARIA.Vine, RDFS.label, Literal("Vine")))

g.add((TERRARIA.JungleSpore, RDF.type, MATERIAL)) 
g.add((TERRARIA.JungleSpore, RDFS.label, Literal("Jungle Spore")))

# Volcano
g.add((TERRARIA.HellstoneOre, RDF.type, MATERIAL)) 
g.add((TERRARIA.HellstoneOre, RDFS.label, Literal("Hellstone Ore")))

g.add((TERRARIA.HellstoneBar, RDF.type, MATERIAL)) 
g.add((TERRARIA.HellstoneBar, RDFS.label, Literal("Hellstone Bar")))

# Hardmode anvil/forges
g.add((TERRARIA.MythrilOre, RDF.type, MATERIAL)) 
g.add((TERRARIA.MythrilOre, RDFS.label, Literal("Mythril Ore")))

g.add((TERRARIA.MythrilBar, RDF.type, MATERIAL)) 
g.add((TERRARIA.MythrilBar, RDFS.label, Literal("Mythril Bar")))

g.add((TERRARIA.OrichalcumOre, RDF.type, MATERIAL)) 
g.add((TERRARIA.OrichalcumOre, RDFS.label, Literal("Orichalcum Ore")))

g.add((TERRARIA.OrichalcumBar, RDF.type, MATERIAL)) 
g.add((TERRARIA.OrichalcumBar, RDFS.label, Literal("Orichalcum Bar")))

g.add((TERRARIA.AdamantiteOre, RDF.type, MATERIAL)) 
g.add((TERRARIA.AdamantiteOre, RDFS.label, Literal("Adamantite Ore")))

g.add((TERRARIA.AdamantiteBar, RDF.type, MATERIAL)) 
g.add((TERRARIA.AdamantiteBar, RDFS.label, Literal("Adamantite Bar")))

g.add((TERRARIA.TitaniumOre, RDF.type, MATERIAL)) 
g.add((TERRARIA.TitaniumOre, RDFS.label, Literal("Titanium Ore")))

g.add((TERRARIA.TitaniumBar, RDF.type, MATERIAL)) 
g.add((TERRARIA.TitaniumBar, RDFS.label, Literal("Titanium Bar")))

# Excalibur
g.add((TERRARIA.HallowedBar, RDF.type, MATERIAL)) 
g.add((TERRARIA.HallowedBar, RDFS.label, Literal("Hallowed Bar")))

# True Excalibur
g.add((TERRARIA.ChlorophyteOre, RDF.type, MATERIAL)) 
g.add((TERRARIA.ChlorophyteOre, RDFS.label, Literal("Chlorophyte Ore")))

g.add((TERRARIA.ChlorophyteBar, RDF.type, MATERIAL)) 
g.add((TERRARIA.ChlorophyteBar, RDFS.label, Literal("Chlorophyte Bar")))

# True Nights Edge
g.add((TERRARIA.SoulOfSight, RDF.type, MATERIAL)) 
g.add((TERRARIA.SoulOfSight, RDFS.label, Literal("Soul of Sight")))

g.add((TERRARIA.SoulOfMight, RDF.type, MATERIAL)) 
g.add((TERRARIA.SoulOfMight, RDFS.label, Literal("Soul of Might")))

g.add((TERRARIA.SoulOfFright, RDF.type, MATERIAL)) 
g.add((TERRARIA.SoulOfFright, RDFS.label, Literal("Soul of Fright")))

# Terrablade
g.add((TERRARIA.BrokenHeroSword, RDF.type, MATERIAL)) 
g.add((TERRARIA.BrokenHeroSword, RDFS.label, Literal("Broken Hero Sword")))

"""ENEMIES - only the ones required for the zenith crafting tree"""
# PRE-HARDMODE
# Required for the gel drop
g.add((TERRARIA.Slime, RDF.type, ENEMY))
g.add((TERRARIA.Slime, RDFS.label, Literal("Slime")))

# Required for the stinger drop
g.add((TERRARIA.Hornet, RDF.type, ENEMY))
g.add((TERRARIA.Hornet, RDFS.label, Literal("Hornet")))

# Required for the vine drop
g.add((TERRARIA.Maneater, RDF.type, ENEMY))
g.add((TERRARIA.Maneater, RDFS.label, Literal("Maneater")))

# HARDMODE
# Required for the broken hero sword drop
g.add((TERRARIA.Mothron, RDF.type, ENEMY))
g.add((TERRARIA.Mothron, RDFS.label, Literal("Mothron")))

# Required for the influx waver drop
g.add((TERRARIA.MartianSaucer, RDF.type, BOSS)) # Technically a mini-boss
g.add((TERRARIA.MartianSaucer, RDFS.label, Literal("Martian Saucer")))

"""CRAFTING STATIONS - only the ones required for Zenith"""
# PRE-HARDMODE
g.add((TERRARIA.Hand, RDF.type, CRAFTING))
g.add((TERRARIA.Hand, RDFS.label, Literal("Hand")))

g.add((TERRARIA.Workbench, RDF.type, CRAFTING))
g.add((TERRARIA.Workbench, RDFS.label, Literal("Workbench")))

g.add((TERRARIA.Furnace, RDF.type, CRAFTING))
g.add((TERRARIA.Furnace, RDFS.label, Literal("Furnace")))

g.add((TERRARIA.Anvil, RDF.type, CRAFTING))
g.add((TERRARIA.Anvil, RDFS.label, Literal("Anvil")))

g.add((TERRARIA.DemonAltar, RDF.type, CRAFTING))
g.add((TERRARIA.DemonAltar, RDFS.label, Literal("Demon Altar")))

g.add((TERRARIA.CrimsonAltar, RDF.type, CRAFTING))
g.add((TERRARIA.CrimsonAltar, RDFS.label, Literal("Crimson Altar")))

g.add((TERRARIA.Hellforge, RDF.type, CRAFTING))
g.add((TERRARIA.Hellforge, RDFS.label, Literal("Hellforge")))

#HARDMODE
g.add((TERRARIA.MythrilAnvil, RDF.type, CRAFTING))
g.add((TERRARIA.MythrilAnvil, RDFS.label, Literal("Mythril Anvil")))

g.add((TERRARIA.OrichalcumAnvil, RDF.type, CRAFTING))
g.add((TERRARIA.OrichalcumAnvil, RDFS.label, Literal("Orichalcum Anvil")))

g.add((TERRARIA.TitaniumForge, RDF.type, CRAFTING))
g.add((TERRARIA.TitaniumForge, RDFS.label, Literal("Titanium Forge")))

g.add((TERRARIA.AdamantiteForge, RDF.type, CRAFTING))
g.add((TERRARIA.AdamantiteForge, RDFS.label, Literal("Adamantite Forge")))

"""GENERALIZATIONS"""
# CRAFTING
g.add((TERRARIA.AnyAnvil, RDF.type, CRAFTING))
g.add((TERRARIA.AnyAnvil, RDFS.label, Literal("Any anvil")))

g.add((TERRARIA.AnyForge, RDF.type, CRAFTING))
g.add((TERRARIA.AnyForge, RDFS.label, Literal("Any forge")))

g.add((TERRARIA.AnyAltar, RDF.type, CRAFTING))
g.add((TERRARIA.AnyAltar, RDFS.label, Literal("Any altar")))

g.add((TERRARIA.HardmodeAnvil, RDF.type, CRAFTING))
g.add((TERRARIA.HardmodeAnvil, RDFS.label, Literal("Hardmode Anvil")))

g.add((TERRARIA.HardmodeForge, RDF.type, CRAFTING))
g.add((TERRARIA.HardmodeForge, RDFS.label, Literal("Hardmode Forge")))

# WEAPONS
g.add((TERRARIA.AnyEvilSword, RDF.type, WEAPON))
g.add((TERRARIA.AnyEvilSword, RDFS.label, Literal("Any Evil Sword")))

# BOSSES
g.add((TERRARIA.AnyMechanicalBoss, RDF.type, BOSS))
g.add((TERRARIA.AnyMechanicalBoss, RDFS.label, Literal("Any Mechanical Boss")))

"""RELATIONS"""
# GENERALIZATION RELATIONS - IS links empty nodes to ones we have actually established
# Crafting sources
g.add((TERRARIA.Furnace, is_a, TERRARIA.AnyForge))
g.add((TERRARIA.Hellforge, is_a, TERRARIA.AnyForge))
g.add((TERRARIA.AdamantiteForge, is_a, TERRARIA.AnyForge))
g.add((TERRARIA.TitaniumForge, is_a, TERRARIA.AnyForge))

g.add((TERRARIA.AdamantiteForge, is_a, TERRARIA.HardmodeForge))
g.add((TERRARIA.TitaniumForge, is_a, TERRARIA.HardmodeForge))

g.add((TERRARIA.Anvil, is_a, TERRARIA.AnyAnvil))
g.add((TERRARIA.MythrilAnvil, is_a, TERRARIA.AnyAnvil))
g.add((TERRARIA.OrichalcumAnvil, is_a, TERRARIA.AnyAnvil))

g.add((TERRARIA.MythrilAnvil, is_a, TERRARIA.HardmodeAnvil))
g.add((TERRARIA.OrichalcumAnvil, is_a, TERRARIA.HardmodeAnvil))

g.add((TERRARIA.DemonAltar, is_a, TERRARIA.AnyAltar))
g.add((TERRARIA.CrimsonAltar, is_a, TERRARIA.AnyAltar))

# Bosses
g.add((TERRARIA.TheTwins, is_a, TERRARIA.AnyMechanicalBoss))
g.add((TERRARIA.TheDestroyer, is_a, TERRARIA.AnyMechanicalBoss))
g.add((TERRARIA.SkeletronPrime, is_a, TERRARIA.AnyMechanicalBoss))

# Weapons
g.add((TERRARIA.Lightsbane, is_a, TERRARIA.AnyEvilSword))
g.add((TERRARIA.BloodButcherer, is_a, TERRARIA.AnyEvilSword))

# CRAFTING RELATIONS
# Materials crafting: bars
g.add((TERRARIA.CopperBar, crafted_from, TERRARIA.CopperOre))
g.add((TERRARIA.CopperBar, crafted_at, TERRARIA.AnyForge))

g.add((TERRARIA.IronBar, crafted_from, TERRARIA.IronOre))
g.add((TERRARIA.IronBar, crafted_at, TERRARIA.AnyForge))

g.add((TERRARIA.LeadBar, crafted_from, TERRARIA.LeadOre))
g.add((TERRARIA.LeadBar, crafted_at, TERRARIA.AnyForge))

g.add((TERRARIA.DemoniteBar, crafted_from, TERRARIA.DemoniteOre))
g.add((TERRARIA.DemoniteBar, crafted_at, TERRARIA.AnyForge))

g.add((TERRARIA.CrimtaneBar, crafted_from, TERRARIA.CrimtaneOre))
g.add((TERRARIA.CrimtaneBar, crafted_at, TERRARIA.AnyForge))

g.add((TERRARIA.HellstoneBar, crafted_from, TERRARIA.HellstoneOre))
g.add((TERRARIA.HellstoneBar, crafted_at, TERRARIA.Hellforge))

g.add((TERRARIA.MythrilBar, crafted_from, TERRARIA.MythrilOre))
g.add((TERRARIA.MythrilBar, crafted_at, TERRARIA.AnyForge))

g.add((TERRARIA.OrichalcumBar, crafted_from, TERRARIA.OrichalcumOre))
g.add((TERRARIA.OrichalcumBar, crafted_at, TERRARIA.AnyForge))

g.add((TERRARIA.AdamantiteBar, crafted_from, TERRARIA.AdamantiteOre))
g.add((TERRARIA.AdamantiteBar, crafted_at, TERRARIA.HardmodeForge))

g.add((TERRARIA.TitaniumBar, crafted_from, TERRARIA.TitaniumOre))
g.add((TERRARIA.TitaniumBar, crafted_at, TERRARIA.HardmodeForge))

g.add((TERRARIA.ChlorophyteBar, crafted_from, TERRARIA.ChlorophyteOre))
g.add((TERRARIA.ChlorophyteBar, crafted_at, TERRARIA.HardmodeForge))

# Miscellaneous
g.add((TERRARIA.Torch, crafted_from, TERRARIA.Gel))
g.add((TERRARIA.Torch, crafted_from, TERRARIA.AnyWood))

# Weapons
g.add((TERRARIA.CopperShortSword, crafted_from, TERRARIA.CopperBar))
g.add((TERRARIA.CopperShortSword, crafted_at, TERRARIA.AnyAnvil))

g.add((TERRARIA.Lightsbane, crafted_from, TERRARIA.DemoniteBar))
g.add((TERRARIA.Lightsbane, crafted_at, TERRARIA.AnyAnvil))

g.add((TERRARIA.BloodButcherer, crafted_from, TERRARIA.CrimtaneBar))
g.add((TERRARIA.BloodButcherer, crafted_at, TERRARIA.AnyAnvil))

g.add((TERRARIA.BladeOfGrass, crafted_from, TERRARIA.Stinger))
g.add((TERRARIA.BladeOfGrass, crafted_from, TERRARIA.JungleSpore))
g.add((TERRARIA.BladeOfGrass, crafted_from, TERRARIA.Vine))
g.add((TERRARIA.BladeOfGrass, crafted_at, TERRARIA.AnyAnvil))

g.add((TERRARIA.Volcano, crafted_from, TERRARIA.HellstoneBar))
g.add((TERRARIA.Volcano, crafted_at, TERRARIA.AnyAnvil))

g.add((TERRARIA.NightsEdge, crafted_from, TERRARIA.AnyEvilSword))
g.add((TERRARIA.NightsEdge, crafted_from, TERRARIA.BladeOfGrass))
g.add((TERRARIA.NightsEdge, crafted_from, TERRARIA.Volcano))
g.add((TERRARIA.NightsEdge, crafted_from, TERRARIA.Muramasa))
g.add((TERRARIA.NightsEdge, crafted_at, TERRARIA.AnyAltar))

g.add((TERRARIA.Excalibur, crafted_from, TERRARIA.HallowedBar))
g.add((TERRARIA.Excalibur, crafted_at, TERRARIA.HardmodeForge))

g.add((TERRARIA.TrueExcalibur, crafted_from, TERRARIA.Excalibur))
g.add((TERRARIA.TrueExcalibur, crafted_from, TERRARIA.ChlorophyteBar))
g.add((TERRARIA.TrueExcalibur, crafted_at, TERRARIA.HardmodeAnvil))

g.add((TERRARIA.TrueNightsEdge, crafted_from, TERRARIA.NightsEdge))
g.add((TERRARIA.TrueNightsEdge, crafted_from, TERRARIA.SoulOfSight))
g.add((TERRARIA.TrueNightsEdge, crafted_from, TERRARIA.SoulOfMight))
g.add((TERRARIA.TrueNightsEdge, crafted_from, TERRARIA.SoulOfFright))
g.add((TERRARIA.TrueNightsEdge, crafted_at, TERRARIA.HardmodeAnvil))

g.add((TERRARIA.Terrablade, crafted_from, TERRARIA.TrueNightsEdge))
g.add((TERRARIA.Terrablade, crafted_from, TERRARIA.TrueExcalibur))
g.add((TERRARIA.Terrablade, crafted_from, TERRARIA.BrokenHeroSword))
g.add((TERRARIA.Terrablade, crafted_at, TERRARIA.HardmodeAnvil))

g.add((TERRARIA.Zenith, crafted_from, TERRARIA.CopperShortSword))
g.add((TERRARIA.Zenith, crafted_from, TERRARIA.StarFury))
g.add((TERRARIA.Zenith, crafted_from, TERRARIA.EnchantedSword))
g.add((TERRARIA.Zenith, crafted_from, TERRARIA.BeeKeeper))
g.add((TERRARIA.Zenith, crafted_from, TERRARIA.Seedler))
g.add((TERRARIA.Zenith, crafted_from, TERRARIA.TheHorsemansBlade))
g.add((TERRARIA.Zenith, crafted_from, TERRARIA.InfluxWaver))
g.add((TERRARIA.Zenith, crafted_from, TERRARIA.StarWrath))
g.add((TERRARIA.Zenith, crafted_from, TERRARIA.Meowmere))
g.add((TERRARIA.Zenith, crafted_from, TERRARIA.Terrablade))
g.add((TERRARIA.Zenith, crafted_at, TERRARIA.HardmodeAnvil))

# DROPPED-FROM RELATIONS
# Materials
g.add((TERRARIA.Gel, dropped_from, TERRARIA.Slime))
g.add((TERRARIA.Stinger, dropped_from, TERRARIA.Hornet))
g.add((TERRARIA.Vine, dropped_from, TERRARIA.Maneater))
g.add((TERRARIA.DemoniteOre, dropped_from, TERRARIA.EaterOfWorlds))
g.add((TERRARIA.CrimtaneOre, dropped_from, TERRARIA.BrainOfCthulhu))
g.add((TERRARIA.HallowedBar, dropped_from, TERRARIA.AnyMechanicalBoss))
g.add((TERRARIA.SoulOfSight, dropped_from, TERRARIA.TheTwins))
g.add((TERRARIA.SoulOfMight, dropped_from, TERRARIA.TheDestroyer))
g.add((TERRARIA.SoulOfFright, dropped_from, TERRARIA.SkeletronPrime))
g.add((TERRARIA.BrokenHeroSword, dropped_from, TERRARIA.Mothron))

# Weapons
g.add((TERRARIA.BeeKeeper, dropped_from, TERRARIA.QueenBee))
g.add((TERRARIA.Seedler, dropped_from, TERRARIA.Plantera))
g.add((TERRARIA.InfluxWaver, dropped_from, TERRARIA.MartianSaucer))
g.add((TERRARIA.TheHorsemansBlade, dropped_from, TERRARIA.Pumpking))
g.add((TERRARIA.Meowmere, dropped_from, TERRARIA.MoonLord))
g.add((TERRARIA.StarWrath, dropped_from, TERRARIA.MoonLord))

# ACQUIRED_FROM RELATIONS
g.add((TERRARIA.StarFury, acquired_from, TERRARIA.Chest))
g.add((TERRARIA.EnchantedSword, acquired_from, TERRARIA.SwordShrine))
g.add((TERRARIA.Muramasa, acquired_from, TERRARIA.Dungeon))

# GAME_PHASE RELATIONS - only doing bosses, weapons, and enemies
# Bosses
g.add((TERRARIA.EyeOfCthulhu, game_phase, TERRARIA.PreHardmode))
g.add((TERRARIA.EaterOfWorlds, game_phase, TERRARIA.PreHardmode))
g.add((TERRARIA.BrainOfCthulhu, game_phase, TERRARIA.PreHardmode))
g.add((TERRARIA.QueenBee, game_phase, TERRARIA.PreHardmode))
g.add((TERRARIA.Skeletron, game_phase, TERRARIA.PreHardmode))
g.add((TERRARIA.WallOfFlesh, game_phase, TERRARIA.PreHardmode))

g.add((TERRARIA.TheTwins, game_phase, TERRARIA.Hardmode))
g.add((TERRARIA.TheDestroyer, game_phase, TERRARIA.Hardmode))
g.add((TERRARIA.SkeletronPrime, game_phase, TERRARIA.Hardmode))
g.add((TERRARIA.Plantera, game_phase, TERRARIA.Hardmode))
g.add((TERRARIA.Pumpking, game_phase, TERRARIA.Hardmode))
g.add((TERRARIA.Golem, game_phase, TERRARIA.Hardmode))
g.add((TERRARIA.LunaticCultist, game_phase, TERRARIA.Hardmode))
g.add((TERRARIA.MoonLord, game_phase, TERRARIA.Hardmode))

# Weapons
g.add((TERRARIA.CopperShortSword, game_phase, TERRARIA.PreHardmode))
g.add((TERRARIA.StarFury, game_phase, TERRARIA.PreHardmode))
g.add((TERRARIA.EnchantedSword, game_phase, TERRARIA.PreHardmode))
g.add((TERRARIA.BeeKeeper, game_phase, TERRARIA.PreHardmode))
g.add((TERRARIA.Lightsbane, game_phase, TERRARIA.PreHardmode))
g.add((TERRARIA.BloodButcherer, game_phase, TERRARIA.PreHardmode))
g.add((TERRARIA.BladeOfGrass, game_phase, TERRARIA.PreHardmode))
g.add((TERRARIA.Volcano, game_phase, TERRARIA.PreHardmode))
g.add((TERRARIA.Muramasa, game_phase, TERRARIA.PreHardmode))
g.add((TERRARIA.NightsEdge, game_phase, TERRARIA.PreHardmode))

g.add((TERRARIA.Excalibur, game_phase, TERRARIA.Hardmode))
g.add((TERRARIA.TrueExcalibur, game_phase, TERRARIA.Hardmode))
g.add((TERRARIA.TrueNightsEdge, game_phase, TERRARIA.Hardmode))
g.add((TERRARIA.Seedler, game_phase, TERRARIA.Hardmode))
g.add((TERRARIA.InfluxWaver, game_phase, TERRARIA.Hardmode))
g.add((TERRARIA.Terrablade, game_phase, TERRARIA.Hardmode))
g.add((TERRARIA.TheHorsemansBlade, game_phase, TERRARIA.Hardmode))
g.add((TERRARIA.Meowmere, game_phase, TERRARIA.Hardmode))
g.add((TERRARIA.StarWrath, game_phase, TERRARIA.Hardmode))
g.add((TERRARIA.Zenith, game_phase, TERRARIA.Hardmode))

# Enemies
g.add((TERRARIA.Slime, game_phase, TERRARIA.PreHardmode))
g.add((TERRARIA.Hornet, game_phase, TERRARIA.PreHardmode))
g.add((TERRARIA.Maneater, game_phase, TERRARIA.PreHardmode))

g.add((TERRARIA.Mothron, game_phase, TERRARIA.Hardmode))
g.add((TERRARIA.MartianSaucer, game_phase, TERRARIA.Hardmode))

# Boss health - since enemy health scales with game progression, I'm leaving it out
g.add((TERRARIA.EyeOfCthulhu, health, Literal(3640)))
g.add((TERRARIA.EaterOfWorlds, health, Literal(15120)))
g.add((TERRARIA.BrainOfCthulhu, health, Literal(1350)))
g.add((TERRARIA.QueenBee, health, Literal(4760)))
g.add((TERRARIA.Skeletron, health, Literal(8800)))
g.add((TERRARIA.WallOfFlesh, health, Literal(11200)))

g.add((TERRARIA.TheTwins, health, Literal(60000)))
g.add((TERRARIA.TheDestroyer, health, Literal(93600)))
g.add((TERRARIA.SkeletronPrime, health, Literal(42000)))
g.add((TERRARIA.Plantera, health, Literal(42000)))
g.add((TERRARIA.Pumpking, health, Literal(33800)))
g.add((TERRARIA.Golem, health, Literal(46200)))
g.add((TERRARIA.LunaticCultist, health, Literal(32500)))
g.add((TERRARIA.MoonLord, health, Literal(217500)))

# Weapon damage
g.add((TERRARIA.CopperShortSword, damage, Literal(5)))
g.add((TERRARIA.EnchantedSword, damage, Literal(23)))
g.add((TERRARIA.StarFury, damage, Literal(25)))
g.add((TERRARIA.Lightsbane, damage, Literal(16)))
g.add((TERRARIA.BloodButcherer, damage, Literal(22)))
g.add((TERRARIA.BladeOfGrass, damage, Literal(18)))
g.add((TERRARIA.Volcano, damage, Literal(40)))
g.add((TERRARIA.BeeKeeper, damage, Literal(30)))
g.add((TERRARIA.Muramasa, damage, Literal(24)))
g.add((TERRARIA.NightsEdge, damage, Literal(40)))

g.add((TERRARIA.Excalibur, damage, Literal(72)))
g.add((TERRARIA.TrueNightsEdge, damage, Literal(70)))
g.add((TERRARIA.TrueExcalibur, damage, Literal(72)))
g.add((TERRARIA.Seedler, damage, Literal(50)))
g.add((TERRARIA.Terrablade, damage, Literal(85)))
g.add((TERRARIA.TheHorsemansBlade, damage, Literal(150)))
g.add((TERRARIA.InfluxWaver, damage, Literal(100)))
g.add((TERRARIA.Meowmere, damage, Literal(200)))
g.add((TERRARIA.StarWrath, damage, Literal(170)))
g.add((TERRARIA.Zenith, damage, Literal(190)))

g.serialize(destination="terraria.rdf", format="xml")

def printer(raw) -> None:
    cleaned = []

    # Conditions: 
        # if number, assume a literal, and append
        # If non-number, take [-1] index, and append

    for row in raw:
        temp = []

        for item in row:
            if isinstance(item, URIRef): # Checks if we are dealing with text
                temp.append(item.split("/")[-1])
            elif isinstance(item, Literal): # Checks if we are dealing with digit types
                temp.append(round(float(item.split(",")[0])))

        cleaned.append(temp)

    for i in cleaned:
        string_yield = ""

        for j in range(len(i)):
            if j < len(i) - 1:
                string_yield += f"{i[j]}: "
            else:
                string_yield += f"{i[j]}"
        print(string_yield)

# Possible example queries:
    # Get boss health > x
    # Get weapon damage > x
    # Get no. pre-hardmode bosses (and no. hardmode bosses)
    # Get no. crafting ingredients required for something

" STANDARD QUERIES "
# Yield all bosses and the game phases in which they belong to
boss_phase_query = """
    SELECT ?boss ?phase
    WHERE {
        ?boss terraria:game_phase ?phase .
        ?boss a terraria:Boss .    
        }
"""

# Yield all items in the Zenith crafting tree
recursive_crafting_query = """
    SELECT ?crafting
    WHERE {
        terraria:Zenith terraria:crafted_from+ ?crafting
    }
"""

# Yield all items dropped from Moon Lord
boss_drop_query = """
    SELECT ?item
    WHERE {
        ?item terraria:dropped_from terraria:MoonLord
    }
"""

# Return all recipes using a specific item (this one should be interesting)
item_used_in_query = """
    SELECT ?weapon
    WHERE {
        ?weapon terraria:crafted_from+ terraria:BladeOfGrass .
        ?weapon terraria:game_phase terraria:Hardmode
    }
"""

boss_phase_result = g.query(boss_phase_query)
recursive_crafting_result = g.query(recursive_crafting_query)
boss_drop_result = g.query(boss_drop_query)
item_used_in_result = g.query(item_used_in_query)

# printer(recursive_crafting_result)
# printer(boss_drop_result)
# printer(item_used_in_result)

# Yield avg boss hp
avg_boss_hp = """
    SELECT (AVG(?hp) AS ?avgHp)
    WHERE {
        ?boss a terraria:Boss .
        ?boss terraria:health ?hp
    }
"""

# Yield the total number of items required to craft a specific item
# ^ means to traverse is_a in reverse; so traverse from AnyEvilSword to the swords themselves (i.e., Lightsbane, BloodButcherer)
item_crafting_tree_size_query = """
    SELECT (COUNT(DISTINCT ?item) as ?numItems)
    WHERE {
        terraria:Zenith (terraria:crafted_from | ^terraria:is_a)+ ?item
    }
"""

# These variables shall store the results of the query (which has been written above)
avg_boss_hp_result = g.query(avg_boss_hp)
item_crafting_tree_size_result = g.query(item_crafting_tree_size_query)

# printer(avg_boss_hp_result)
printer(item_crafting_tree_size_result)