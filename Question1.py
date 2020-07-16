import numpy  
import random  

A = [] 
B = [] 


def DotProduct(N, ListA, ListB):
   
    for i in range(N):  
        a = random.randint(1, 1000)  
        ListA.append(a)  
    for h in range(N):  
        b = random.randint(1, 1000)  
        ListB.append(b)  


    result = numpy.dot(ListA, ListB)  

    print("Size of Array:", N)
    print("ListA:", ListA)
    print("ListB:", ListB)
    print("Dot Product:", result)  


DotProduct(10, A, B)  
DotProduct(100, A, B)