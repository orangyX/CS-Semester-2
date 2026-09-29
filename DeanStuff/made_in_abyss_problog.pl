

% https://problog.readthedocs.io/en/latest/

% =========================
% Facts from graph
% =========================

% Beast entities
beast(amaranthine_deceptor).
beast(orb_piercer).
beast(hammerbeak).
beast(shroombear).
beast(crimson_splitjaw).
beast(corpse_weeper).
beast(hamashirama).
beast(inbyo).
% tie beasts to their corresponding danger levels
has_danger_level(amaranthine_deceptor, absurd_danger).
has_danger_level(orb_piercer, absurd_danger).
has_danger_level(hammerbeak, insignificant_danger).
has_danger_level(shroombear, harmless_danger).
has_danger_level(crimson_splitjaw, deadly_danger).
has_danger_level(corpse_weeper, serious_danger).
has_danger_level(hamashirama, insignificant_danger).
has_danger_level(inbyo, caution_danger).
% tie beasts to their corresponding inhabitence
lives_in(hammerbeak, layer_1).
lives_in(corpse_weeper, layer_2).
lives_in(inbyo, layer_2).
lives_in(crimson_splitjaw, layer_3).
lives_in(amaranthine_deceptor, layer_4).
lives_in(orb_piercer, layer_4).
lives_in(shroombear, layer_4).
lives_in(hamashirama, layer_5).
% tie a location to teh requirements for that place
layer_requirement(layer_1, red_whistle).
layer_requirement(layer_2, blue_whistle).
layer_requirement(layer_3, moon_whistle).
layer_requirement(layer_4, black_whistle).
layer_requirement(layer_5, white_whistle).
% Character entities
character(kiyui).
character(reg).
character(marulk).
character(jiruo).
character(bido).
character(bondrewd).
% Tie characters to their correspinding whistle rank
whistle_rank(kiyui, bell).
whistle_rank(reg, red_whistle).
whistle_rank(marulk, blue_whistle).
whistle_rank(jiruo, moon_whistle).
whistle_rank(bido, black_whistle).
whistle_rank(bondrewd, white_whistle).
% Give whistles independent numerical representations 
rank_experience(bell, 0).
rank_experience(red_whistle, 1).
rank_experience(blue_whistle, 2).
rank_experience(moon_whistle, 3).
rank_experience(black_whistle, 4).
rank_experience(white_whistle, 5).

% Probability clauses
% Note most of the numbers are made up, as theres no real probable way to determine these dangers. 
% Complexity is required but i'll guess on what the show provides or shows.

% Chance a person encounters a beast 
0.3::encounters(X) :- beast(X).

% probability of an encounter being fatel if x danger level is encountered
0.01::fatal_if_encountered(X) :- has_danger_level(X, harmless_danger).
0.05::fatal_if_encountered(X) :- has_danger_level(X, insignificant_danger).
0.15::fatal_if_encountered(X) :- has_danger_level(X, caution_danger).
0.35::fatal_if_encountered(X) :- has_danger_level(X, serious_danger).
0.60::fatal_if_encountered(X) :- has_danger_level(X, deadly_danger).
0.85::fatal_if_encountered(X) :- has_danger_level(X, absurd_danger).

% An incident occurs when an encounter occurs AND is fatal
incident(X) :- encounters(X), fatal_if_encountered(X).

% An incident occurs in a layer if the incident occurs and the beast lives in that layer.
incident_in_layer(Layer) :- lives_in(Beast, Layer), incident(Beast).

% Probability of an incident being underprepared eg. Location requirement > delvers experience.
% Character X, their corresponding whistle rank and numerical value. 
% A locatoins required rank, and the numerical value of that. 
% Compare the characters numerical value to the requirements numerical value.
% Gives us a 'weighting' to experience. Multiple weighting depending on scale
0.5::underprepared_incident(X, Layer) :-
    character(X), whistle_rank(X, CharRank), rank_experience(CharRank, CN),
    layer_requirement(Layer, ReqRank), rank_experience(ReqRank, RN),
    CN < RN.

0.3::overprepared_incident(X, Layer) :-
    character(X), whistle_rank(X, CharRank), rank_experience(CharRank, CN),
    layer_requirement(Layer, ReqRank), rank_experience(ReqRank, RN),
    CN > RN.

% Main query. Chance of surviving a layer depends on the incident in the layer, 
% its probability of being fatal, and the weighting 
% uses \+ to formulate 1 - probability. 1 means to survive and chances reduce as danger increases.
% Survives_layer to be true we have the formula
%
% A = The probability a character is under rank. We calculate 1 - P(A) as being underrank reduces chances
% B = If an incident in a layer occurs, we also subtract this from the survival chances
% C = We actually want to add this.
% B and C is coupled, as only 1 can occur at a time. either a negative incident or character is strong.
%
% We can see we have a relation like:
% S = ¬A ∧ (¬B ∨ C)
% We know in this case calculating the inverse would be easier. Using De Morgans Law
% ¬S = A ∨ ¬(¬B ∨ C)
% ¬S = A ∨ (B ∧ ¬C)
% P(¬S) = 1 - P(S) = 1 - (1 - P(A))[1 - (P(B)(1 - P(C))]
% P(S) = (1 - P(A))[1 - P(B)(1 - P(C))]
% P(C) has an inverse relation with P(B) meaning it reduces its effects when it occurs. 

survives_layer(X, Layer) :-
    \+ underprepared_incident(X, Layer),
    (\+ incident_in_layer(Layer) ; overprepared_incident(X, Layer)).


% Queries
% Incident danger -> more dangerous beast has less survival chance 
query(incident(orb_piercer)).               %0.255
query(incident(hammerbeak)).                %0.015

% Comparison of 2 characters. in layer 4 
% bondrewd white whistle > bidos black whistle > Regs, red whistle
% Layer 5 creature less dangerous -> higher survival of that layer.
query(survives_layer(bondrewd, layer_1)).   %0.989
query(survives_layer(bondrewd, layer_4)).   %0.687

query(survives_layer(reg, layer_1)).        %0.985  
query(survives_layer(reg, layer_4)).        %0.277
query(survives_layer(reg, layer_5)).        %0.493

query(survives_layer(bido, layer_4)).       %0.553

% Conditional, when whistle rank < layer rank, we have a 50% probability weighting
query(underprepared_incident(bido, layer_4)).   %0
query(underprepared_incident(reg, layer_4)).    %0.5
query(underprepared_incident(reg, layer_5)).    %0.5

% Conditional when a whistle rank is over the layer rank.
query(overprepared_incident(bido, layer_4)).    %0
query(overprepared_incident(bondrewd, layer_4)).%0.3

% This is just a confirmaiton of my formula
% P(S) = (1 - P(A))[1 - P(B)*(1 - P(C))]

% P(A) = underprepared_incident. Bido ahs a greater rank, return 0
% P(B) = incident in layer. CrimsonSplit jaw is encounter at a 0.3 probability
% P(B) = Encounter (0.30) and fatal rate (Deadly 0.60) = 0.18
% P(C) = Bido is over prepared -> return 0.30

% P(S) = (1 - 0)*[(1 - (0.18)*(1-0.30)
% P(S) = 1 - (0.18)(0.70)
% P(S) = 1 - 0.126 
% P(S) =. 0.874
query(survives_layer(bido, layer_3)).           % 0.874
query(underprepared_incident(bido, layer_3)).   % 0
query(incident_in_layer(layer_3)).              % 0.18
query(overprepared_incident(bido, layer_3)).    % 0.3
