database = {'Water': 'Base Element', 'Fire': 'Base Element', 'Earth': 'Base Element', 'Wind': 'Base Element', 'Smoke': 'Fire + Wind', 'Lake': 'Water + Water', 'Steam': 'Water + Fire', 'Plant': 'Earth + Water', 'Fog': 'Smoke + Lake', 'Engine': 'Steam + Fire', 'Mud': 'Earth + Steam', 'Car': 'Engine + Plant', 'Rally': 'Mud + Car', 'Race': 'Engine + Rally', 'Volcano': 'Fire + Fire', 'Island': 'Volcano + Lake', 'Ocean': 'Water + Lake', 'Fish': 'Water + Ocean', 'Hawaii': 'Volcano + Island', 'Poke': 'Fish + Hawaii', 'Pokemon': 'Island + Poke', 'Fjord': 'Lake + Mountain', 'Cloud': 'Water + Steam', 'Whale': 'Water + Fjord', 'Electricity': 'Steam + Lightning', 'Lightning': 'Cloud + Fire', 'Pikachu': 'Electricity + Whale', 'Mountain': 'Earth + Earth', 
'Lava': 'Fire + Volcano', 'Eruption': 'Volcano + Lava', 'Mountain_Range': 'Mountain + Mountain', 'Yellowstone': 'Mountain_Range + Volcano', 'Supervolcano': 'Yellowstone + Volcano'}  
global searched
searched = []
key = 0

def searchElement(a) :
    global searched
    try:
        if database[a] != "Base Element":
            print(f"{a} = {database[a]}")
            searched.append(a)
            key = database[a].split()
            if key[0] not in searched:
                searchElement(key[0])
            if key[2] not in searched:
                searchElement(key[2])
    except:
        #print("Sorry, this is not in the database yet. Maybe add in some things?") Will implement this soon
        for i in range(1):
            continue
    
    

def addElement(a, b) :
    database[a] = b

while True:
    print("What would you like to do?")
    print("1) Add into database")
    print("2) Find word and crafts in database")
    #print("3) Search for words using letters & numbers in database")
    home = input("Type the number:")
    if home == "1":
        home = input("Name of Element: ")
        for i in database.items():
            if i[0] == home:
                print("Sorry, this word aready exists. Please try another word.")
                key = 1
        if key == 0:
            print("If element has a space, add a underline instead. Eg. Mountain_Range")
            receive = input("First element of the combination: ")
            received = input("Second element of the combination: ")
            addElement(home, (receive + " + " + received))
        key = 0
    elif home == "2":
        home = input("Name of Element: ")
        print("Remember, the crafts may not usually be in order. I will fix this soon, I promise.")
        print()
        searchElement(home)
        searched = []
    elif home == "3":
        print(database)
    print("---------------------------------------")
    print()

