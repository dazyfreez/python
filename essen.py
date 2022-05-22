print("das ist ein essensplaner")
essen =  ["spagetti", "burger", "lasagne", "bestellen", "eier"]
x = int(input("für wie viel tage wollen sie planen"))
i = 0
while i < x:
    print(essen[i])
    i = i + 1
print("wollen sie die ergebnisse in einer anderen reihenfolge anzeigen")
print("ja oder nein")
eingabe = input()
if eingabe == "ja":
    essen.reverse()
    print(essen)
else:
    print(essen)
print("wollen sie einen neuen eintrag hinzufügen")
print("ja oder nein")
eingabe = input()
if eingabe == "ja":
    neu = input("was möchten sie hinzufügen")
    essen.append(neu)
    print(essen)
else:
    print(essen)
print("wollen sie einen eintrag löschen")
print("ja oder nein")
eingabe = input()
if eingabe == "ja":
    löschen = input("was möchten sie löschen")
    essen.remove(löschen)
    print(essen)
else:
    print(essen)
print("wollen sie einen eintrag ändern")
print("ja oder nein")
eingabe = input()
if eingabe == "ja":
    print(essen)
    ändern = input("was möchten sie ändern")
    essen.remove(ändern)
    neu = input("was möchten sie ändern")
    essen.append(neu)
    print(essen)
else:
    print(essen)
print("wollen sie die ergebnisse in einer datei speichern")


