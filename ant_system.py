import random
import math


class Ant:
    def __init__(self, num_cities):
        self.num_cities = num_cities
        self.visited = [False] * num_cities
        self.tour = []
        self.total_distance = 0.0

    def visit_city(self, city):
        self.visited[city] = True
        self.tour.append(city)

    def is_visited(self, city):
        return self.visited[city]

    def clear(self):
        self.visited = [False] * self.num_cities
        self.tour = []
        self.total_distance = 0.0


def distance(city1, city2):
    return math.sqrt((city1[1] - city2[1]) ** 2 + (city1[2] - city2[2]) ** 2)


def calculate_total_distance(tour, cities):
    total_distance = 0.0
    for i in range(len(tour)):
        total_distance += distance(cities[tour[i]], cities[tour[(i + 1) % len(tour)]])
    return total_distance


def ant_system(cities, num_ants, alpha, beta, evaporation_rate, num_iterations):
    num_cities = len(cities)
    pheromone = [[1.0 / (num_cities * num_cities)] * num_cities for _ in range(num_cities)]

    best_tour = None
    best_distance = float('inf')

    for _ in range(num_iterations):
        ants = [Ant(num_cities) for _ in range(num_ants)]
        for ant in ants:
            ant.visit_city(random.randint(0, num_cities - 1))

        for _ in range(num_cities - 1):
            for ant in ants:
                current_city = ant.tour[-1]
                unvisited_cities = [i for i in range(num_cities) if not ant.is_visited(i)]

                probabilities = [math.pow(pheromone[current_city][i], alpha) * math.pow(1.0 / distance(cities[current_city], cities[i]), beta) for i in unvisited_cities]
                total_probability = sum(probabilities)
                probabilities = [p / total_probability for p in probabilities]

                selected_city = random.choices(unvisited_cities, probabilities)[0]
                ant.visit_city(selected_city)

        for ant in ants:
            ant.total_distance = calculate_total_distance(ant.tour, cities)
            if ant.total_distance < best_distance:
                best_distance = ant.total_distance
                best_tour = ant.tour

        for i in range(num_cities):
            for j in range(num_cities):
                pheromone[i][j] *= (1.0 - evaporation_rate)

        for i in range(num_cities):
            for j in range(num_cities):
                if i != j:
                    pheromone[i][j] += (1.0 / best_distance)

    return best_tour, best_distance
