from keyword import iskeyword

def contains_keyword(*str):
    for x in str:
        if iskeyword(x):
            return True;
    return False

print(contains_keyword('hello', 'goodbye')) 			 	                # print out: False
print(contains_keyword('def', 'haha', 'lol', 'chickens are evil', 42))  	# print out: True
print(contains_keyword('four', 'for', 'if'))  					            # print out: True
print(contains_keyword('blabla', 'doggo', 'crab', 'anchor'))  		        # print out: False
print(contains_keyword('grizzly', 'ignore', 'return', 'False'))  		    # print out: True

