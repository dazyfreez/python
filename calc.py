print ("das ist ein rechner")
print ("wollen sie addieren oder subrtahiren?")
print ("1. addieren")
print ("2. subtrahieren")
print ("3. multiplizieren")
print ("4. dividieren")
print ("5. hochrechnen")
print ("6. wurzel berechnen")
print ("7. quadrat berechnen")
print ("8. programm beenden")
x = input("bitte wählen sie eine option: ")
if x == "1":
    print ("addieren")
    a = int(input("bitte geben sie eine zahl ein: "))
    b = int(input("bitte geben sie eine zahl ein: "))
    print (a + b)
elif x == "2":
    print ("subtrahieren")
    a = int(input("bitte geben sie eine zahl ein: "))
    b = int(input("bitte geben sie eine zahl ein: "))
    print (a - b)
elif x == "3":
    print ("multiplizieren")
    a = int(input("bitte geben sie eine zahl ein: "))
    b = int(input("bitte geben sie eine zahl ein: "))
    print (a * b)
elif x == "4":
    print ("dividieren")
    a = int(input("bitte geben sie eine zahl ein: "))
    b = int(input("bitte geben sie eine zahl ein: "))
    print (a / b)
elif x == "5":
    print ("hochrechnen")
    a = int(input("bitte geben sie eine zahl ein: "))
    b = int(input("bitte geben sie eine zahl ein: "))
    print (a ** b)
elif x == "6":
    print ("wurzel berechnen")
    a = int(input("bitte geben sie eine zahl ein: "))
    print (a ** 0.5)
elif x == "7":
    print ("quadrat berechnen")
    a = int(input("bitte geben sie eine zahl ein: "))
    print (a ** 2)
elif x == "8":
    print ("programm beenden")
