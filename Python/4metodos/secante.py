def secant(fun, x_a, x_b, steps=50):
    # El método de la secante no se puede aplicar
    if fun(x_a) * fun(x_b) >= 0:
        print('El método de la secante no se puede aplicar')
        return None
    
    # El método de la secante 
    for n in range(steps + 1):
        # Cálculo de la secante
        x_n = x_a - fun(x_a)*(x_b - x_a)/(fun(x_b) - fun(x_a))
        
        if fun(x_n) == 0:
            return x_n
        
        if fun(x_a) * fun(x_n) < 0:
            x_b = x_n
        else:
            x_a = x_n
    return x_n

f = lambda x: x**2 + 2*x - 8
secant(f, 0, 5,  5) # 1.995887594242632
secant(f, 0, 5, 15) # 1.9999999303082814
secant(f, 0, 5, 25) # 1.9999999999988198
secant(f, 0, 5, 35) # 2.0