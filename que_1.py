user=str(input("Enter a string: "))
char = dict.fromkeys(user,0)
for each in user:
    char[each] += 1
print(char)