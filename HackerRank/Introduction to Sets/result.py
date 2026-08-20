def average(array):
    a=set(array)
    sum=0
    for i in a:
        sum+=i
    n=len(a)
    avg=sum/n
    return avg

if __name__ == '__main__':
    n = int(input())
    arr = list(map(int, input().split()))
    result = average(arr)
    print(result)