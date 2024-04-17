from functools import reduce

# Recibe la lista de las notas y la lista de los pesos
def calcular_promedio(estudiante_notas, pesos):
        # Obtenemos la lista con los resultados de multiplicar nota1*peso1 / nota2*peso2 / nota3*peso3
        notas_ponderadas = map(lambda x: x[0]*x[1], zip(estudiante_notas,pesos))
        # Devolvemos la suma de las notas ponderadas
        return reduce(lambda x,y: x+y, notas_ponderadas) 

def calcular_promedio_ponderado(estudiante_notaEjercicio, pesos):
    # Retorna una lista de tuplas donde el primer elemento será el nombre y el segundo el resultado de calcular_promedio
    return list(map(lambda x: (x[0],calcular_promedio(x[1],pesos)), estudiante_notaEjercicio))


estudiante_notaEjercicio = [("Alice",[90,80,70]),("Bob",[85,75,65]),("Charlie",[95,85,75])]
pesos =[0.3,0.4,0.3]

resultado = calcular_promedio_ponderado(estudiante_notaEjercicio,pesos)
print(resultado)

