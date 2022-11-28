""" #tupple

mytuple = (34, 23432, "tbc", "saburtalo", 23432)  #ტუპლში არ ხდება მონაცემის ჩანაცვლება ჩამატება და ა.შ.

print(mytuple)

mylist = list(mytuple)  #ამ ხერხით შეგვიძლია ტუპლის ლისტად გადაქცევა და შემდეგ მონაცემების შეცვლა ან ჩამატება

mylist[1] = "mariami" # მონაცემის შეცვლა

mylist.append(23) # მონაცემის ჩამატება

print(mylist)

mytuple = tuple(mylist) #ლისტის ისევ ტუპლად დაბრუნება

print(mytuple)


newtuple = (11, 45, "avto")

tupleadditional = newtuple + mytuple  # შეგვიძლია ორი სხვადასხვა ტუპლის გაერთიანება


print(tupleadditional) """

#key:value წყვილი

cars = {"brand":"bmw",
        "model":"m5",
        "color":"black",
      }

#print(cars["brand"])

cars["speed"] = ["200", "250", "300"]

#print(cars.keys())

#print(cars.values())

newcars = {"brand":"mercedes",
           "model":"gtr",
           "type":"coupe"
       }

cars.update(newcars)

print(cars)

