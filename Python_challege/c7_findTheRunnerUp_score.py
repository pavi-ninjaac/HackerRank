"""
Given the participants' score sheet for your University Sports Day, you are required to find the runner-up score. You are given  scores. Store them in a list and find the score of the runner-up.
Sample Input 

5
2 3 6 6 5
Sample Output

5
"""

import time
if __name__ == '__main__':
    start=time.time()
    n = int(input("enter the value"))
    arr = list(map(int, input().split()))
    first_larger=max(arr)
    num=arr.count(first_larger)
    for i in range(num):
        arr.remove(first_larger)
    second_larger=max(arr)
    print(second_larger)
    end=time.time()
    print(f"execution time is {end-start}") #7.96122234
    
"""
method 2
start=time.time()
start=time.time()
n = int(input("enter the value"))
arr = list(map(int, input().split()))
arr.sort()
print(arr[-2])
end=time.time()
print(f"execution time is {end-start}") # 10.4567635
"""
