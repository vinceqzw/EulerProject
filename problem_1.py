# Goal: Find the sum of all the multiples of 3 or 5 below 1000
# Author: Vince
# Date: May 20, 2017
# Version: 1.0


# Use function to find the multiples of x or y below z

def sumProblemString(x, y, z):
    Ix = 1
    Sx = 0
    Mx = 0
    for Mx in range (0, z):
        Sx = Mx + Sx
        Mx = x * Ix
        Ix = Ix + 1
    print Sx

    Iy = 1
    Sy = 0
    My = 0
    for My in range (0, z):
        Sy = My + Sy
        My = y * Iy
        Iy = Iy + 1
    print Sy

    Ixy = 1
    Sxy = 0
    Mxy = 0
    for Mxy in range (0, z):
        Sxy = Mxy + Sxy
        Mxy = (x*y) * Ixy
        Ixy = Ixy + 1
    print Sxy

    sum = Sx + Sy - Sxy

    return 'The sum of {} and {} below {} is {}.'.format(x, y, z, sum)

def main():
    print(sumProblemString(3, 5, 1000))
    a = int(input("Enter first integer: "))
    b = int(input("Enter second integer: "))
    c = int(input("Enter the range: "))
    print(sumProblemString(a, b, c))

main() 
    



# Find the sum of all multiples of 3 below 1000
i = 1
S3 = 0
M3 = 0
while M3 < 1000:
    S3 = M3 + S3
    M3 = 3 * i
    i = i + 1

# Find the sum of all multiples of 5 below 1000
j = 1
S5 = 0
M5 = 0
while M5 < 1000:
    S5 = M5 + S5
    M5 = 5 * j
    j = j + 1

# Find the sum of all multiples of 15 below 1000
k = 1
S15 = 0
M15 = 0
while M15 < 1000:
    S15 = S15 + M15
    M15 = 15 * k
    k += 1

# Print final result
print (S3 + S5 - S15)

# Print sub result
print S3
print S5
print S15