def InPlace(arr):
  for i in range(len(arr)-1):
    ele = arr[i+1]
    j = i
    while ele < arr[j] and j >= 0:
      temp = arr[j]
      arr[j] = ele
      arr[j+1] = temp
      j = j - 1

arr = [3,7,11,8,4,1,2,9,15]
InPlace(arr)
print(arr)