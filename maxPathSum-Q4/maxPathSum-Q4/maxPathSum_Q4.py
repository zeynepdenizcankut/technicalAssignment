
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

tri = [ [215],
        [193, 124],
        [117, 237, 442],
        [218, 935, 347, 235],
        [320, 804, 522, 417, 345],
        [229, 601, 723, 835, 133, 124],
        [248, 202, 277, 433, 207, 263, 257],
        [359, 464, 504, 528, 516, 716, 871, 182],
        [461, 441, 426, 656, 863, 560, 380, 171, 923],
        [381, 348, 573, 533, 447, 632, 387, 176, 975, 449],
        [223, 711, 445, 645, 245, 543, 931, 532, 937, 541, 444],
        [330, 131, 333, 928, 377, 733, 17, 778, 839, 168, 197, 197],
        [131, 171, 522, 137, 217, 224, 291, 413, 528, 520, 227, 229, 928],
        [223, 626, 34, 683, 839, 53, 627, 310, 713, 999, 629, 817, 410, 121],
        [924, 622, 911, 233, 325, 139, 721, 218, 253, 223, 107, 233, 230, 124, 233]]
 
max_test = maxPathSum(tri)
print(max_test)