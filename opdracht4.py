products = ['appel', 'aap', 'opa', 'bompa', 5, True, True]

def frequency(array_list):
    frequencies = {}
    for entry in array_list:
        if not entry in frequencies:
            frequencies[entry] = 1
        else:
            frequencies[entry] += 1
    return frequencies

print(frequency(products))