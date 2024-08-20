# Función para calcular el volumen y el pago
def calcular_pago(L, A, H, costo_por_metro_cubico):
    # Calcular el volumen de la alberca (en metros cúbicos)
    volumen = L * A * H
    
    # Calcular el pago total
    pago = volumen * costo_por_metro_cubico
    
    return volumen, pago

# Leer las dimensiones de la alberca y el costo por metro cúbico de agua
L = float(input("Ingrese el largo de la alberca en metros: "))
A = float(input("Ingrese el ancho de la alberca en metros: "))
H = float(input("Ingrese la altura de la alberca en metros: "))
costo_por_metro_cubico = float(input("Ingrese el costo por metro cúbico de agua: "))

# Calcular el volumen y el pago
volumen, pago = calcular_pago(L, A, H, costo_por_metro_cubico)

# Mostrar los resultados
print(f"El volumen de la alberca es de {volumen:.2f} metros cúbicos.")
print(f"El pago total por llenar la alberca es de ${pago:.2f}.")
