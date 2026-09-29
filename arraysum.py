n = int(input("Enter the number of elements: "))
array = []
print(f"Enter {n} integers: ")
for i in range(n):
    element = int(input(f"Element {i+1}: "))
    array.append(element)
total_sum = sum(array)
print(f"Elements of the array are: {array}")
print(f"Sum of all elements is: {total_sum}")
