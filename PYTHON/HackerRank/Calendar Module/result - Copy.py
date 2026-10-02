# Enter your code here. Read input from STDIN. Print output to STDOUT
import calendar
n=input().split()
m=int(n[0])
d=int(n[1])
y=int(n[2])
i=calendar.weekday(y,m,d)
print(calendar.day_name[i].upper())
