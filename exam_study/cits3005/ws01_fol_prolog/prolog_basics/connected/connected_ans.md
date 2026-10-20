# E3

## a. question
Give every answer, in order, to ```?- connected(green_park, X, L).```

### E3(a) answer
| Step | X | L |
| :--- | :--- | :--- |
| 1 | X = charing_cross | L = jubilee |
| 2 | X = picadilly_circus | L = picadilly | 
| 3 | X = oxford_circus | L = victoria |

The above denotes every possible fact related to ```green_park```.

## b. question
Slide 32 says we "can derive that Bond Street and Charing Cross are not nearby". What does ```?- nearby(bond_street, charing_cross)```. actually return? Name the clause and the facts used.

### E3(b) answer
```?- nearby(bond_street, charing_cross)``` steps:
X and Y get bond_street and charing_cross. In accordance with the rules, Z and L are missing:
```
nearby(X,Y) :- connected(X,Y,_L).
nearby(X,Y) :- connected(X,Z,L), connected(Z,Y,L).
```

| Clausal step | Fact | Fact exists |
| :--- | :--- | :--- |
| 1 | connected(bond_street, charing_cross, _) | False |
| 2 | connected(bond_street, Z, L), connected(Z, charing_cross, L) | False |

Attempt:
```
Let Z = oxford_circus, L = central
    yield connected(oxford_circus, charing_cross, central)
Not exists. try other route

Z = green_park, L = jubilee
    yield connected(green_park, charing_cross, jubilee)
Not exists. return false.
```

## c. question
Fix (c) by making adjacency symmetric. Explain why adding connected(X,Y,L) :- connected(Y,X,L). is the wrong fix.

### E3(c) answer
The following:
```
connected(X,Y,L) :- connected(Y,X,L).
```

Yields an infinite loop; since prolog backtracks on a falsity, it checks connected(X, Y, L), if that is not true, it then checks connected(Y, X, L); if that is also untrue, it then checks connected(X, Y, L), and does the same forever.

The fix:
```
link(X, Y, L) :- connected(X, Y, L).
link(X, Y, L) :- connected(Y, X, L).
```

Where the clause never calls itself; on a falsity, it returns false. On a truth, it returns true; it never has the mechanism to call itself infinitely with no call in either body.

## d. question
Slide 32: why can't this knowledge base tell us that Subiaco and Leederville are not nearby?

### E3(d) answer
connected(_ | subiaco, subiaco | _, _) and connected(_ | leederville, leederville | _, _) literally do not exist in the knowledge base; prolog cannot prove that something holds if it does not exist.

Under CWA, it will return false.