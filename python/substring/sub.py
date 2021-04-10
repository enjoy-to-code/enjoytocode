#
# Microsoft Interview Question
#
# Given an array of strings and a string x. Find no of strings in array which have prefix as x.
# Input: A={"Cisco","Citrix","Cipla"} ,x="Cit"
#      Output: 1
#     There is only 1 string "Citrix" 
#     which contains "Cit" as prefix.

A= {"Cisco","Citrix","Cipla"}
x = "Cit"
answer = 0

for str in A:
    if (x == str[0:3]):
        answer = answer+1

print(answer)

