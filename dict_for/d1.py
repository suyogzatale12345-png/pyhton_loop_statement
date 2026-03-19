student = {
    "name": "Suyog",
    "age": 21,
    "course": "IT"
}

keyName = 'age'

print(student[keyName])
for stud in student:
    print(f"stud = {stud}, type of stud = {type(stud)} keyVaue ={student.get(stud)}")