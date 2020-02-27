import numpy


'''Ackley N. 2 Function
Global Minima f(x) = -200 located at x = (0,0)'''
def ackley(x,y):
    h = -200 * numpy.exp(-0.02*numpy.sqrt((x ** 2) + (y **2)))
    a = 0.000000000000000001
    return 1/(h + a)

def ackley_global_minima(x,y):
    return -200 * numpy.exp(-0.02*numpy.sqrt((x ** 2) + (y **2)))