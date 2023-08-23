class Airplane:
    def __init__(self, id, origin, destination, cost):
        self.id = id
        self.origin = origin
        self.destination = destination
        self.cost = cost

    def __repr__(self):
        return f"Airplane({self.id}, {self.origin}, {self.destination}, {self.cost})"

def find_flights(airplanes, search):
    if search == 1:
        city = input("Enter the city: ")
        return [airplane for airplane in airplanes if airplane.origin == city]
    elif search == 2:
        city = input("Enter the city: ")
        return [airplane for airplane in airplanes if airplane.destination == city]
    elif search == 3:
        city_from = input("Enter the city from: ")
        city_to = input("Enter the city to: ")
        return [airplane for airplane in airplanes if airplane.origin == city_from and airplane.destination == city_to]
    else:
        print("ERROR")

if __name__ == "__main__":
    airplanes = [
        Airplane("AI161E90", "BLR", "BOM", 5600),
        Airplane("BR161F91", "BOM", "BBI", 6750),
        Airplane("AI161F99", "BBI", "BLR", 8210),
        Airplane("VS171E20", "JLR", "BBI", 5500),
        Airplane("AS171G30", "HYD", "JLR", 4400),
        Airplane("AI131F49", "HYD", "BOM", 3499),
    ]

    search = int(input("Enter the search parameter (1, 2, or 3): "))

    filtered_airplanes = find_flights(airplanes, search)

    if filtered_airplanes:
        print(filtered_airplanes)
    else:
        print("No flights found.")
