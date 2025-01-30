birthdays = {
    'Sachin': '03/14/2003',
'Carl': '02/20/2001',
'Razi': '12/10/2010',
'Haydar': '06/14/2020',
'Khan': '08/21/2005',
'Donald': '01/08/2006',
'Modi': '09/01/2013',
'Rohan': '04/26/2023',
}
name = input("enter your name:").capitalize()

# for k in birthdays:
#     if name in birthdays:
#         print(name)
if name in birthdays:
    print("{}'s birthday is {}" .format(name, birthdays[name]))
else:
    print("{} is not in database".format(name))