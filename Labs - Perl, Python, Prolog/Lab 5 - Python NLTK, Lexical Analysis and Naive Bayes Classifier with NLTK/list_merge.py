#!/local/bin/python3

some_list = ["first_name", "last_name", "age", "occupation"]
some_tuple = ("John", "Holloway", 35, "carpenter")

result = dict(zip(some_list,some_tuple))
print(result)
 
