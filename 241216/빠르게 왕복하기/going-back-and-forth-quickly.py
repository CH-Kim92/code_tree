number_people = int(input())
mat = []
asum = 0
bsum = 0
bmin = 100000
amin = 100000
bmax = 0 
aa = 0
for i in range(number_people):
    s = input().split(" ")
    a = int(s[0]) 
    b = int(s[-1])
    if b < bmin:
        bmin = b 
    if a < amin:
        amin = a
    if b > bmax:
        bmax = b 
        aa = a 
    asum += a 
    bsum += b 

if asum >= bsum:
    print(asum+bmin)
else:
    print(bsum+ a)
    