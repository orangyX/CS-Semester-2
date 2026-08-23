start :-
    writeln("Guess between 1, 100"),
    random_between(1, 100, Number),
    loop(Number).

% Fetch the guess
loop(Secret) :-
    write("Guess: "),
    read(Guess),
    check_guess(Guess, Secret).

% Case 1: Guess == Secret
check_guess(Guess, Secret) :-
    Guess == Secret,
    writeln("Correct").

% Case 2: Guess != Secret, and Guess < Secret
check_guess(Guess, Secret) :-
    Guess < Secret,
    writeln("Higher"),
    loop(Secret).

% Case 3; Guess != Secret, and Guess > Secret
check_guess(Guess, Secret) :-
    Guess > Secret,
    writeln("Lower"),
    loop(Secret).
