

# for i,a in enumerate(x,0):
#     for j,b in enumerate(x,0):
#         text = text+str(f"{(i*j):5}")
#     print(text)
#     text=""
print("   ",end="")
for k in range(10):
    print(f"{k:5}",end="")

print()
print()
for i in range(0,10,1):
    print(i,end="  ")
    for j in range(0,10,1):
        print(f"{j*i:5}",end="")
    print()