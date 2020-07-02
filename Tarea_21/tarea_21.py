Valor_introducido = float (input()) #Se usa float porque se introduce un número decimal.
conversion_a_n_entero = int(Valor_introducido * 10000) #int para convertir el valor introducido a número entero.
Conversor_a_n_entero = 10000
divisor_común = conversion_a_n_entero

#Mientras el divisor común sea desigual a 1, se ha de cumplir que el resto para ambos valores, con el divisor común, sea igual a 0.
while divisor_común != 1 :
    if conversion_a_n_entero % divisor_común == 0 and Conversor_a_n_entero % divisor_común == 0:
        conversion_a_n_entero = conversion_a_n_entero // divisor_común
        Conversor_a_n_entero = Conversor_a_n_entero // divisor_común
    divisor_común =  divisor_común - 1 #el divisor se va reduciendo hasta llegar al máximo común divisor.

Num = conversion_a_n_entero
Denom = Conversor_a_n_entero
print (Num, '/', Denom) 