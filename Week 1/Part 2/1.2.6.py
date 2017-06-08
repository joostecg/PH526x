ids = set()
ids = set([1,2,4,6,7,8,9])
len(ids)
ids.add(10)
ids
ids.add(2)  #sets do not hold duplicate values
ids

ids.pop()
ids
ids.pop()
ids

ids = set(range(10))
ids
males = set([1,3,5,6,7])
females = ids - males
type(females)
females
males

everyone = males | females

everyone & set([1,2,3])     # provides intersection of two sets

word = "antidisestablishmentarism"
letters = set(word)
len(letters)
