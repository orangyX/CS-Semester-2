% Justin Power | 24174788

% Facts; connected components
% Mandurah line
connected(mandurah, lakelands, mandurah_line).
connected(lakelands, warnbro, mandurah_line).
connected(warnbro, rockingham, mandurah_line).
connected(rockingham, wellard, mandurah_line).
connected(wellard, kwinana, mandurah_line).
connected(kwinana, aubin_grove, mandurah_line).
connected(aubin_grove, cockburn_central, mandurah_line).
connected(cockburn_central, murdoch, mandurah_line).
connected(murdoch, bull_creek, mandurah_line).
connected(bull_creek, canning_bridge, mandurah_line).
connected(canning_bridge, elizabeth_quay, mandurah_line).

% Airport line
connected(high_wycombe, airport_central, airport_line).
connected(airport_central, redcliffe, airport_line).
connected(redcliffe, bayswater, airport_line).
connected(bayswater, meltham, airport_line).
connected(meltham, maylands, airport_line).
connected(maylands, mt_lawley, airport_line).
connected(mt_lawley, east_perth, airport_line).
connected(east_perth, claisebrook, airport_line).
connected(claisebrook, mciver, airport_line).
connected(mciver, perth, airport_line).

% Mandurah line closures
closed(lakelands).
closed(warnbro).

% Airport line closures
closed(meltham).

% Rules
% Check if a station S lies on line L
% Two facts to be verified: S can sit in 2 positions of the fact
% ---------------------------------------------------------------------------------------------------------------------------------------
station_on_line(S, L) :-
    connected(_, S, L); % _ means, we do not care about the variable, it is never used; this is just to avoid singleton variable warnings
    connected(S, _, L).

% This has more moving parts; need some way to find out that S lies before T, on line L
% First case: S, T, L lie within the same fact, so  we know for certain that S occurs before T
% ---------------------------------------------------------------------------------------------------------------------------------------
before_on_line(S, T, L) :-
    connected(S, T, L).

before_on_line(S, N, L) :-
    connected(N, _, L).
    
% Second case: S, T do not lie within the same fact; we need a way to deduce across all facts
% ---------------------------------------------------------------------------------------------------------------------------------------
before_on_line(S, T, L) :-
    connected(S, T, L).
    % Check, are _ and T connected to the same fact? recurse if not, else return true
before_on_line(S, T, L) :-
    connected(S, T, L),
    before_on_line(T, N, L).

% Check if station S is a terminal
% Case 1: _ is unable to unify with anything before S
% ---------------------------------------------------------------------------------------------------------------------------------------
terminal(S, L) :-
    station_on_line(S, L),
    \+ connected(_, S, L). % Must have that _ is unable to unify with anything before S

% Case 2: _ is unable to unify with anything after S
% ---------------------------------------------------------------------------------------------------------------------------------------
terminal(S, L) :-
    station_on_line(S, L),
    \+ connected(S, _, L). % Must have that _ is unable to unify with anything after S

% Route -> denoted by a list of stations; does it go from station S to T, on line L, w/ no closed stations?
% Base case; if resident within the same connected fact, and none are closed, then a route exists; terminates recursion
% ---------------------------------------------------------------------------------------------------------------------------------------
route_on_line(S, T, L, [S, T]) :-
    connected(S, T, L), % All must be connected
    \+ closed(S), % Both must be non-closed
    \+ closed(T).

% Other case; if not in the same connected component; recursively collect stations into R; [S|R] decares S as the head of R
route_on_line(S, T, L, [S|R]) :-
    % Check if S is connected to a successor station, X
    connected(S, X, L),
    % If closed, the route is invalidated
    \+ closed(S),
    % Recurse, call the successor station, supplying T, on line with L, with the acquired route so far
    route_on_line(X, T, L, R). % If the above conditions are true, R is bound to the route from X to T