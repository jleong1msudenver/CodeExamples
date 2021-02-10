# Take a string as an input and, using a for loop, print the reverse of the string.

# Hint: in what direction should the loop go? 

s = input("Enter a string:")
step = -1
stop = -1
start = len(s) - 1
for k in range(start,stop,step):
    print(s[k])