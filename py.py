#nima
start = int(input("enter start number: "))
end = (int(input("enter end number: "))) + 1
numbers = list(range(start,end))
sum = 0
for number in numbers:
    sum = sum + number
print (sum)
tmp = input("enter any key to continue...")