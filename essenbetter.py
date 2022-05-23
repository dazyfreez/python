print("das ist ein essensplaner")
essen =  ["spagetti", "burger", "lasagne", "bestellen", "eier"]
x = int(input("für wie viel tage wollen sie planen"))
print("wollen sie das menü öffen")
print("ja oder nein")
eingabe = input()
if eingabe == "ja":
    print("1 führ eine andere reinfolge aus")
    print("2 führ einen neuen eintrag hinzu")
    print("3 lösche einen eintrag")
    print("4 ändere einen eintrag")
    print("5 speichere die ergebnisse in einer datei")
    print("6 beenden")
    eingabe = int(input())
    if eingabe == 1:
        essen.reverse()
        print(essen)
    elif eingabe == 2:
        neu = input("was möchten sie hinzufügen")
        essen.append(neu)
        print(essen)
    elif eingabe == 3:
        löschen = input("was möchten sie löschen")
        essen.remove(löschen)
        print(essen)
    elif eingabe == 4:
        ändern = input("was möchten sie ändern")
        essen.remove(ändern)
        neu = input("was möchten sie ändern")
        essen.append(neu)
        print(essen)
    elif eingabe == 5:
        datei = open("essen.txt", "w")
        datei.write(str(essen))
        datei.close()
    elif eingabe == 6:
        print("beenden")
    else:
        print("falsche eingabe")
else:
    print(essen)