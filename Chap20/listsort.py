from operator import itemgetter,attrgetter 
import datetime



class Person(object):
    def __init__(self,name,birthday,height):
        self.name=name
        self.birthday=birthday
        self.height=height

    def __repr__(self):
        return self.name


"""
l=[Person("John Cena",datetime.date(1992,9,12),175),
   Person("Chuck Norris",datetime.date(1999,3,18),188),
   Person("Joe Skeet",datetime.date(2000,12,12),168)]

l.sort(key=lambda item: item.name)
print(l)

l.sort(key=lambda item: item.height)
print(l)

people = [{'name':"John Cena", 'age':20,'salary':2000},
        {'name':"Chuck Norris", 'age':19, 'salary':5000},
        {'name':"Joe Skeet", 'age':30, 'salary':3000}]

by_age=itemgetter('age')
by_salary=itemgetter('salary')

people.sort(key=by_age)
print(people)
people.sort(key=by_salary)
print(people)
"""

persons = [Person("John Cena", datetime.date(1992, 9, 12), 175),
     Person("Chuck Norris", datetime.date(1999, 3, 18), 188),
     Person("Joe Skeet", datetime.date(2000, 12, 12), 168)]

persons.sort(key=attrgetter("name"))
print(persons)
by_birthday=attrgetter("birthdaylst=[1]")
persons.sort(key=by_birthday)
print(persons)
