
intArray = [ 1, 4, 6, 7, 12, 15, 23, 25, 28, 29, 30 ]
searchNumber = 28

def binarySearch (intArray, start, end, searchNumber):
    # check if array has more than one element
    if end >= start:
        # calculate middle of array
        mid = start + (end - start) // 2
        # If searchNumber is found at the middle postion
        if intArray[mid] == searchNumber:
            return mid
        # If mid > searchNumber, select left half of intArray
        elif intArray[mid] > searchNumber:
            return binarySearch(intArray, start, mid-1, searchNumber)
        # else select right half intArray
        else:
            return binarySearch(intArray, mid + 1, end, searchNumber)
    else:
        # searchNumber not found in the intArrayay
        return -1
  
result = binarySearch(intArray, 0, len(intArray)-1, searchNumber)
  
if result != -1:
    print ("Element is found  at index % d" % result)
else:
    print ("Element is not found")

