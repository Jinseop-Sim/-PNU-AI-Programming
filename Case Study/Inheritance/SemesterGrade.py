import student

def obtainListOfStudents():
    listOfStudents = []
    flag = 'Y'
    while flag == 'Y':
        name = input("Enter Student's name : ")
        midterm = float(input("Enter grade on midterm : "))
        final = float(input("Enter grade on final : "))
        category = input("Enter category (LG or PF) : ")
        if category.upper() == "LG":
            st = student.LGStudent(name, midterm, final)
        else:
            st = student.PFStudent(name, midterm, final)
        listOfStudents.append(st)
        flag = input("Do you want to continue (Y/N)? ")
        flag = flag.upper()
    return listOfStudents

def displayResults(listOfStudents):
    print("\nNAME\tGRADE\tSTATUS")
    listOfStudents.sort(key=lambda x: x.getName())
    for pupil in listOfStudents:
        print(pupil)

listOfStudents = obtainListOfStudents()
displayResults(listOfStudents)
