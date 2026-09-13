def find_employees_role(name):
    for n in employees:
        fullname=n['first_name']+" "+n['last_name']
        if name == fullname:
            return n['role']
    return "Does not work here!"