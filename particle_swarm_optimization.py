import random
import math


def fitness_function(solution):
    return sum([-x * math.sin(math.sqrt(abs(x))) for x in solution])


def initialize_particles(num_particles, num_dimensions, domain_min, domain_max):
    positions = []
    velocities = []
    personal_best = []
    personal_best_fitness = []

    for _ in range(num_particles):
        position = [random.uniform(domain_min, domain_max) for _ in range(num_dimensions)]
        velocity = [random.uniform(-1, 1) for _ in range(num_dimensions)]
        positions.append(position)
        velocities.append(velocity)
        personal_best.append(position[:])
        personal_best_fitness.append(fitness_function(position))

    return positions, velocities, personal_best, personal_best_fitness


def update_particles(positions, velocities, personal_best, personal_best_fitness, global_best, global_best_fitness, inertia_weight, cognitive_weight, social_weight):
    num_particles = len(positions)
    num_dimensions = len(positions[0])

    for i in range(num_particles):
        for j in range(num_dimensions):
            cognitive_component = cognitive_weight * random.random() * (personal_best[i][j] - positions[i][j])
            social_component = social_weight * random.random() * (global_best[j] - positions[i][j])
            velocities[i][j] = inertia_weight * velocities[i][j] + cognitive_component + social_component
            positions[i][j] += velocities[i][j]

        fitness_value = fitness_function(positions[i])

        if fitness_value < personal_best_fitness[i]:
            personal_best[i] = positions[i][:]
            personal_best_fitness[i] = fitness_value

        if fitness_value < global_best_fitness:
            global_best = positions[i][:]
            global_best_fitness = fitness_value

    return positions, velocities, personal_best, personal_best_fitness, global_best, global_best_fitness


def PSO(num_dimensions, num_particles, inertia_weight, cognitive_weight, social_weight, max_iterations, domain_min, domain_max):
    positions, velocities, personal_best, personal_best_fitness = initialize_particles(num_particles, num_dimensions, domain_min, domain_max)
    global_best = positions[personal_best_fitness.index(min(personal_best_fitness))][:]
    global_best_fitness = min(personal_best_fitness)

    for _ in range(max_iterations):
        positions, velocities, personal_best, personal_best_fitness, global_best, global_best_fitness = update_particles(positions, velocities, personal_best, personal_best_fitness, global_best, global_best_fitness, inertia_weight, cognitive_weight, social_weight)

    return global_best, global_best_fitness
