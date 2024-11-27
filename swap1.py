def swap(a,b):
     temp=a
     a=b
     b=temp
     print(f"a={a}")
     print(f"b={b}")
    
     return(a,b)
 


#main fuction
a=int(input("enter a"))
b=int(input("enter b"))

swap(a,b)
print(f"a ={a}  b={b}")
