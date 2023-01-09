A=[5000,1,2,1,5,6,7,525,2,5,25,2,6,26,4,6,246,42,62,6,46,2,64,2,62,6,426,246,246,246,264,26,1,426,24,624,62,46,24626,2,624]
suma = 4
l= 0
r = len(A)-1
verificador = False
A.sort()
while l<r and verificador == False:
    print(A[l],A[r])
    if (A[l] + A[r] == suma):
        print("si")
        verificador = True
    elif (A[l] + A[r] < suma):
        l += 1
    else:
        r -= 1
   
 
