def OutPlace(arr):
  for i in range(1, len(arr)):
    arr1 = []
    ele = arr[i]
    j = i - 1
    while ele < arr[j] and j >= 0:
      arr1.insert(0, arr[j])
      j = j - 1
    arr1.insert(0, ele)
    while j != -1:
      arr1.insert(0, arr[j])
      j = j - 1
    j = i + 1
    while j != len(arr):
      arr1.append(arr[j])
      j = j + 1
    arr = arr1
  return arr
    
arr = [6,8,9,1,2,10,7,3,11]
print(OutPlace(arr))