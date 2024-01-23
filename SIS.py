import json

#Simple Student Information System using Python and JSON 


#Create menu
def printMenu(): 
    print("-MENU-")
    print("0. EXIT")
    print("1. GET ALL STUDENTS")
    print("2. GET ONE STUDENT")
    print("3. ADD A STUDENT")
    print("4. EDIT A STUDENT")
    print("5. DELETE A STUDENT")
    print("")
    
#Exit program
def exit():
    return False

#Get all students
def getAll():
    for x in studentList:
        print("")
        for key, value in x.items():
            print(key, value)
            
#Get one student
def getOne():
    val=input("What id do you want? (Range: 0-"+str(len(studentList))+")\nInput:")
    for x in studentList:
        print("")
        for key, value in x.items():
            if key=='id' and value == val:
                for key, value in x.items():
                    print(key, value)
            else:
                print("This ID does not exist in the system. Try Again")
                getOne()

#Add a new student
def add():
    id = len(studentList)+1
    firstName = input("What is the first name?\nInput:")
    lastName = input("What is the last name?\nInput:")
    age = input("What is the age?\nInput:")
    gender = input("What is the gender?\nInput:")
    newStudent = {"id":str(id),
              "first_name":firstName,
              "last_name":lastName,
              "age":age,
              "gender":gender}
    studentList.append(newStudent)
    with open("SIS.json", "w") as writeFile:
        fileContent = json.dumps(studentList, indent=4)
        writeFile.write(fileContent)
    
#Edit existing student
def edit():
    chooseID = input("Which ID would you like to edit? (Range: 0-"+str(len(studentList))+")\nInput:")
    firstName = input("What is the new first name?\nInput:")
    lastName = input("What is the new last name?\nInput:")
    age = input("What is the new age?\nInput:")
    gender = input("What is the new gender?\nInput:")
    newStudent = {"id":str(chooseID),
              "first_name":firstName,
              "last_name":lastName,
              "age":age,
              "gender":gender}
    studentList[int(chooseID)-1]=newStudent
    with open("SIS.json", "w") as writeFile:
        fileContent = json.dumps(studentList, indent=4)
        writeFile.write(fileContent)
    
#Delete existing student
def delete():
    chooseID = input("Which ID would you like to delete? (Range: 0-"+str(len(studentList))+")\nInput:")
    studentList.pop(int(chooseID)-1)
    with open("SIS.json", "w") as writeFile:
        fileContent = json.dumps(studentList, indent=4)
        writeFile.write(fileContent)
    

#Load data from file
with open("SIS.json", "r") as readFile:
    studentList=json.load(readFile)

#Main program
print("Welcome to SIS\n")
run = True
while run == True:
    printMenu()
    action = input("What would you like to do?\nInput:")
    if action == '0':
        run = exit()
    else:
        if action == '1':
            getAll()
            print("")
        elif action == '2':
            getOne()
            print("")
        elif action == '3':
            add()
            print("")
        elif action == '4':
            edit()
            print("")
        elif action == '5':
            delete()
            print("")