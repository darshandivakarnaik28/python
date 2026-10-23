# Function to create dictionary
# arr is list of tuple. tuple contain name and marks.


def create_dict(arr):

    dict = {}

    for i in arr:
        dict[i[0]]=i[1]
        
    # Hint: use loop to iterate through arr
    # and assign key value to the dict

    return dict