def list_manipulation(array_list, command, location, value = None):
    if command == 'remove':
        if location == 'beginning':
            print(array_list.pop(0))
        else:
            print(array_list.pop(len(array_list)-1))
    else:
        if location == 'beginning':
            array_list.insert(0,value)
            print(array_list)
        else:
            array_list.append(value)
            print(array_list)



list_manipulation([1, 2, 3], 'remove', 'end') 			# print out: 3
list_manipulation([1, 2, 3], 'remove', 'beginning')  		# print out: 1
list_manipulation([1, 2, 3], 'add', 'beginning', 20)  		# print out: [20, 1, 2, 3]
list_manipulation([1, 2, 3], 'add', 'end', 30)  			# print out: [1, 2, 3, 30]
