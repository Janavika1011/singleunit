def print_unique_elements(arr):
    count = {}
    for i in arr:
        if i in count:
            count[i] += 1
        else:
            count[i] = 1
    
    for key, value in count.items():
        if value == 1:
            print(key)

arr = list(map(int, input("Enter : ").split()))
print_unique_elements(arr)
