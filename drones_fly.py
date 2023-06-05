from math import dist

# calculate distance between stops
def distanza(x1,x2):
    distanza = dist(x1, x2)
    return distanza


# read coordinate of stops
with open("stop.py","r",encoding="utf-8") as file:
    point = []
    for riga in file:
        punt = riga[0]
        coord =[int(riga[2]),int(riga[4])]
        stop = punt, coord
        point.append(stop)

    file.close()

# read drone route
drone_set= []
with open("drones.txt","r", encoding="utf-8") as dro:
    for riga in dro:
        el1=000
        el2=000
        drone= riga[0:3]
        percorso = riga[4:].rstrip()
        percorso = percorso.split(",")
        distanze = []
        number_of_stop = 0
        for el in percorso:
            number_of_stop = number_of_stop + 1
            for stop in point:
                if el in stop and el1 != 000:
                    el2 = stop[1]
                    d = distanza(el1, el2)
                    distanze.append(d)
                    el1 = el2
                    el2 = 000
                if el in stop:
                    el1 = stop[1]

        distanza_totale = sum(distanze)
        battery_need = distanza_totale / number_of_stop
        drone_plane = {"drone": drone,
                       "total distance": distanza_totale,
                       "number of stops": number_of_stop,
                       "battery capacity": battery_need
                       }
        drone_set.append(drone_plane)
#  calculates which drone needs the most energy and print the desired characteristics of it

highest_capacity = float(0)
for drone_plane in drone_set:
    high = drone_plane.get("battery capacity")
    if high > highest_capacity:
        highest_capacity = high
        name = drone_plane.get("drone")
        distance = drone_plane.get("total distance")
        num = drone_plane.get("number of stops")
print(f"highest battery capacity for {name}")
print(f"total distance:{distance}")
print(f"number of stops: {num}")

dro.close()









