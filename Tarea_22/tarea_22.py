N_Vacas_venta = int(input('Número de vacas en venta: ')) #La cantidad de vacas a la venta.
P_Camión = int(input('Camión de (kg): '))  #El peso del camión.
print(' ')
N_Vaca = 1 #El número de la vaca.
Lista_n =[N_Vaca]
Lista_n.remove(1)
E_Vaca = 0 #Eficiencia de la vaca (L/día*Kg).
Lista_E = [E_Vaca]
Lista_E.remove(0)
P_Vaca = 0 #Peso de la vaca
Lista_P = [P_Vaca]
Lista_P.remove(0)
T_Vaca = 0 #Suma de los pesos totales.
T_L_vaca = 0 #Suma de los litros producidos por día.
E_Vaca_A = 0 #La eficencia de la vaca anterior.
L_vaca = 0 #Litros producidos por día.
Lista_L = [L_vaca]
Lista_L.remove(0)

elemento = 0 #

print('Nº / Kg / Producción (l/día)') 
#Un bucle para coger los valores de las vacas.
#AL INTRODUCIR LOS DATOS PONERLOS A LA VEZ SEPARADOS CON UN ESPACIO.
while N_Vaca != N_Vacas_venta + 1: #Este bucle While hace la función de un bucle For.
    print (N_Vaca,end= ' ') #El "(end= ' ')"" para mantener el input en la misma línea.
    
    P_Vaca, L_vaca = map(int, input('  ').strip().split()) #He recurrido a esta opción para poner dos input en la misma línea. 
    E_Vaca = int(round((L_vaca / P_Vaca)* 100000, 3)) #Cálculo de la eficiencia y multiplicado por 100000 no trabajar con decimales.
    elemento = iter(Lista_E)
    a = 100000000

    if (E_Vaca_A < E_Vaca): #Para resolver el ejercicio he creado listas que se irán reordenando de mayor a menor según la eficiencia de las vacas(L/día*Kg).
        E_Vaca_A = E_Vaca
        Lista_E.insert(0, E_Vaca)
        Lista_n.insert(0, N_Vaca)
        Lista_P.insert(0, P_Vaca)
        Lista_L.insert(0, L_vaca)
    else:
        for _ in range(N_Vacas_venta):  #Se comparan las eficiencias y se van ordenando.
            if E_Vaca > a and (E_Vaca not in Lista_E): 
                Lista_E.insert(Lista_E.index(a), E_Vaca)
                Lista_n.insert(Lista_E.index(E_Vaca), N_Vaca)
                Lista_P.insert(Lista_E.index(E_Vaca), P_Vaca)
                Lista_L.insert(Lista_E.index(E_Vaca), L_vaca)
            elif len(Lista_E) > 2 and _ <= len(Lista_E)-1:
                a = next(elemento)
            elif E_Vaca not in Lista_E:
                Lista_E.append(E_Vaca)
                Lista_n.append(N_Vaca)
                Lista_P.append(P_Vaca)
                Lista_L.append(L_vaca)                 

    T_L_vaca = T_L_vaca + L_vaca              
    T_Vaca = T_Vaca + P_Vaca  
    N_Vaca = N_Vaca + 1

print (' '+ '\n')
print('Vaca(s) seleccionada(s):'+ '\n')
print('Nº / Kg / Producción (l/día)') 

while T_Vaca > P_Camión: #Bucle que va suprimiendo las vacas que no van a ser compradas y valora alternativas mejores según su peso y producción.
    A_T_Vaca = T_Vaca - Lista_P[-2] #Suma de los pesos totales alternativa.
    A_T_L_vaca = T_L_vaca - Lista_L[-2] #Suma de los litros producidos por día alternativa.
    R_T_L_vaca = T_L_vaca - Lista_L[-1] #Suma de los litros producidos por día reciente a comparar.

    if A_T_Vaca < P_Camión and A_T_L_vaca > R_T_L_vaca:
        Lista_n.pop(-2)
        T_L_vaca = T_L_vaca - Lista_L.pop(-2)
        T_Vaca = T_Vaca - Lista_P.pop(-2)    
    else:
        Lista_n.pop()
        T_L_vaca = T_L_vaca - Lista_L.pop()
        T_Vaca = T_Vaca - Lista_P.pop()
        
for i in range(len(Lista_n)): #Para imprimir los valorres finales elegidos.
    print (Lista_n[i], ' ', Lista_P[i], Lista_L[i])   
print()    
print(len(Lista_n),'vaca(s) seleccionada(s), con un peso total de', T_Vaca,'Kg. y con una producción total de', T_L_vaca,'L.')
input()