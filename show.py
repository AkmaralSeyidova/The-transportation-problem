import numpy as np
from scipy.optimize import linprog
import tkinter as tk
from tkinter import messagebox

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

# Function called when "Solve" button is clicked
# Funcția apelată când butonul "Rezolvă" este apăsat
def solve():
    try:
        # Get cost matrix from user input
        # Obținem matricea de costuri din intrarea utilizatorului
        cost_matrix = np.array([[float(x) for x in row.split()] for row in cost_matrix_entry.get("1.0", "end-1c").split("\n") if row])
        
        # Get supply and demand values from user input
        # Obținem valorile de ofertă și cerere din intrarea utilizatorului
        supply = [float(x) for x in supply_entry.get().split()]
        demand = [float(x) for x in demand_entry.get().split()]
        
        # Solve transportation problem
        # Rezolvăm problema transportului
        solution, total_cost = solve_transport_problem(cost_matrix, supply, demand)
        
        # Display the results
        # Afișăm rezultatele
        result_text = f"Plan de transport:\n{solution}\n\nCost total: {total_cost:.2f}"
        result_label.config(text=result_text)
    except Exception as e:
        messagebox.showerror("Eroare", f"Eroare de intrare: {str(e)}")

# Create the GUI using Tkinter
# Creăm interfața grafică (GUI) folosind Tkinter
root = tk.Tk()
root.title("Problema de transport - Metoda Simplex")

# Input for cost matrix
# Introducere pentru matricea de costuri
tk.Label(root, text="Matricea de costuri (separați cu spațiu valorile pe rânduri):").pack()
cost_matrix_entry = tk.Text(root, height=8, width=60)
cost_matrix_entry.pack()

# Input for supply values
# Introducere pentru valorile de ofertă
tk.Label(root, text="Cantități disponibile (separați cu spațiu valorile):").pack()
supply_entry = tk.Entry(root, width=60)
supply_entry.pack()

# Input for demand values
# Introducere pentru valorile de cerere
tk.Label(root, text="Cantități necesare (separați cu spațiu valorile):").pack()
demand_entry = tk.Entry(root, width=60)
demand_entry.pack()

# Solve button
# Butonul "Rezolvă"
solve_button = tk.Button(root, text="Rezolvă", command=solve)
solve_button.pack()

# Label to display the results
# Etichetă pentru afișarea rezultatelor
result_label = tk.Label(root, text="")
result_label.pack()

# Start the GUI loop
# Pornim bucla interfeței grafice
root.mainloop()



