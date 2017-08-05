# Problem 1, Even Fibonacci numbers
# 2017-08-05
# Answer : 4613732

def solve_p2():
	first = 1; second = 2; third = 0;
	sumEven = second
	while third <= 4000000:
		third = first + second		
#		print(first, second, third)
		if third % 2 == 0 : sumEven += third
		first = second; second = third
	print("result :", sumEven)

solve_p2()
