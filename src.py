import csv
from queue import PriorityQueue


class CityNotFoundError(Exception):

    def __init__(self, city):

        print("%s does not exist" % city)


class SameCitySelectedError(Exception):

    def __init__(self):

        print("Starting city and destination city cannot be the same.")


def build_graph(path):

    graph = {}

    with open(path, newline='', encoding='utf-8') as csvfile:
        
        reader = csv.reader(csvfile, delimiter=',')

        next(reader) # Otherwise error occurs (Since the headers are not in the same format with the target data itself)

        for row in reader:
            # Get the needed information from the file
            city1 = row[0]
            city2 = row[1]
            distance = row[2]

            if city1 not in graph:
                # If the city is not added before, then add it to the graph
                graph[city1] = {}

            if city2 not in graph:
                # If the city is not added before, then add it to the graph
                graph[city2] = {}

            # Add the distances as values to the graph dictionary whiches keys are city1 and city2.
            # Since the roads in between cities are bidirectional, make the same operation in two ways.
            graph[city1][city2] = int(distance)
            graph[city2][city1] = int(distance)

    return graph


def uniform_cost_search(graph, start, end):

    if start not in graph:
        # If the selected city is not in the graph since it is not in the file
        raise CityNotFoundError(start)

    if end not in graph:
        # If the selected city is not in the graph since it is not in the file
        raise CityNotFoundError(end)

    if start == end:
        # If the selected cities are the same, then it must be a logical mistake
        raise SameCitySelectedError()

    # To keep track of the nodes to be explored
    queue = PriorityQueue()
    # Init the queue with adding starting point with an empty path with cost = 0
    queue.put((0, start, []))
    # To keep track of the explored nodes
    explored = set()

    while not queue.empty():
        # Until the road is fully created

        (cost, current_node, path) = queue.get()

        if current_node == end:
            # If the road is ended and so the goal is reached

            # Add the current node to the currently reached path
            return (cost, path + [current_node])

        # Flag the current node as it is explored if the ending point is not reached so the path is not complete yet
        explored.add(current_node)

        for neighbor, distance in graph[current_node].items():

            if neighbor not in explored:
                # If the neighbor is not explored yet

                # Put the path + current node as the path with adding the cost to get that neighbor to the queue
                queue.put((cost + distance, neighbor, path + [current_node]))

    raise CityNotFoundError(
        "There is no path between %s and %s" % (start, end))


if __name__ == "__main__":

    path = input("Enter the path of the csv file: ")
    graph = build_graph(path)
    
    print("Available cities:")

    for city in graph.keys():

        print(city)

    start = input("Select starting city from the list: ")

    end = input(
        "Select ending city from the list -differs from the starting point-: ")

    try:

        cost, path = uniform_cost_search(graph, start, end)

        print("The shortest distance from %s to %s is %d km." %
              (start, end, cost))

        print("The path is:", ' -> '.join(path))

    except CityNotFoundError as e:

        print(e)

    except SameCitySelectedError as e:

        print(e)
