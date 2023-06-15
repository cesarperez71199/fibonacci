

#Serie Fibonacci

#Proceso que calculara la serie fibonacci 
def fibonacci(m):
    f0=0
    f1=1
    lista_fibo=[0,1]
    
    
    for k in range(2,m):        #Todo esteproceso cambia los valores de f0,f1 y f 
                                #conforme vaya aumentando el contador
        f=f0+f1
        f0=f1
        f1=f
        lista_fibo.append(f)
        
    print("La serie Fibonacci es: ",lista_fibo)
    
    
fibonacci(10)
