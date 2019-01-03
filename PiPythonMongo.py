import pymongo

from pymongo import MongoClient
con = MongoClient()


db = con.pymongo_testRon

people = db.people
people.insert({'name': 'Ron', 'Food': 'cheese'})
people.insert({'name': 'Ron2', 'Food': 'pizza','Location': 'NL'})
people.insert({'name': 'Ron3', 'Food': 'cheese'})

overview = people.find()

print('Insert & Find Test')
for person in overview:
    print (person)

selection = people.find({'Food':'cheese'})

print('Food is kaas')
for person in selection:
    print (person)

print('Update record test - vervang pizza door eggs')

person = people.find_one({'Food':'pizza'})
person['Food'] = 'eggs'
people.save(person)

# for person in people.find({'Food':'eggs'}):
#    print (person)


for person in people.find({'Food':'cheese'}):
        people.remove(person)

print('Result : alleen de eggs')
overview_Final = people.find()
for person in overview_Final:
    print (person)
