# for Loop
# syntax------->seq = range(start,stop,step)

'''
range(start,stop,step):
-----------------------
> returns a sequnce of int values.
> start ->inclusive
> stop--> exculsive
> step(arge3)--> can not be zero

'''

seq = range(5,20,2)
for i in seq:
    print(i)
print(" --------------------------------------")

for i in range(1,20,2):
   print("rka : ",i)

print(" --------------------------------------")

for i in range(1,10,3):
   print("rka : ",i)

print(" --------------------------------------")

for i in range(1,4,1):
   print("rka : ",i)


print(" --------------------------------------")

for i in range(5,1,-1):
   print("rka : ",i)

print(" --------------------------------------")

for i in range(-5,-1,-1):
   print("rka : ",i)


print(" --------------------------------------")

for i in range(-1,-5,1): # empty sequence
   print("rka : ",i)

print(" --------------------------------------")

for i in range(5,5,1): # empty sequence
   print("rka : ",i)

print(" --------------------------------------")

for i in range(1,5,0): # error
   print("rka : ",i)



print(" --------------------------------------")

for i in range(5,5,.2): # error
   print("rka : ",i)


























   
