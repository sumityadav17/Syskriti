#  Taking input
N = int(input("Enter value of N: "))

#  Use 2 for loops for rows and columns N*N matrix
for row in range(N):
    for col in range(N):
        
        #  Apply conditions
        if row == col:
            print("X", end=" ")
        
        elif (row + col) % 2 == 0:
            print("1", end=" ")
        
        else:
            print("0", end=" ")

  
