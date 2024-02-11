import json
StudentNumber = int(input("How many student do you want to add to the list:"))
for i in range(0, StudentNumber):
    ID = input("Enter your ID:")
    Name = input("Enter your name:")
    Age = input("Enter your age: ")
    Email = input("Enter your email: ")
    # number of elements as input
    n = 3
    ListNumbers = []
    # iterating till the range
    for i in range(0, n):
        Numbers = int(input(f'Enter {n} numbers:'))
        # adding the element
        ListNumbers.append(Numbers)
    UserData = {
        "id": ID,
        "name": Name,
        "age": Age,
        "email": Email,
        "Numbers": ListNumbers
    }
    StudentList = {
        "students": [UserData]
    }
    try:
        with open('UserData.json', 'r') as file:
            data = json.load(file)
    except FileNotFoundError:
        # If the file doesn't exist, initialize an empty list
        data = {"students": []}
        
    # Add the new student to the list
    data["students"].append(UserData)
    with open('UserData.json', 'w') as f:
        json.dump(data, f, )

print("___")

