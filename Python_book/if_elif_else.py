class_,rank_str= {
    1: (AceCard, 'A'),
    11: FaceCard, 12: FaceCard, 13: FaceCard
}.get(rank, NumberCard)
rank_str= {1:'A', 11:'J', 12:'Q', 13:'K'}.get(rank,str(rank))
return class_( rank_str, suit )