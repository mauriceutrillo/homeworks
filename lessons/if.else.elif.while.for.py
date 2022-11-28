""" n = 20

if n%20==0:
    print("ეს რიცხვი ლუწია")
else:
    print("ეს რიცხვი კენტია")


x = -2

if x>0:
    print("ეს რიცხვი დადებითია")
elif x<0:
    print("ეს რიცხვი უარყოფითია")
else:
    print("ეს რიცხვი უდრის 0-ს")
  """

#####################################

#loops


""" x = 100
y = 0

while y<x:   #while loop - მანამ სანამ
    print(y)
    y = y + 1
 """


numbers = []

for i in range(100):
    numbers.append(i**2)

print(numbers)