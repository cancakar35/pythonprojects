maks = 0
maks_bolen = 1
for i in range(1000, 10000):
    bolen = 1
    for j in range(2, i+1):
        if i % j == 0:
            bolen += 1
    if bolen >= maks_bolen:
        maks_bolen = bolen
        maks = i

print(maks)
