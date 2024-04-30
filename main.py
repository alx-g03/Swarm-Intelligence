from ant_system import ant_system
from citeste_fisier import citeste_tsp_din_fisier
from particle_swarm_optimization import PSO


def main():
    tsp_file = "kroC100.tsp"  # Numele fișierului cu datele tsp
    cities = citeste_tsp_din_fisier(tsp_file)

    def afisare_meniu():
        print("Meniu:")
        print("1. Particle swarm optimization pentru functia Schwefel")
        print("2. Ant system pentru TSP")
        print("x. Exit")

    while True:
        afisare_meniu()
        optiune = input("Selectați o opțiune: ")

        if optiune == "1":
            best_solution, best_fitness = PSO(num_dimensions=2, num_particles=20, inertia_weight=0.5,
                                              cognitive_weight=0.5, social_weight=0.5, max_iterations=100,
                                              domain_min=-500, domain_max=500)
            print("Best solution:", best_solution)
            print("Best fitness:", best_fitness)
        elif optiune == "2":
            best_tour, best_distance = ant_system(cities, num_ants=20, alpha=1.0, beta=3.0, evaporation_rate=0.1,
                                                  num_iterations=100)
            print("Best tour:", best_tour)
            print("Best distance:", best_distance)
        elif optiune == "x":
            break
        else:
            print("Opțiune invalidă! Vă rugăm să selectați din nou.")


if __name__ == "__main__":
    main()
