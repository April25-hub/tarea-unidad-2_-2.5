print(" ")
print("Arzaba Diaz April 3W 1173")
import math

def area_circulo(radio):
    """
    Esta funcion calcula el area de un circulo dado su radio. #en esta linea
    
    Args:
    radio (float): El radio del circulo.

    Returns:
    float: El area del circulo.
    """
    return math.pi * radio ** 2

def volumen_cilindro(radio, altura):
    """
    Esta funcion calcula el volumen de un cilindro dado su radio y altura. #en esta linea
    
    Args:
    radio (float): El radio de la base del cilindro.
    altura (float): La altura del cilindro.

    Returns:
    float: El volumen del cilindro.
    """
    area_base = area_circulo(radio)
    return area_base * altura

# Ejemplo de uso
area = area_circulo(5)
volumen = volumen_cilindro(5, 10)
print(f"Area del circulo: {area}")  # Salida: Area del circulo: 78.53981633974483
print(f"Volumen del cilindro: {volumen}")  # Salida: Volumen del cilindro: 392.69908169872417
