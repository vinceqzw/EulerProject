i = 1
S3 = 0
M3 = 0
while M3 < 1000:
    S3 = M3 + S3
    M3 = 3 * i
    i = i + 1


j = 1
S5 = 0
M5 = 0
while M5 < 1000:
    S5 = M5 + S5
    M5 = 5 * j
    j = j + 1


k = 1
S15 = 0
M15 = 0
while M15 < 1000:
    S15 = S15 + M15
    M15 = 15 * k
    k += 1


print (S3 + S5 - S15)
print S3
print S5
print S15