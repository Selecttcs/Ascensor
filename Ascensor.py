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


##Variable para el bucle...
SW = True

##Comienzo del bucle...
while SW:

    os.system('clear')
    print('Bienvenido al ascensor Alto Colon')
    V_PISO_ACTUAL_PERSONA = random.randint(V_PRIMER_PISO, V_ULTIMO_PISO)
    V_PISO_ACTUAL_ASCENSOR_IZQ = random.randint(V_PRIMER_PISO, V_ULTIMO_PISO)
    V_PISO_ACTUAL_ASCENSOR_DER = random.randint(V_PRIMER_PISO, V_ULTIMO_PISO)

    print(f'Usted se encuentra en el piso {V_PISO_ACTUAL_PERSONA}')
    print(f'El ascensor izquierdo actualmente se encuentra en el piso {V_PISO_ACTUAL_ASCENSOR_IZQ}\n')
    print(f'El ascensor derecho actualmente se encuentra ene l piso {V_PISO_ACTUAL_ASCENSOR_DER}\n')
    op = int(input('¿Sube o baja?\n1)Sube\n2)Baja\nR:'))

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
             





        
