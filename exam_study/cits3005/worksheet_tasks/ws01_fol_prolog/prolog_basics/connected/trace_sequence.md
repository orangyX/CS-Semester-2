# E4
```
Call: nearby(oxford_circus, charing_cross)
 Call: connected(oxford_circus, charing_cross, _)
 Fail: connected(oxford_circus, charing_cross, _)
Redo: nearby(oxford_circus, charing_cross)
 Call: connected(oxford_circus, _Z, _L)
 Exit: connected(oxford_circus, tottenham_court_road, central)
 Call: connected(tottenham_court_road, charing_cross, central)
 Fail: connected(tottenham_court_road, charing_cross, central)
 Redo: connected(oxford_circus, _Z, _L)
 Exit: connected(oxford_circus, piccadilly_circus, bakerloo)
 Call: connected(piccadilly_circus, charing_cross, bakerloo)
 Exit: connected(piccadilly_circus, charing_cross, bakerloo)
Exit: nearby(oxford_circus, charing_cross)
true.
```