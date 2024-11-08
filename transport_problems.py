import numpy as np
from scipy.optimize import linprog

# Function to solve the transportation problem using Simplex Method
# Funcția care rezolvă problema transportului folosind metoda Simplex
def solve_transport_problem(cost_matrix, supply, demand):
    # Flatten cost matrix into 1D vector
    # Transformați matricea de costuri într-un vector 1D
    c = cost_matrix.flatten()

    # Constraints for supply and demand (equality constraints)
    # Constrângeri pentru ofertă și cerere (constrângeri de egalitate)
    A_eq = []
    b_eq = []

    # Adding supply constraints
    # Adăugăm constrângerile pentru ofertă
    for i in range(len(supply)):
        constraint = [0] * len(c)
        for j in range(len(demand)):
            constraint[i * len(demand) + j] = 1
        A_eq.append(constraint)
        b_eq.append(supply[i])

    # Adding demand constraints
    # Adăugăm constrângerile pentru cerere
    for j in range(len(demand)):
        constraint = [0] * len(c)
        for i in range(len(supply)):
            constraint[i * len(demand) + j] = 1
        A_eq.append(constraint)
        b_eq.append(demand[j])

    # Solve transportation problem using Simplex
    # Rezolvăm problema transportului folosind Simplex
    result = linprog(c, A_eq=np.array(A_eq), b_eq=np.array(b_eq), method="simplex")

    # Reshape solution into matrix format
    # Reformatăm soluția într-o matrice
    solution = result.x.reshape(cost_matrix.shape)

    # Calculate total cost
    # Calculăm costul total
    total_cost = np.sum(solution * cost_matrix)
    return solution, total_cost

# Example usage
# Exemplar de utilizare
cost_matrix = np.array([[8, 15, 3, 5, 10], 
                        [2, 7, 4, 20, 8], 
                        [1, 15, 5, 6, 4]])

supply = [180, 80, 160]  # Available supply / Oferta disponibilă
demand = [60, 100, 80, 120, 60]  # Required demand / Cerere necesară

solution, total_cost = solve_transport_problem(cost_matrix, supply, demand)

print("Transport Plan (Simplex Method):\n", solution)
print(f"Total Cost: {total_cost:.2f}")

