# insert into dictionary
def insert_dict(query, dict):
    name=query[1]
    dict[name]=query[2]
    return "Inserted"

# deleting from dictionary
def del_dict(query, dict):
    name=query[1]
    del dict[name]
    return "Deleted"
    

# print marks of required name
def print_dict(key, dict):
    if key in dict:
        print("Marks of",key,"is",dict[key])
    else:
        print("-1")
