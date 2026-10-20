% Assumptions: 
    % Drop rates are taken from expert mode in Terraria

% DROP RATES -------------------------------------------------------------------------------------------------------------------------------------------
% These are dropped from common enemies, so I will assume that the player has these items; they are easily obtained
% Raw materials
player_has(gel).
player_has(stinger).
player_has(vine).
player_has(jungle_spore).

% Ingots
player_has(copper_bar).
player_has(hellstone_bar).
player_has(chlorophyte_bar).

% Weapons not obtainable from crafting/boss 
player_has(star_fury).
player_has(enchanted_sword).
player_has(muramasa).

% All mechanical bosses drop hallowed bars; a shared drop amongst these bosses
is_a(the_twins, any_mechanical_boss).
is_a(the_destroyer, any_mechanical_boss).
is_a(skeletron_prime, any_mechanical_boss).

% CRAFTING RECIPES -------------------------------------------------------------------------------------------------------------------------------------
is_a(lightsbane, any_evil_sword).
is_a(blood_butcherer, any_evil_sword).

% Zenith crafing recipe
crafted_from(zenith, copper_shortsword).
crafted_from(zenith, star_fury).
crafted_from(zenith, enchanted_sword).
crafted_from(zenith, bee_keeper).
crafted_from(zenith, seedler).
crafted_from(zenith, the_horsemans_blade).
crafted_from(zenith, influx_waver).
crafted_from(zenith, star_wrath).
crafted_from(zenith, meowmere).
crafted_from(zenith, terrablade).

% Terrablade crafing recipe
crafted_from(terrablade, broken_hero_sword).
crafted_from(terrablade, true_excalibur).
crafted_from(terrablade, true_nights_edge).

% True excalibur crafting recipe
crafted_from(true_excalibur, chlorophyte_bar).
crafted_from(true_excalibur, excalibur).

% True nights edge crafting recipe
crafted_from(true_nights_edge, nights_edge).
crafted_from(true_nights_edge, soul_of_sight).
crafted_from(true_nights_edge, soul_of_might).
crafted_from(true_nights_edge, soul_of_fright).

% Excalibur crafting recipe
crafted_from(excalibur, hallowed_bar).

% Nights edge crafting recipe
crafted_from(nights_edge, any_evil_sword).
crafted_from(nights_edge, blade_of_grass).
crafted_from(nights_edge, volcano).
crafted_from(nights_edge, muramasa).

% Nights edge components crafting recipes
crafted_from(volcano, hellstone_bar).

crafted_from(blade_of_grass, stinger).
crafted_from(blade_of_grass, jungle_spore).
crafted_from(blade_of_grass, vine).

crafted_from(lightsbane, demonite_bar).
crafted_from(blood_butcherer, crimtane_bar).

crafted_from(copper_shortsword, copper_bar).

crafted_from(demonite_bar, demonite_ore).
crafted_from(crimtane_bar, crimtane_ore).

% DEFEATS (these are suppositions); the actual chance that the player defeats a boss depends on their skill-level and gear
3/4::defeats(eye_of_cthulhu).
1/2::defeats(eater_of_worlds).
1/2::defeats(brain_of_cthulhu).
3/4::defeats(queen_bee).
1/3::defeats(the_twins).
1/3::defeats(the_destroyer).
1/3::defeats(skeletron_prime).
1/2::defeats(plantera).
3/4::defeats(mothron).
3/4::defeats(martian_saucer).
3/4::defeats(pumpking).
1/8::defeats(moon_lord).

defeats(any_mechanical_boss) :- % Disjunction between the mechanical bosses; a player defeats any_mechanical_boss if they defeat at least one
    defeats(the_twins);
    defeats(the_destroyer);
    defeats(skeletron_prime).

