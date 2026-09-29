n = int(input("Enter no. of elements: "))
array = []
print(f"Enter {n} elements: ")
for i in range(n):
    elt = int(input(f"Element {i+1}: "))
    array.append(elt)
array.sort()

print("Smallest element: ", array[0])
print("Second smallest element: ", array[1])
print("Second largest element: ", array[-2])
print("Largest element: ", array[-1])