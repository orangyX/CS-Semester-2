defeat(henryVII, richardIII).
oldestson(henryVIII, henryVII).
king(richardIII).
king(Y) :- oldestson(Y, X), king(X).
king(Y) :- defeat(Y, X), king(X).