% DROP RATES -------------------------------------------------------------------------------------------------------------------------------------------
% Certainties
drop_rate(eater_of_worlds, demonite_ore, 1). % 1 means infers determinism; the item WILL drop with 100% certainty when the boss is defeated
drop_rate(brain_of_cthulhu, crimtane_ore, 1).
drop_rate(the_twins, soul_of_sight, 1).
drop_rate(the_destroyer, soul_of_might, 1).
drop_rate(skeletron_prime, soul_of_fright, 1).
drop_rate(any_mechanical_boss, hallowed_bar, 1).

drop_rate(queen_bee, bee_keeper, 1/3). % Place probabilities in the drop_rate predicate; needed by trials(...) predicate for unfication of P
drop_rate(plantera, seedler, 1/8).
drop_rate(mothron, broken_hero_sword, 7/16).
drop_rate(martian_saucer, influx_waver, 1/6).
drop_rate(pumpking, the_horsemans_blade, 1/20).
drop_rate(moon_lord, meowmere, 1/5).
drop_rate(moon_lord, star_wrath, 1/5).

% STATS ------------------------------------------------------------------------------------------------------------------------------------------------
% Weapon damage
damage(copper_shortsword, 5).
damage(enchanted_sword, 23).
damage(star_fury, 25).
damage(lightsbane, 16).
damage(blood_butcherer, 22).
damage(blade_of_grass, 18).
damage(bee_keeper, 30).
damage(volcano, 40).
damage(muramasa, 24).
damage(nights_edge, 40).

damage(excalibur, 72).
damage(true_nights_edge, 70).
damage(true_excalibur, 72).
damage(seedler, 50).
damage(terrablade, 85).
damage(the_horsemans_blade, 150).
damage(influx_waver, 100).
damage(meowmere, 200).
damage(star_wrath, 170).
damage(zenith, 190).

% Boss health
health(eye_of_cthulhu, 3640).
health(eater_of_worlds, 15120).
health(brain_of_cthulhu, 1350).
health(queen_bee, 4760).
health(skeletron, 8800).
health(wall_of_flesh, 11200).

health(the_twins, 60000).
health(the_destroyer, 93600).
health(skeletron_prime, 42000).
health(plantera, 42000).
health(pumpking, 33800).
health(golem, 46200).
health(lunatic_cultist, 32500).
health(moon_lord, 217500).

player_has(Either) :-
    is_a(Item, Either),
    player_has(Item).

player_has(Item) :- % A player has an item X if it is dropped from a boss Y in which they defeat, or they can craft it
    drop(_, Item); % defeats(Y) is handled in the logic of drops(Y, X); where Y drops X if Y is defeated
    can_craft(Item).

can_craft(Item) :-
    crafted_from(Item, _),
    forall(crafted_from(Item, Other), player_has(Other)). % The player has all items needed to craft X

% FIRST-ORDER PROBABILISTIC CLAUSES --------------------------------------------------------------------------------------------------------------------
% Modified defeat chances in accordance with the owned weapon; compute the chance that the player beats a boss using a specific weapon
P::drop(Boss, Weapon) :- % P binds to Probability
    drop_rate(Boss, Weapon, Probability),
    defeats(Boss),
    P is Probability.

P::weapon_defeats(Boss, Weapon) :-
    damage(Weapon, Dmg),
    health(Boss, Health),
    NumHits is Health / Dmg,
    % K / (K + Hits) ensures that the probability is strictly less than 1, and hence always non-deterministic
    P is 341 / (341 + NumHits). % Here, K = 341 since, for on-tier weapons against bosses, that would be the average no. hits required to defeat that boss

% Case 1: the item drops on the Nth trial
drop_trials(Boss, Item, N) :-
    N > 0,
    trial(Boss, Item, N).

% Case 2: the item drops somewhere between trial 1 and trial N-1
drop_trials(Boss, Item, N) :- 
    N > 0,
    K is N - 1,
    drop_trials(Boss, Item, K).

P::trial(Boss, Item, N) :- % Here, bind P to the probability that the specific item drops from a particular boss
    drop_rate(Boss, Item, P).

query(drop(plantera, seedler)).
query(drop_trials(pumpking, the_horsemans_blade, 50)).