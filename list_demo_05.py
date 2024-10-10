# adding elements in the list
listStudents = []
size = int(input("hoe many students you want  to store in list: "))
i = 1
stuName =""
while i <= size:
    stuName =input("enter student name:")
    listStudents.append(stuName)
    print(stuName,"Add in the list")
    i=i+1
    print("student names in the list are: ")
    for x in listStudents:
        print(x)
