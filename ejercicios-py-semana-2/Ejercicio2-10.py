METROS_A_PULGADAS = 39.3701

def convertir_metros_a_pulgadas(metros):
    pulgadas = metros * METROS_A_PULGADAS
    return pulgadas

metros = float(input("Ingrese la cantidad de metros de tela: "))

pulgadas = convertir_metros_a_pulgadas(metros)

print(f"Debe pedir {pulgadas} pulgadas de tela.")