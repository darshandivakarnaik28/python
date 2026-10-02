def count_substring(string, sub_string):
    count=0
    l=len(sub_string)
    if 1<=len(string)<=200:
        for i in range(len(string)):
            if string[i:l]==sub_string:
                count+=1
                l+=1
            else:
                l+=1
    return count        
if __name__ == '__main__':
    string = input().strip()
    sub_string = input().strip()
    
    count = count_substring(string, sub_string)
    print(count)