import random
print("das ist ein RUSSISCHE ROULETTE SPIEL")  # hier wird das spiel gestartet
print("wollen sie das spiel starten")       # hier wird das spiel gestartet
print("ja oder nein")   
eingabe = input()
if eingabe == "ja":
    print("sie können zwischen 6 zahlen whälen")
    print("wollen sie das spiel starten bedenken sie ihr leben hängt an ihrer wahl ab")
    print(random.randint(0, 6))
