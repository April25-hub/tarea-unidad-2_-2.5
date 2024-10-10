# tarea-unidad-2_-2.5
Arzaba Diaz April 1174 3W
print(" ")
print("Arzab Diaz April 3W 1173")
import math

def calcular_area_circulo(radio):
    """
    calcula el area de un circulo dado su radio.

    args:
        radio (float): el radio del circulo.

    returns:
        float: el area del circulo.
    """
    area = math.pi * (radio ** 2)
    return area

def calcular_volumen_cilindro(radio, altura):
    """
calcula el volumen de un cilindro dado su radio y altura.

    args:
        radio (float): el radio de la base del cilindro.
        altura (float): la altura del cilindro.

    returns:
        float: el volumen del cilindro.
    """
    area_base = calcular_area_circulo(radio)  #esta linea llama a la funcion para calcular el area
    volumen = area_base * altura
    return volumen

#esta linea me dara un ejemplo de uso
radio = 5  #esta linea me da el radio del circulo y base del cilindro
altura = 10  #esta linea me dara la altura del cilindro

area = calcular_area_circulo(radio)
volumen = calcular_volumen_cilindro(radio, altura)

print(f"el area del circulo con radio {radio} es: {area}")
print(f"el volumen del cilindro")
![image](https://github.com/user-attachments/assets/df43b4ec-f8a2-42e4-b0e8-ade4e852a455)
![image](https://github.com/user-attachments/assets/16e29208-f945-46ed-b6bd-c0160fdd3de5)

