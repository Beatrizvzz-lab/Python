import math
from turtle import *

# Funções para desenhar as asas da borboleta
def butterfly_x(t):
    return math.sin(t) * (math.exp(math.cos(t)) - 2 * math.cos(4*t) - math.sin(t/12)**5)

def butterfly_y(t):
    return math.cos(t) * (math.exp(math.cos(t)) - 2 * math.cos(4*t) - math.sin(t/12)**5)

# Configurações da tartaruga
speed(9000)
bgcolor("lightblue")

# Loop para desenhar a borboleta
for t in range(10000):
    x = butterfly_x(t / 100) * 50  # Multiplicado por 50 para aumentar o tamanho
    y = butterfly_y(t / 100) * 50
    goto(x, y)
    color("purple")
    
# Finalização do desenho
done()
