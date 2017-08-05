# Problem 1, Multiples of 3 and 5
# 2017-07-30
# Answer : 233168  

def solve_p1():
    sum = 0
    for i in range(1, 1000, 1):
        if (i % 3 == 0) or (i % 5 == 0):
        	sum = sum + i
    print("result :", sum)

solve_p1()
