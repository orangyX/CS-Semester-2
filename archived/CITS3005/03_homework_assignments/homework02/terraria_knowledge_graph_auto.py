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
TERRARIA = Namespace("http://example.org/terraria/") # require / after, since it glues together: http://terraria_knowledge_graph.comBoss
g.bind("terraria", TERRARIA)

BOSS = TERRARIA.Boss
ENEMY = TERRARIA.Enemy
WEAPON = TERRARIA.Weapon
MATERIAL = TERRARIA.Material
CRAFTING = TERRARIA.CraftingSource
LOCATION = TERRARIA.Location
 # This is specirfic for the generalized cases; the to-be-generalized items must have a relationship with the generalized entities

dropped_from = TERRARIA.dropped_from # if the item is a drop from a boss
crafted_from = TERRARIA.crafted_from
crafted_at = TERRARIA.crafted_at
acquired_from = TERRARIA.acquired_from
is_a = TERRARIA.is_a

def add_objects() -> None:
    g.add((TERRARIA.Chest, RDF.type, TERRARIA.Location))
    g.add((TERRARIA.Chest, RDFS.label, Literal("Chest")))

    g.add((TERRARIA.SwordShrine, RDF.type, TERRARIA.Location))
    g.add((TERRARIA.SwordShrine, RDFS.label, Literal("Sword Shrine")))

    g.add((TERRARIA.Dungeon, RDF.type, TERRARIA.Location))
    g.add((TERRARIA.Dungeon, RDFS.label, Literal("Dungeon")))

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
    g.add((TERRARIA.CrimtaneOre, dropped_from, TERRARIA.BrainOfCthulu))
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

    # ACQUIRED-FROM RELATIONS
    g.add((TERRARIA.StarFury, acquired_from, TERRARIA.Chest))
    g.add((TERRARIA.EnchantedSword, acquired_from, TERRARIA.SwordShrine))
    g.add((TERRARIA.Muramasa, acquired_from, TERRARIA.Dungeon))

    g.serialize(destination="terraria.rdf", format="xml")


"""LOCATION - includes objects, or biomes/structures"""

def printer(raw, num_vars: int) -> None:
    raw_lst = [raw[r] for r in range(num_vars)]
    processed_lst = []

    for i in range(len(raw_lst)):
        processed_lst.append(raw_lst[i].split("/")[-1])

    for i in processed_lst:
        print(i)

def queryer() -> None:    
    relation = input("Select relation: ")
    entity = input("Enter entity: ")
    new_query = None

    if relation == "dropped_from":
        new_query = f"""SELECT DISTINCT ?x
            WHERE {{
                 ?x terraria:{relation} terraria:{entity}
            }}
        """
    if relation == "crafted_from" or relation == "acquired_from":
        new_query = f"""SELECT DISTINCT ?x
            WHERE {{
                 terraria:{entity} terraria:{relation} ?x
            }}
        """

    if new_query is not None:
        queried = g.query(new_query)

        if len(queried) == 0:
            print(f"No results retrievable from the query:\n{new_query}")

        for row in queried:
            printer(row, 1)
        print("\n")
    else:
        print("Illegal query")

zenith_crafting_ingredients = """
    SELECT DISTINCT ?x
    WHERE {
        terraria:Zenith terraria:crafted_from ?x
    }
"""

# The + operator means "follow the path as deeply as possible"
copper_ore_crafting = """
    SELECT DISTINCT ?x
    WHERE {
        ?x terraria:crafted_from+ terraria:CopperOre
    }
"""

crafting_ore_copper = """
    SELECT DISTINCT ?x
    WHERE {
        terraria:Zenith terraria:crafted_from+ ?x
    }
"""

zenith_ingredients = g.query(zenith_crafting_ingredients)
# something_else = g.query(crafting_ore_copper)

# for row in something_else:
#     printer(row, 1)
# print("\n")

# for row in mechanical_query:
#     printer(row, 1)

# Continue from here
# Goal: make a query; ask what recipes use a specified item
# Other goal: add + to show the growing reuslt list

if __name__ == "__main__":
    add_objects()

    while True:
        queryer()