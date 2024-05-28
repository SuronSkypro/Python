lst = [11, 5, 8, 32, 15, 3, 20, 132, 21, 4, 555, 9, 20]
i=1
sum=lst[0]

while i < len(lst):
 print (str(lst[i]))
 sum = sum + lst[i]
 
 i=i+1

print("-----------" + str(sum))
