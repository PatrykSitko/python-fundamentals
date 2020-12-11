group_of_people = ['Alex', 'Eliot', 'Veronica', 'Lucy', 'Wouter', 'Bart']

#standard 
def startswith(array_list,str):
    filtered_array_list = []
    for entry in array_list:
        if str in entry[0:len(str)]:
            filtered_array_list.append(entry)
    return filtered_array_list

print(startswith(group_of_people,'A'))

#list comprehension
def _startswith(array_list,str):
    return [entry for entry in array_list if str in entry[0:len(str)]]

print(_startswith(group_of_people,'A'))