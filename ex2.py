def prim(n):  
      for i in range (1,n):
          if i==0 or i==1:
              continue
          else:
            if(n%i==0):
                return False 
            return True

n=int(input("Introduce n:"))
for i in range (n+1):
    if prim(i):
        print(i)

