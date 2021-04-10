# demonstration of lambda expression
def square(n):
    return n*n

numbers =  [0,1,2,4,8,16,32,64,128]

print(list(map(square, numbers)))

# with a lambda function (anonymous function)
print(list(map(lambda x: x*x, numbers)))



