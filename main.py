import random
import numpy as np

# Tính tổng khoảng cách
def calculate_distance(route, distance_matrix):
    return sum(distance_matrix[route[i-1]][route[i]] for i in range(len(route)))

# Tạo quần thể ban đầu
def initialize_population(cities, population_size):
    return [random.sample(cities, len(cities)) for _ in range(population_size)]

# Lựa chọn cha mẹ - Roulette Wheel Selection
def select_parents(population, fitness):
    total_fitness = sum(fitness)
    probabilities = [f / total_fitness for f in fitness]
    idx = np.random.choice(len(population), size=2, p=probabilities)
    return population[idx[0]], population[idx[1]]

# PMX - Partially Mapped Crossover (sửa lỗi)
def pmx(parent1, parent2):
    size = len(parent1)
    start, end = sorted(random.sample(range(size), 2))
    child = [None] * size
    child[start:end] = parent1[start:end]
    mapping = {parent1[i]: parent2[i] for i in range(start, end)}
    for i in range(size):
        if child[i] is None:
            value = parent2[i]
            while value in mapping and value in child[start:end]:
                value = mapping[value]
            child[i] = value
    
    return child


# CX - Cycle Crossover
def cx(parent1, parent2):
    size = len(parent1)
    child = [None] * size
    visited = [False] * size
    start = 0
    while None in child:
        if child[start] is None:
            idx = start
            while True:
                child[idx] = parent1[idx]
                visited[idx] = True
                idx = parent1.index(parent2[idx])
                if idx == start:
                    break
        start = visited.index(False) if False in visited else None
    for i in range(size):
        if child[i] is None:
            child[i] = parent2[i]
    return child

# OX - Order Crossover
def ox(parent1, parent2):
    size = len(parent1)
    start, end = sorted(random.sample(range(size), 2))
    child = [None] * size
    child[start:end] = parent1[start:end]
    pointer = end
    for city in parent2:
        if city not in child:
            if pointer >= size:
                pointer = 0
            child[pointer] = city
            pointer += 1
    return child

# Đột biến - Swap Mutation
def mutate(route):
    a, b = random.sample(range(len(route)), 2)
    route[a], route[b] = route[b], route[a]

# Thuật toán di truyền chính
def genetic_algorithm(distance_matrix, cities, population_size, generations, crossover_method="pmx"):
    population = initialize_population(cities, population_size)
    best_route = None
    best_distance = float('inf')

    for generation in range(generations):
        # Tính fitness
        fitness = [-calculate_distance(route, distance_matrix) for route in population]
        
        # Cập nhật lời giải tốt nhất
        for route in population:
            distance = calculate_distance(route, distance_matrix)
            if distance < best_distance:
                best_distance = distance
                best_route = route
        
        new_population = []
        
        # Sinh sản
        for _ in range(population_size // 2):
            parent1, parent2 = select_parents(population, fitness)
            
            # Lai ghép
            if crossover_method == "pmx":
                child1 = pmx(parent1, parent2)
                child2 = pmx(parent2, parent1)
            elif crossover_method == "cx":
                child1 = cx(parent1, parent2)
                child2 = cx(parent2, parent1)
            elif crossover_method == "ox":
                child1 = ox(parent1, parent2)
                child2 = ox(parent2, parent1)
            else:
                raise ValueError("Invalid crossover method")
            
            # Đột biến
            if random.random() < 0.1:
                mutate(child1)
            if random.random() < 0.1:
                mutate(child2)
            
            new_population.extend([child1, child2])
        
        population = new_population
    
    return best_route, best_distance

# Ví dụ sử dụng
if __name__ == "__main__":
    # Ma trận khoảng cách giữa các thành phố
    cities = list(range(5))
    distance_matrix = np.random.randint(1, 100, size=(5, 5))
    np.fill_diagonal(distance_matrix, 0)
    
    # In ra ma trận khoảng cách
    print("Distance Matrix:")
    print(distance_matrix)
    
    # Chạy thuật toán di truyền
    method = "pmx"  # Thay đổi giữa "pmx", "cx", và "ox"
    best_route, best_distance = genetic_algorithm(distance_matrix, cities, population_size=10, generations=100, crossover_method=method)
    
    # Kết quả
    print(f"Best route using {method.upper()}: {best_route}")
    print(f"Best distance: {best_distance}")
