number_people = int(input())
mat = []
asum = 0
bsum = 0
min = 1000
for i in range(number_people):
    s = input().split(" ")
    a = int(s[0]) 
    b = int(s[-1])
    if b < min:
        min = b 
    asum += a 
    bsum += b 

if asum >= bsum:
    print(asum+min)
else:
    print(asum+ (bsum-asum))
    