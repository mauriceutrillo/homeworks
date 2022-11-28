mylist = [1, "dato", 2, 0, 0, 'gio'] #სიაში მონაცემების შეყვანა

print(mylist)

print(len(mylist)) #სიის ზომის დათვლა

print(mylist[4]) #ინდექსირება, ამ კოდით შესაძლებელია სიიდან კონკრეტულის ამოღება ინდექსის ნომრის მიხედვით. 

mylist.append(568) # მონაცემის ჩამატება სიაში

print(mylist)

mylist.pop() #შლის სიაში ბოლო ადგილზე მდებარე მონაცემს

print(mylist)

mylist.remove(1)

print(mylist)

mylist_set = set(mylist)  #სიის გადაკეთება სიმრავლედ

print(mylist_set)

myset = {"jaba", 10, "valeri"}

allinone = myset.union(mylist) #ორი სიმრავლის გაერთიანება.

#myset.update(mylist)

print(allinone)