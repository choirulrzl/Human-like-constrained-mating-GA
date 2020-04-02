import numpy as np

a = 1e-16 #GLOBAL variable a for derminator

'''[1] Beale ada sum'''
def beale(x,y):
    h = np.power((1.5 - x + x*y),2) + np.power((2.25 - x + x*(np.power(y,2))),2) + np.power((2.625 - x + x*(np.power(y,3))),2)
    value = np.sum( [h for i in range(1,6)] )
    fitness = 1/(value + a)
    return fitness,value

'''[2] Easom'''
def easom(x,y):
    value = -1*np.cos(x)*np.cos(y)*np.exp(-1 * np.power((x - np.pi),2) - np.power((y - np.pi),2))
    fitness = 1/(value + a)
    return fitness,value

'''[3] Matyas'''
def matyas(x,y):
    value = 0.26*(np.power(x,2) + np.power(y,2)) - 0.48*x*y
    fitness = 1/(value + a)
    return fitness,value

'''[4] Zakharov'''
def zakharov(x):
    sum1 = np.sum([np.power(x[i],2)for i in range(len(x))])
    sum2 = np.power(np.sum([0.5*(i+1)*x[i] for i in range(len(x))]),2)
    sum3 = np.power(np.sum([0.5*(i+1)*x[i] for i in range(len(x))]),4)
    value = 0.26*(np.power(x,2) + np.power(y,2)) - 0.48*x*y
    fitness = 1/(value + a)
    return fitness,value

'''[5] Colville'''
def matyas(x1,x2,x3,x4):
    value = 100 * np.power((np.power(x1,2) - np.power(x2,2)),2) + np.power(x1 - 1,2) + np.power(x3 - 1,2) +\
            90 * (np.power(x3,2) - x4) + 10.1 * ( np.power(x2 - 1,2) + np.power(x4 - 1,2) ) -\
            0.48 * x1 * x2 + 19.8 * (x2 - 1) * (x4 - 1)
    fitness = 1/(value + a)
    return fitness,value

'''[6] Schwefel 1.2'''
def schwefel(x):
    value = np.sum( [np.power(np.sum([x[j] for j in range(1,i)]),2)for i in range(1,31)] )
    fitness = 1/(value + a)
    return fitness,value

'''[7] Rosenbrock'''
def rosebrock(x):
    value = np.sum([((100*np.power((np.power((x[i]) ,2)-x[i+1]),2)) + np.power((1-x[i]),2)) for i in range(len(x))])
    fitness = 1/(value + a)
    return fitness,value


'''[8] Trid 10'''
def trid10(x):
    sum1= np.sum([np.power(x[i]-1,2) for i in range(len(x))])
    sum2= np.sum([(x[i]*x[i]-1) for i in range(len(x))])
    value = sum1 - sum2
    fitness = 1/(value + a)
    return fitness,value

'''[9] Bohachevsky 1'''
def bohanchevsky_1(x,y):
    value = np.power(x,2) + 2 * np.power(y,2) - 0.3 * np.cos(3*np.pi*x) - 0.4 * np.cos(4*np.pi*y) + 0.7
    fitness = 1/(value + a)
    return fitness,value

'''[10] Michalewicz 2'''
def mich2_5(x):
    value = -1* np.sum([(np.sin(x[i])*np.power(np.sin((i+1)*np.power(x[i],2)/np.pi),20)) for i in range(len(x))])
    fitness = 1/(value + a)
    return fitness,value

'''[11] Michalewicz 5'''
# def mich5(x):
#     value = -1* np.sum([(np.sin(x)*np.power(np.sin(i*np.power(x)/np.pi),20)) for i in range(1,6)])
#     fitness = 1/(value + a)
#     return fitness,value

'''[12] Bohachevsky 2'''
def bohanchevsky_2(x,y):
    value = np.power(x,2) + 2 * np.power(y,2) - 0.3 * np.cos(3*np.pi*x) * np.cos(4*np.pi*y) + 0.3
    fitness = 1/(value + a)
    return fitness,value

'''[13] Bohachevsky 3'''
def bohanchevsky_3(x,y):
    value = np.power(x,2) + 2 * np.power(y,2) - 0.3 * np.cos(3*np.pi*x + 4*np.pi*y) + 0.3
    fitness = 1/(value + a)
    return fitness,value

'''[14] Auckley'''
def auckley(x):
    D = 30
    sum1 = np.sum([np.power(x[i],2) for i in range(len(x))])
    sum2 = np.sum([np.cos(2*np.pi*x[i]) for i in range(len(x))])
    value = -20*np.exp(-0.2*np.sqrt(1/D*sum1))-np.exp(1/D*sum2)+20+np.exp(1)
    fitness = 1/(value + a)
    return fitness,value

'''[15] GoldStein-Price'''
def goldstein(x,y):
    value = (1 + np.power((x+y+1),2)*(19 - 14*x + 3*np.power(x,2) - 14*y + 6*x*y + 3*np.power(y,2)))*\
            (30 + np.power((2*x - 3*y),2)*(18 - 32*x + 12*np.power(x,2) + 4*y - 36*x*y + 27*np.power(y,2)))
    fitness = 1/(value + a)
    return fitness,value