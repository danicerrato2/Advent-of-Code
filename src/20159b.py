import sys

def calculate_route(to_visit, trips, last_visited, longest, actual) -> int:
    if len(to_visit) == 1:
        if actual > longest:
            longest = actual
        return longest
    
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
        longest = calculate_route(aux_to_visit, aux_trips, city, longest, aux_actual)
        aux_trips = trips.copy()
        aux_actual = actual
    return longest

if __name__ == '__main__':

    if len(sys.argv) != 2:
        sys.exit("Error: Faltan argumentos")
    
    file_in = open(sys.argv[1], 'r')
    if file_in is None:
        sys.exit("Error: Apertura de fichero fallida")

    trips = []
    cities = set()
    longest = 0
    line = file_in.readline()[:-1]
    while line != '':
        splited = line.split(' = ')
        splited[1] = int(splited[1])
        splited[0] = splited[0].split(' to ')
        trips.append([splited[0][0], splited[0][1], splited[1]])
        cities.add(splited[0][0])
        cities.add(splited[0][1])

        line = file_in.readline()[:-1]

    cities = list(cities)
    cities.sort()
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
            longest = calculate_route(aux_cities, aux_trips, dest, longest, actual)
            aux_trips = trips.copy()
        aux_cities = cities.copy()
    
    print("The longest route costs: " + str(longest))
