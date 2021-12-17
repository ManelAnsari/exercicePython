#Exercice 1.2
X={"a","b","c","d"}
Y={"s","b","d"}
print(X)
print(Y)
print("appartenane de l'élement 'c' a X",X.__contains__("c"))
print("appartenane de l'élement 'a' a Y",Y.__contains__("a"))
print("X-Y = ",X-Y)
print("Y-X = ",Y-X)
print("X union Y = ",X.union(Y))
print("X intersaction Y = ",X.intersection(Y))
