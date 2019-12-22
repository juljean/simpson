import numpy as np
import re
import pandas as pd
import plotly.graph_objs as go
from plotly.offline import plot
import math
re_answy=re.compile("\s{0,}y\s{0,}$")#comparing with tamplate func
re_answn=re.compile("\s{0,}n\s{0,}$")
inp_n=re.compile("\s{0,}[+]?\d{0,}\s{0,}$")#index,int
inp_float=re.compile("^[+-]{0,1}[0-9]{1,}[.]{0,1}[0-9]{0,}$")

def validation(text, pattern): #matches text and pattern, returns true/false
    return bool(pattern.match(text))
def func_inp():
    y=input("Enter the function:")
    return  y
def ans():
    answer=input("Do you want to continue(y/n)?")
    if validation(answer, re_answy):
        y=func_inp()
        a = a_val()
        b = b_val()
        N = N_val()
        simps(a,b,N,y)
    elif validation(answer, re_answn):
        print("Bye")
    else:
        print("You entered incorrect symbol, choose y or n")
        ans()

def N_val():#к-ство н%2=0
    n=input("Enter the integer value N, that >=1 and even:")
    if validation(n, inp_n):
        n=int(n)
        if n<1:
            print("You entered a wrong symbol. Try again.")
            del n
            n=N_val()
        elif n%2==1:
            print("You entered a wrong symbol. It must be even. Try again.")
            del n
            n=N_val()
    else:
        print("You entered incorrect input. Try again.")
        del n
        n=N_val()
    return n

def a_val():
    a=input("Enter a(lower bound):")
    if validation(a, inp_float):
        a=float(a)
    else:
        print("You entered incorrect input. Try again.")
        del a
        a=a_val()
    return a

def b_val():
    b=input("Enter b(upper bound):")
    if validation(b, inp_float):
        b=float(b)
    else:
        print("You entered incorrect input. Try again.")
        del b
        b=b_val()
    return b
y=func_inp()
a = a_val()
b = b_val()
N = N_val()

def simps(a,b,N,y):
    dx = (b-a)/N#step
    x = np.linspace(a, b, N + 1)
    f=eval(y)
    S = dx/3 * np.sum(f[0:-1:2] + 4*f[1::2] + f[2::2])#sums all list's elements with changes
    print("Answer is ",S)
    y = list(map(lambda t: t*t, x))
    tracel = go.Scatter(
        x=np.linspace(a, b, N + 1),
        y=y,
        mode="lines"
    )
    fog = dict(data=[tracel])
    plot(fog)
    ans()
    return S
simps(a,b,N,y)
tracel =go.Scatter(
    x=np.linspace(a, b, N + 1),
    y=y,
    mode = "lines"
)
fog = dict(data = [tracel])
plot(fog)