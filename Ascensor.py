#Programa ascensor Colon

##Importación de librerías
import time
import os
import random 


##Variables a utilizar
V_SUBIR = 0
V_BAJAR = 0
V_PISO_ACTUAL_PERSONA = 0
V_PISO_ACTUAL_ASCENSOR_IZQ  = 0
V_PISO_ACTUAL_ASCENSOR_DER  = 0


V_PRIMER_PISO = 1
V_ULTIMO_PISO = 15
V_DISTANCIA_PERSONA_IZQ = 0
V_DISTANCIA_PERSONA_DER = 0

##Variable para el bucle...
SW = True

##Comienzo del bucle...
while SW:

    os.system('clear')
    print('Bienvenido al ascensor Alto Colon')
    V_PISO_ACTUAL_PERSONA = random.randint(V_PRIMER_PISO, V_ULTIMO_PISO)
    V_PISO_ACTUAL_ASCENSOR_IZQ = random.randint(V_PRIMER_PISO, V_ULTIMO_PISO)
    V_PISO_ACTUAL_ASCENSOR_DER = random.randint(V_PRIMER_PISO, V_ULTIMO_PISO)

    V_DISTANCIA_PERSONA_IZQ = V_PISO_ACTUAL_PERSONA - V_PISO_ACTUAL_ASCENSOR_IZQ
    V_DISTANCIA_PERSONA_DER = V_PISO_ACTUAL_PERSONA - V_PISO_ACTUAL_ASCENSOR_DER
    V_DISTANCIA_TOTAL = V_DISTANCIA_PERSONA_IZQ - V_DISTANCIA_PERSONA_DER

    print(f'Usted se encuentra en el piso {V_PISO_ACTUAL_PERSONA}')
    print(f'El ascensor izquierdo actualmente se encuentra en el piso {V_PISO_ACTUAL_ASCENSOR_IZQ}\n')
    print(f'El ascensor derecho actualmente se encuentra en el piso {V_PISO_ACTUAL_ASCENSOR_DER}\n')
    op = int(input('¿Sube o baja?\n1)Sube\n2)Baja\nR:'))
    
    ##Condicionales para saber si subo o baja el ascensor de la izquierda o la derecha
    if V_DISTANCIA_PERSONA_IZQ < V_DISTANCIA_PERSONA_DER:
        print(f'Yendo ascensor de la izquierda piso {V_PISO_ACTUAL_ASCENSOR_IZQ} hacia la persona que se encuentra')

        print(f'en el piso {V_PISO_ACTUAL_PERSONA}')
        SW = False

    elif V_DISTANCIA_PERSONA_DER < V_DISTANCIA_PERSONA_IZQ:
        print(f'Yendo ascensor de la derecha piso {V_PISO_ACTUAL_ASCENSOR_DER} hacia la persona que se encuentra')

        print(f'en el piso {V_PISO_ACTUAL_PERSONA}')   
        SW = False
        



    if op == 1:
        print('Subiendo...')
        time.sleep(3)
        SW = False
    elif op == 2:
        print('Bajando...')
        time.sleep(3)
        SW = False
    else:
        os.system('clear')
        print('Escoga los números indicados...')
        time.sleep(3)
             





        
