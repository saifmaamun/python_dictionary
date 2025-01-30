# Students = {
#     'Jonny': {
#         'Rollno': 10,
#         'Name': 'Jonny',
#         'Dept_name': 'EEE'
#     },
#     'Sam': {
#         'Rollno': 36,
#         'Name': 'Sam',
#         'Dept_name': 'MECH'
#     },
#     'Peter': {
#         'Rollno': 45,
#         'Name': 'Peter',
#         'Dept_name': 'CS'
#     },
#     'Tim': {
#         'Rollno': 17,
#         'Name': 'Tim',
#         'Dept_name': 'IT'
#     },
#     'Mark': {
#         'Rollno': 38,
#         'Name': 'Mark',
#         'Dept_name': 'ECE'
#     }
# }

Students = {}

for i in range(4):
    name=input('enter name: ')
    roll = input('enter roll: ')
    dept= input('enter dept name: ')
    info={
        'Rollno': roll,
        'Name': name.capitalize(),
        'Dept_name': dept.upper()
    }
    Students.setdefault(name.capitalize(),info)

print(Students)