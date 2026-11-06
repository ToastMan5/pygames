def show_array(array):
    print("           ")
    for i in range():
        print(row)


def make_array(rows,collumns,fill):
    array = []
    for i in range(rows):
        array.append([])
        for j in range(collumns):
            array[i].append(fill)
    return array

def fill_array(array,fill):
    for i in range(len(array)):
        array[i][0] = fill
        for j in range(len(array[i])):
            array[i][j] = fill
    return array


def parse_position(string,selector):
    for i in range(len(string)):
        if string[i] == ",":
            if selector == 0:
                return int(string[:i])
            elif selector == 1:
                return int(string[i+1:])

park = make_array(6,10,"")
#show_array(park)
option = 0
while option !=  5:
    print("Options:")
    print("  1: Set all spaces in car park to \"empty\"")
    print("  2: Park a car")
    print("  3: Remove a car")
    print("  4: Display car park in grid form")
    print("  5: Quit")
    option = int(input("Enter option: "))
    if option == 1:
        fill_array(park, "empty")
    if option == 2:
        registration = input("Enter your car registration number: ")
        position_input = input("Enter row/collumn of place where you want to park your car (eg. \"1,5\"): ")
        position_row = parse_position(position_input,0)-1
        position_collumn = parse_position(position_input,1)-1
        park[position_row][position_collumn] = registration
    if option == 3:
        registration = input("Enter your car registration number: ")
        for i in range(len(park)):
            for j in range(len(park[i])):
                if park[i][j] == registration:
                    park[i][j] = "empty"
        count = 0
        for i in range(len(park)): #verify its removed
            for j in range(len(park[i])):
                if park[i][j] == registration:
                    count += 1
        if count == 0:
            print(f"Removal of car with {registration = } - success!")
        else: print(f"Removal of car with {registration = } - failiure!")
    if option == 4:
        show_array(park)
    if option == 5:
        option = 5

