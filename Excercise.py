myRow = {3,4,5,7,8,9}
print(myRow)

# myRow.append(9)
# print(myRow)
#
# myRow.insert(0, 99)
# print(myRow)

myRow[0] +=1
print(myRow)

newRow = [3]
print(myRow + newRow)

myRow += [32]
print(myRow)

myRow.extend([5,6,8,9,0])
print(myRow)

myRow.pop(1)
print(myRow)

myRow.pop()
print(myRow)

myRow.pop(6)
print(myRow)

names = ["Titi", "Wales", "Toy"]
print(names)

names_joined = "-".join(names)
print(names_joined)

names_joined = "*".join(names)
print(names_joined)

