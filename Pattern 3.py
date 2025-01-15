'''  *
    **
   ***
  ****
 ***** '''
# left Triangle star pattern
def pattern(n):
    for i in range(n):
        #To print spaces
        for j in range(n-i):
            print(" ",end="")
        for k in range(i+1):
            print("*",end="")
        # To print in next line
        print()

n=7
pattern(n)