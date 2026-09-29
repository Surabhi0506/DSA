n = int(input("Enter no. of elements: "))
array = []
count_even = 0
count_odd = 0
print(f"Enter {n} elements: ")
for i in range(n):
    num = int(input(f"Element {i+1}: "))
    array.append(num)

    if num % 2 == 0:
        count_even = count_even + 1
    else:
        count_odd = count_odd + 1
print("Number of even elements: ", count_even)
print("Number of odd elements: ", count_odd)
