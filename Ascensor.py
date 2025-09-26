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
MENSAJE = ''
IZQ = 0
DER = 0
ACT = 0

##Variable para el bucle...
SW = True

##Comienzo del bucle...
while SW:

    os.system('clear')
    print('*************************************')
    print('*                                   *')
    print('* Bienvenido al ascensor Alto Colon *')
    print('*                                   *')
    print('*************************************\n')
    V_PISO_ACTUAL_PERSONA = random.randint(V_PRIMER_PISO, V_ULTIMO_PISO)
    V_PISO_ACTUAL_ASCENSOR_IZQ = random.randint(V_PRIMER_PISO, V_ULTIMO_PISO)
    V_PISO_ACTUAL_ASCENSOR_DER = random.randint(V_PRIMER_PISO, V_ULTIMO_PISO)
    V_DISTANCIA_PERSONA_IZQ = V_PISO_ACTUAL_ASCENSOR_IZQ - V_PISO_ACTUAL_PERSONA
    V_DISTANCIA_PERSONA_DER = V_PISO_ACTUAL_ASCENSOR_DER - V_PISO_ACTUAL_PERSONA

    #Validacion si el numero es negativo cambiar a positivo el signo
    if V_DISTANCIA_PERSONA_IZQ < 0:
        V_DISTANCIA_PERSONA_IZQ = 0
        V_DISTANCIA_PERSONA_IZQ = V_PISO_ACTUAL_PERSONA - V_PISO_ACTUAL_ASCENSOR_IZQ
    
    if V_DISTANCIA_PERSONA_DER < 0:
        V_DISTANCIA_PERSONA_DER = 0
        V_DISTANCIA_PERSONA_DER = V_PISO_ACTUAL_PERSONA - V_PISO_ACTUAL_ASCENSOR_DER


    print('*************************************')
    print('*                                   *')
    print(f'* Usted se encuentra en el piso {V_PISO_ACTUAL_PERSONA}   *')
    print('*                                   *')
    print('*************************************\n')
    
    print('*****************************************************************')
    print('*                                                                *')
    print(f'* El ascensor IZQUIERDO actualmente se encuentra en el piso {V_PISO_ACTUAL_ASCENSOR_IZQ} *\n')
    print(f'* El ascensor DERECHO actualmente se encuentra en el piso {V_PISO_ACTUAL_ASCENSOR_DER} *')
    print('*                                                              *')
    print(f'****************************************************************\n')
    

    try:    
        op = int(input('¿Desea presionar el botón? \n1)Presionar 2)No presionar\nR:'))
        if op == 1:

        #Validación si el usuario se encuentra en el mismo piso que el de algún ascensor no enviar
        #ascensor al usuario y enviar mensaje de que el ascensor ya se encuentra ahí

            if V_PISO_ACTUAL_PERSONA == V_PISO_ACTUAL_ASCENSOR_IZQ or V_PISO_ACTUAL_PERSONA == V_PISO_ACTUAL_ASCENSOR_DER:
                
                if V_PISO_ACTUAL_ASCENSOR_IZQ == V_PISO_ACTUAL_ASCENSOR_DER:
                    os.system('clear')
                    ACTUAL = V_PISO_ACTUAL_ASCENSOR_DER
                    print(f'El ascensor de la izquierda y la derecha se encuentran en el mismo piso que el usuario (Piso {ACTUAL})..')
                    print('\nAbriendo puertas del ascensor de la derecha...')
                    time.sleep(3)

                elif V_PISO_ACTUAL_PERSONA == V_PISO_ACTUAL_ASCENSOR_IZQ:
                    os.system('clear')
                    IZQ = V_PISO_ACTUAL_ASCENSOR_IZQ
                    ACT = V_PISO_ACTUAL_PERSONA
                    print(f'El Ascensor IZQUIERDO está en el mismo piso que el usuario (piso {ACT}) así que solo se abrirán las puertas...')

                    time.sleep(3)
                    os.system('clear')
                elif V_PISO_ACTUAL_PERSONA == V_PISO_ACTUAL_ASCENSOR_DER:    
                    os.system('clear')
                    DER = V_PISO_ACTUAL_ASCENSOR_DER
                    ACT = V_PISO_ACTUAL_PERSONA
                    print(f'El Ascensor DERECHO está en el mismo piso que el usuario (piso {ACT}) así que solo se abrirán las puertas...')

                    time.sleep(3)
                    os.system('clear')
            else:
                ##Condicionales para saber si subo o baja el ascensor de la izquierda o la derecha
                if V_DISTANCIA_PERSONA_IZQ <= V_DISTANCIA_PERSONA_DER:
                    print(f'\n\nYendo ascensor de la izquierda piso {V_PISO_ACTUAL_ASCENSOR_IZQ} hacia la persona que se encuentra')

                    print(f'en el piso {V_PISO_ACTUAL_PERSONA}.')

                    #print('Explicación:')
                    #print(f'Porque la distancia entra la persona y el ascensor izquierdo ({V_DISTANCIA_PERSONA_IZQ}) es inferior a la')
                    #print(f'distancia ascensor derecho ({V_DISTANCIA_PERSONA_DER})')
                    SW = False
                elif V_DISTANCIA_PERSONA_DER <= V_DISTANCIA_PERSONA_IZQ:
                    print(f'\n\nYendo ascensor de la derecha piso {V_PISO_ACTUAL_ASCENSOR_DER} hacia la persona que se encuentra')
        
                    print(f'en el piso {V_PISO_ACTUAL_PERSONA}')

                    #print('\n\n\nExplicación:')
                    #print(f'Porque la distancia entra la persona y el ascensor derecho ({V_DISTANCIA_PERSONA_DER}) es inferior a la')
                    #print(f'distancia ascensor izquierdo ({V_DISTANCIA_PERSONA_IZQ})')
                    SW = False
        elif op == 2: 
            print('Hasta luego!')
            time.sleep(3)
            SW = False

        else:
            os.system('clear')
            print('Escoga los números indicados...')
            time.sleep(3)
    except:
        os.system('clear')
        print('Ocurrió un error, probablemente pusiste una letra donde debía ir un número...')
        time.sleep(3)
        




        
