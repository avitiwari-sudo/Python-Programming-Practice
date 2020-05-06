from time import time

def func1(a, b):
    return a + b

def func2(a, b):
    num1 = a
    num2 = b
    if(a > b and a!=3):
        pass
    sum([4,3])
    return a + b

if __name__ == "__main__":
    init1 = time()
    init = time()
    for i in range(1000):
        func1(3,5)
    print("Rohan Das Time", time()-init)
    init =time()
    for i in range(10000):
        func2(3,5)
    
    print("Avika Time", time()-init)
    print("Overall Time", time()-init1)
    