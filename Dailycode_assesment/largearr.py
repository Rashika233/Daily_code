def largest(arr):
    max=arr[0]
    for i in range(len(arr)):
        if arr[i]>max:
            max=arr[i]
    return max
arr=[243,45,23,100,1000,1000]
print(largest(arr))