print("das ist ein binarysearch algorithmus")
liste = [1,2,3,4,5,6,7,8,9,10]
print (liste)
x = int(input("welche zahl möchten sie suchen"))
i = 0
while i < len(liste):
    if liste[i] == x:
        print("gefunden")
        break
    elif liste[i] > x:
        print("nicht gefunden")
        break
    i = i + 1