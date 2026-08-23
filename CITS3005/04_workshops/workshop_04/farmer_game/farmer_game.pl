% Helpers for opposites
opposite(west, east).
opposite(east, west).

% Unsafe state; Wolf + Goat alone
unsafe(Farmer, Wolf, Goat, Cabbage) :-
    Wolf = Goat,
    Farmer \= Wolf;
    Goat = Cabbage,
    Farmer \= Goat.

% Movement for farmer
move(state(Farmer, W, G, C), state(Farmer2, W, G, C)) :-
    % Have no idea to tell where Farmer is, so we attach both variables! it will yield the matched case in the above opposite helper
    opposite(Farmer, Farmer2).

move(state(Farmer, Wolf, G, C), state(Farmer2, Wolf2, G, C)) :-
    Farmer = Wolf,
    opposite(Farmer, Farmer2),
    opposite(Wolf, Wolf2).

move(state(Farmer, W, Goat, C), state(Farmer2, W, Goat2, C)) :-
    Farmer = Goat,
    opposite(Farmer, Farmer2),
    opposite(Goat, Goat2).

move(state(Farmer, W, G, Cabbage), state(Farmer2, W, G, Cabbage2)) :-
    Farmer = Cabbage,
    opposite(Farmer, Farmer2),
    opposite(Cabbage, Cabbage2).

% Goal predicate
goal(state(east, east, east, east)).

solve(CurrentState, NextState, AllStates) :-
    goal(CurrentState),
    writeln("Success!");
    \+goal(CurrentState),
    \+unsafe(CurrentState),
    AllStates
    