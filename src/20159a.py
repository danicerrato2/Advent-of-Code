import sys

def calculate_route(to_visit, trips, last_visited, shortest, actual) -> int:
    if len(to_visit) == 1:
        if actual < shortest:
            shortest = actual
        return shortest
    
    aux_to_visit = to_visit.copy()
    aux_to_visit.remove(last_visited)
    aux_trips = trips.copy()
    aux_actual = actual
    for city in aux_to_visit:
        for trip in trips:
            if last_visited in trip:
                if city in trip:
                    aux_actual += trip[2]
                aux_trips.remove(trip)
        shortest = calculate_route(aux_to_visit, aux_trips, city, shortest, aux_actual)
        aux_trips = trips.copy()
        aux_actual = actual
    return shortest

if __name__ == '__main__':

    if len(sys.argv) != 2:
        sys.exit("Error: Faltan argumentos")
    
    file_in = open(sys.argv[1], 'r')
    if file_in is None:
        sys.exit("Error: Apertura de fichero fallida")

    trips = []
    cities = set()
    shortest = 0
    line = file_in.readline()[:-1]
    while line != '':
        splited = line.split(' = ')
        splited[1] = int(splited[1])
        if splited[1] > shortest:
            shortest = splited[1]
        splited[0] = splited[0].split(' to ')
        trips.append([splited[0][0], splited[0][1], splited[1]])
        cities.add(splited[0][0])
        cities.add(splited[0][1])

        line = file_in.readline()[:-1]

    cities = list(cities)
    cities.sort()
    shortest *= len(cities)
    aux_cities = cities.copy()
    aux_trips = trips.copy()
    for city in cities:
        aux_cities.remove(city)
        for dest in aux_cities:
            for trip in trips:
                if city in trip:
                    if dest in trip:
                        actual = trip[2]
                    aux_trips.remove(trip)
            shortest = calculate_route(aux_cities, aux_trips, dest, shortest, actual)
            aux_trips = trips.copy()
        aux_cities = cities.copy()
    
    print("The shortest route costs: " + str(shortest))
