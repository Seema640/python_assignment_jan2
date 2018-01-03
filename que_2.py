my_list = [2,5,7,9,11,17,222]
item = int(input("Enter the number you want to search: "))

low = 0
high = len(my_list) - 1

found = False

while low <= high and found is False:
    mid = int((low + high) / 2)

    if my_list[mid] is item:
        print("Value found")
        found = True
    else:
        if my_list[mid]>item:
            high=mid-1
        else:
            low=mid+1

if found is False:
    print("The value is not found")
