#Cwiczenie innego zapisu for do generowania listy zioru i slownika

#1
x= [i/10 for i in range(11)]
print(x)
#2
y=[(i,i**2,i**3) for i in range(-10,11)]
print(y)
#3
zbior = {"aaa","dasd","asdwqdwd"}
z={x: len(x) for x in zbior}
print(z)

