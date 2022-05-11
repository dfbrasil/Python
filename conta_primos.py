
def n_primos(n):
    
    aux = 0
    
    while n>=2:
        
        if n == 2 or n == 3 or n == 5 or n == 7:
            aux = aux + 1
            n = n - 1
               
           
        elif n%2==0 or n%3==0 or n%5==0 or n%7==0:
            n = n - 1
            

        elif n%2!=0 or n%3!=0 or n%5!=0 or n%7!=0:
            aux = aux + 1
            n = n - 1
        
        
    return(aux)

       

print (n_primos(121))