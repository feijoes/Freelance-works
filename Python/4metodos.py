import numpy as np


def f(x):
    #return x*x*x-10*x*x+5
    return (x**3)-(10*x**2)+(5)

iteracciones = 50 
eps = 10E-6 

a = 0        
b = 1      
 

if f(a)*f(b)<=0:
  
   

  print('\ni \t\t     XInf \t     XSup \t\t  XM \t\t|f(xm)| \t |Er|       ')
  print('------------------------------------------------------------------')
   

  for i in range(iteracciones):
      c = b-((f(b))*(a-b))/(f(a)-f(b))      
      n = abs(float((a-c)/c))
  
      print(str(i+1)+'\t\t% 10.4f\t% 10.4f\t% 10.4f\t% 10.4f\t% 10.4f\t' %(a, b, c, f(c), n))
      if np.abs(f(c))<eps:
          print('\nRaíz x = '+str(c))
          print('\n\n\n\n\n\n')
          break
      if f(a)*f(c)<0:
          b = c
      else:
          a = c
  if i==iteracciones-1:
      print('\n\nMaximas interacciones alcanzadas')
      print('Aproximacion de las iteracciones: '+str(c))
else:
  print("No hay raiz en el rango establecido")
  