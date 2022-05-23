print("hiermit können Sie eine binäre Zahl in eine dezimale umwandeln und umgekehrt")
x = int(input("welche zahl möchten sie suchen"))
print(bin(x))   # bin() gibt die binäre Zahl als String zurück
print(int(bin(x), 2))   # int() wandelt einen String in eine Zahl um
