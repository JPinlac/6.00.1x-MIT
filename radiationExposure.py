'''
def f(x):
    import math
    return 10*math.e**(math.log(0.5)/5.27 * x)
    '''
def f(x):
    import math
    return 400*math.e**(math.log(0.5)/3.66 * x)
    
def radiationExposure(start, stop, step):
    '''
    Computes and returns the amount of radiation exposed
    to between the start and stop times. Calls the 
    function f (defined for you in the grading script)
    to obtain the value of the function at any point.
 
    start: integer, the time at which exposure begins
    stop: integer, the time at which exposure ends
    step: float, the width of each rectangle. You can assume that
      the step size will always partition the space evenly.

    returns: float, the amount of radiation exposed to 
      between start and stop times.
    '''
    exposure=0
    for x in drange(start,stop,step):
        exposure+=f(x)*step
    print exposure
    return exposure
def drange(start, stop, step):
     r = start
     while r < stop:
     	yield r
     	r += step
radiationExposure(0, 4, 0.25)
