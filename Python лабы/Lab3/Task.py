import random
import math
from datetime import date, datetime

def generate_param():
    arr = list()
    subarr = list()
    for i in range (random.randint(1,10)):
        for i in range (random.randint(1,10)):
            subarr.append(i)
        arr.append(subarr)
    return arr

def task1(*params:list):
    try:
        intersect = set(params[0])
        for j in params:
            intersect = intersect.intersection(j)
        print(intersect)
    except:
        print("Error: error in finding the intersection of set")
            
def reducer(m:int,n:int):
    gcd = math.gcd(m,n)
    return m/gcd,n/gcd

def M(m:int):
    if m == 0:
        return 0
    return m - F(M(m-1))

def F(f:int):
    if f == 0:
        return 1
    return f - M(F(f-1))

def hofstadter_f_m(n:int):
    for i in range(n):
        print((F(i),M(i)))

def nearest_date(*params):
    today = datetime.today()
    diff = abs(datetime.strptime(params[0],"%d.%m.%Y").date()-today.date())
    Date = datetime.strptime(params[0],"%d.%m.%Y").date()

    for i in range(len(params)):
        if abs(datetime.strptime(params[i],"%d.%m.%Y").date()-today.date()) < diff:
            Date = datetime.strptime(params[i],"%d.%m.%Y").date()
        if abs(datetime.strptime(params[i],"%d.%m.%Y").date()-today.date()) < diff:
            Date = max(Date,datetime.strptime(params[i],"%d.%m.%Y").date())
    print("date = ",Date.strftime("%d.%m.%Y"))




def main():
    #task1
    params = generate_param()
    task1(*params)

    #task2
    m = random.randint(1,100)
    n = random.randint(m+1,200)
    print(reducer(m,n))

    #task3
    n = int(input())
    hofstadter_f_m(n)

    #task4
    params = ["01.01.2050", "12.04.2011", "31.12.1970","03.11.2023","05.11.2023"]
    nearest_date(*params)

main()