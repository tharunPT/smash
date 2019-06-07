b=int(input())
if((b%4)==0):
    print("Yes")
elif((b%400)==0)and (b%100)==0:
   print("Yes")
else:
  print("no")
