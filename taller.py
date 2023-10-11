# Importando las librerías necesarias
import numpy as np
from datasets import load_dataset

# Función para instalar la librería 'datasets' e importar el dataset
def load_and_process_data():
    # Cargando el dataset
    dataset = load_dataset("mstz/heart_failure")

    # Accediendo a la partición "train"
    data = dataset["train"]

    # Convirtiendo la lista de edades a un arreglo de NumPy
    ages = np.array(data['age'])

    return ages

# Función para calcular e imprimir el promedio de edad
def calculate_average_age(ages):
    # Calculando el promedio de edad
    average_age = np.mean(ages)

    # Imprimiendo el promedio de edad
    print(f"El promedio de edad de los participantes en el estudio es {average_age:.2f} años.")

# Ejecutando las funciones
ages = load_and_process_data()
calculate_average_age(ages)