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