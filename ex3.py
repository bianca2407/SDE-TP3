list=["banana","mar","kiwi","piersica","capsuna"]
list.sort()
for i in range (0,len(list)):
    print(list[i] + str(len(list[i])))

list.append("rosu")
list.append("verde")
list.append("albastru")
list.reverse()
print(list)