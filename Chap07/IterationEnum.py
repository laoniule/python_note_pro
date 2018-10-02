from enum import Enum

class Color(Enum):
    red=1
    green=2
    yellow=3

print(Color.red)
print(Color(1))
print(Color['red'])


print([c for c in Color])


#for c in Color:
#    print(c)
