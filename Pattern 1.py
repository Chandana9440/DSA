'''    * 
      * *
     * * *
    * * * *
   * * * * * '''

def pyramid(n):
    for i in range(n):
        # To print spaces
        for j in range(n - i - 1):
            print(" ", end="")
        
        # To print stars
        for j in range(i + 1):
            print("*",end=" ")
        
        # To move to the next line after each row
        print()

n = 5
pyramid(n)
