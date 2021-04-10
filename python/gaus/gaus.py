
# array with 9 elements
numbers = [10, 1, 2, 3, 6, 4, 7, 9, 8]

# function for calculating sum n-elements
def gaus_sum(n):
    return (n*(n+1)) / 2

# calculate sum of elements numbers array
tot_numbers = sum(numbers)

# calculate total sum of numbers array + 1
tot_entire_array = gaus_sum(len(numbers)+1) 

# answer is difference of sum entire array and nummber array
print(tot_entire_array-tot_numbers)


