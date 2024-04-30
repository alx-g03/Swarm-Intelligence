def citeste_tsp_din_fisier(filename):
    cities = []
    with open(filename, 'r') as file:
        lines = file.readlines()
        node_coord_section = False
        for line in lines:
            if line.startswith('NODE_COORD_SECTION'):
                node_coord_section = True
                continue
            elif line.startswith('EOF'):
                break
            elif node_coord_section:
                data = line.split()
                city_id = int(data[0])
                x = float(data[1])
                y = float(data[2])
                cities.append((city_id, x, y))
    return cities
