from hashlib import new


fruits=["apple","orange","banana"]
fruits_2=["cherry","tomato"]
fruits.append("cherry")
print(fruits)
fruits.remove("cherry")
print(fruits)
my_fruits=fruits.pop(1)
print(fruits)
print(my_fruits)
fuits_3=fruits+fruits_2
fruits.extend(fruits_2)
print(fruits)
fruits_2.clear()
print(fruits_2)

fruits_4=["apple","orange","banana",]
print(fruits_4)
print(fruits_4[1])
new_list=list(fruits_4)
new_list.append("tomato")

fruits_4=tuple(new_list)
fruits_5={"apple","orange","orange","orange"}
print(fruits_5)