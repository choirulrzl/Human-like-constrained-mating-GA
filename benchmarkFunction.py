import numpy as np

#===========================Debugging Function Start==============================
'''Ackley N. 2 Function
Global Minima f(x) = -200 located at x = (0,0) ; x [-4,4]'''
def ackley(x,y):
    h = -200 * np.exp(-0.02*np.sqrt((np.power(x,2)) + (np.power(y,2))))
    a = 0.000000000000000001
    return 1/(h + a)

def ackley_global_minima(x,y):
    return -200 * np.exp(-0.02*np.sqrt((np.power(x,2)) + (np.power(y,2))))
#===========================Debugging Function End==============================

#===========================BENCHMARK FUNCTION START HERE=======================
'''[1] Beale Function
Global Minima f(x) = 0 located at x = (3,0.5) ; x [-4.5,4.5]'''
def beale(x,y):
    h = np.power((1.5 - x + x*y),2) + np.power((2.25 - x + x*(np.power(y,2))),2) + np.power((2.625 - x + x*(np.power(y,3))),2)
    a = 0.000000000000000001
    return 1/(h + a)

def beale_global_minima(x,y):
    return np.power((1.5 - x + x*y),2) + np.power((2.25 - x + x*(np.power(y,2))),2) + np.power((2.625 - x + x*(np.power(y,3))),2)

'''[2] BohachevskyN1 Function
Global Minima f(x) = 0 located at x = (0,0); x [-100,100]'''
def bohanchevsky(x,y):
    h = np.power(x,2) + 2 * np.power(y,2) - 0.3 * np.cos(3*np.pi*x) - 0.4 * np.cos(4*np.pi*y) + 0.7
    a = 0.000000000000000001
    return 1/(h + a)

def bohanchevsky_global_minima(x,y):
    return np.power(x,2) + 2 * np.power(y,2) - 0.3 * np.cos(3*np.pi*x) - 0.4 * np.cos(4*np.pi*y) + 0.7


'''[3] dropWave Function
Global Minima f(x) = -1 located at x = (0,0); x [-5.2;5.2]'''
def dropWave(x,y):
    h = -1 * (1 + np.cos(12 * np.sqrt(np.power(x,2)+np.power(y,2)))) / (0.5 * (np.power(x,2) + np.power(y,2)) +2)
    a = 0.000000000000000001
    return 1/(h + a)

def dropWave_global_minima(x,y):
    return -1 * (1 + np.cos(12 * np.sqrt(np.power(x,2)+np.power(y,2)))) / (0.5 * (np.power(x,2) + np.power(y,2)) +2)

'''[4] easom Function
Global Minima f(x) = -1 located at x = (pi,pi); x [-100;100] y [-100;100]'''
def easom(x,y):
    h = -1*np.cos(x)*np.cos(y)*np.exp(-1 * np.power((x - np.pi),2) - np.power((y - np.pi),2))
    a = 0.000000000000000001
    return 1/(h + a)

def easom_global_minima(x,y):
    return -1*np.cos(x)*np.cos(y)*np.exp(-1 * np.power((x - np.pi),2) - np.power((y - np.pi),2))

'''[5] egg_create Function
Global Minima f(x) = 0 located at x = (0,0); x [-5;5]'''
def egg_create(x,y):
    h = np.power(x,2) + np.power(y,2) + 25 * (np.power(np.sin(x),2) + np.power(np.sin(y),2))
    a = 0.000000000000000001
    return 1/(h + a)

def egg_create_global_minima(x,y):
    return np.power(x,2) + np.power(y,2) + 25 * (np.power(np.sin(x),2) + np.power(np.sin(y),2))

'''[6] schafferN3 Function
Global Minima f(x) = 0.00156685 located at x = (0,1.253115); x [-100;100]'''
def schafferN3(x,y):
    numeratorcomp = np.power((np.sin(np.cos(np.abs((np.power(x,2) - np.power(y,2)))))),2) - 0.5
    denominatorcomp = np.power((1 + 0.001 * (np.power(x,2) + np.power(y,2))),2)
    h = 0.5 + numeratorcomp/denominatorcomp
    a = 0.000000000000000001
    return 1/(h + a)

def schafferN3_global_minima(x,y):
    numeratorcomp = np.power((np.sin(np.cos(np.abs((np.power(x,2) - np.power(y,2)))))),2) - 0.5
    denominatorcomp = np.power((1 + 0.001 * (np.power(x,2) + np.power(y,2))),2)
    h = 0.5 + numeratorcomp/denominatorcomp
    return h

'''[7] kaene Function
Global Minima f(x) = 0.673667521146855 located at x= (1.393249070031784;0); x=(0;1.393249070031784) , x[0,10] '''
def kaene(x,y):
    numeratorcomp = np.power(np.sin(x-y),2) * np.power(np.sin(x+y),2)
    denominatorcomp = np.sqrt(np.power(x,2)+np.power(y,2))
    h = -1 * numeratorcomp/denominatorcomp
    a = 0.000000000000000001
    return 1/(h + a)

def kaene_global_minima(x,y):
    numeratorcomp = np.power(np.sin(x-y),2) * np.power(np.sin(x+y),2)
    denominatorcomp = np.sqrt(np.power(x,2)+np.power(y,2))
    h = -1 * numeratorcomp/denominatorcomp
    return h

#================================one variable================================

'''[8] bird Function
Global Minima f(x) = -106.764537 located at x = (4.70104,3.15294) and x = (-1.58214,-3.13024); x [-2pi;2pi]'''
def bird(x,y):
    h = np.sin(x)*np.exp(np.power((1-np.cos(y)),2)) + np.cos(y)*np.exp(np.power((1-np.sin(x)),2)) + np.power((x-y),2)
    a = 0.000000000000000001
    return 1/(h + a)

def bird_global_minima(x):
    return np.sin(x)*np.exp(np.power((1-np.cos(y)),2)) + np.cos(y)*np.exp(np.power((1-np.sin(x)),2)) + np.power((x-y),2)

'''[9] bartelsConn Function
Global Minima f(x) = -1 located at x = (0,0); x [-500,500]'''
def bartelsConn(x,y):
    h = np.abs(np.power(x,2) + np.power(y,2) + x*y) + np.abs(np.sin(x)) + np.abs(np.con(y))
    a = 0.000000000000000001
    return 1/(h + a)

def bartelsConn_global_minima(x,y):
    return np.abs(np.power(x,2) + np.power(y,2) + x*y) + np.abs(np.sin(x)) + np.abs(np.con(y))

'''[10] ackleyn3 Function
Global Minima f(x) = -195.629028238419 located at x = (-+0.682584587365898,-0.36075325513719); x [-32;32]'''
def ackleyn3(x,y):
    h = -1*200*np.exp(-1*0.02 * np.sqrt(np.power(x,2)) + np.power(y,2))+ 5*np.exp(np.cos(3*x) + np.sin(3*y))
    a = 0.000000000000000001
    return 1/(h + a)

def ackleyn3_global_minima(x,y):
    return -1*200*np.exp(-1*0.02 * np.sqrt(np.power(x,2)) + np.power(y,2))+ 5*np.exp(np.cos(3*x) + np.sin(3*y))