marks = [[0 for j in range(30)] for i in range(3)]

max_stud = [0,0,0]

for i in range(3):

    max_stud[i] = int(input(f"\n\tEnter Maximum students in class {i+1} : "))

    print()

    if not 0 < max_stud[i] < 31: 
        print("\tStudents in  a class can only be between 1 to 30")
        exit(0)

    for j in range(max_stud[i]):
        marks[i][j] = int(input(f"\tEnter marks of student {j+1} of class {i+1} : "))

for i in range(3):
    for j in range(max_stud[i]):
        print(f"\tMarks of Student {j+1} of class {i+1} is : {marks[i][j]}") 

