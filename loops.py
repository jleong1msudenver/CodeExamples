# Take a string as an input and, using a for loop, print the reverse of the string.
# Hint: in what direction should the loop go? 

# s = input("Enter a string:")

# for k in range(len(s) - 1, -1, -1):
#     print(s[k])

# Problem 3
alist = [1,2,3,"hello",10.5,"Wow!"]

for s in range(len(alist)-1, -1, -1):
	print(alist[s])