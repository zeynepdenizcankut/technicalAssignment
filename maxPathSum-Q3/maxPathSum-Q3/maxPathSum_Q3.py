
tri = [[int(s) for s in l.split()] for l in open('data.txt').readlines()]


def maxPathSum(tri):
    sum = 0
    r = -1 # Initial value of the reference value index
    for row in range(len(tri)): #iterate through the rows of the pyramid from top to bottom
        max = -1 # Initial value of max, reset at each row 
        if r == -1: #Top of the pyramid
            max = tri[row][0] #Value of the top of the pyramid
            r = 0
        else:
            for i in range(r,r+2): #Diagonally check the two bottom numbers
                if tri[row][i] > 1: 
                    for j in range(2,int(tri[row][i])):
                        if (tri[row][i] % j == 0) and tri[row][i] > max: #check if it's a prime number and if it's higher than the local maximum
                            max = tri[row][i] #set the number value as local maximum
                            r = i # set its index to be the reference index for the next row
                else: # if the integer number is 0 or 1:
                    if tri[row][i] > max: #check if it's higher than the local maximum value
                        max = tri[row][i]
                        r = i
            if max == -1: # if the two numbers are prime
              max = -10
        if max == -10: #check if both numbers are prime
          break
        else:
            #print (max)
            sum += max
    return sum
    

max_test = maxPathSum(tri)
print(max_test)