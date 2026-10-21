Given N number  of queries, implement a dictionary where key represents the student name and value represents the student's marks .
Each query can be one of the following three types:

1- Insert (i key value):
    Insert the given key with its corresponding value into the dictionary.
    The driver code will print "Inserted" after successful insertion.
2- Delete (d key):
    Delete the entry corresponding to the given key from the dictionary.
    Return True if the key exists and is deleted successfully (driver prints "Deleted").
    Return False if the key does not exist (driver prints "-1").
3- Print (p key):
    Print the marks of the given student in the following format:
    "Marks of <student name> is : <marks>".
    Return True if the key exists and the marks are printed successfully.
    Return False if the key does not exist (driver prints "-1").

Implement the following functions:
 insert_dict(query, dict)→ inserts a key-value pair into the dictionary.
 del_dict(query, dict)→ deletes a key from the dictionary and returns a boolean.
 print_dict(query, dict)→ prints the student's marks and returns a boolean. 

Example:

Input:
N = 5
i geeks 100
i for 200
d geeks
i geeks 300
p geeks
Output:
Inserted
Inserted
Deleted
Inserted
Marks of geeks is 300
Explanation:
For first four queries, insert and del operation happens, correspondingly Inserted And Deleted is printed. For the last query, marks of geeks is printed.
Constraints:
1 ≤ N ≤ 104
1 ≤ marks ≤ 104