#def road(start, end, houses):
  #x = list(range(start, end+1))
 # stations = []
  #for i in houses:
   # min = i-4
    #max = i + 4
    #if len(stations) == 0:
    #  stations.append(houses[0] + 4)
    #for j in stations:
    #  print(min)
    #  print(max)
    #  print(i)
    #  print(j)
    #  if(min == j):
    #    return
    #  else:
    #    print("it added")
    #    stations.append(i+4)
#
#    return stations

import random

def makehouses():
    houses = []

    for a in range(0, 10):
        x = random.randint(0, 100)
        houses.append(x)
        houses.sort()

    return houses

def road():
    houses = makehouses()
    stations = []
    print(houses)
    place = 0
    for i in range(0, len(houses)):
        if houses[i] - houses[place] > 8:
            stations.append(houses[place] + 4)
            place = i
    a = len(stations)
    print(stations)
    return a
print(road())
