def ft_count_harvest_iterative():
	print("Days until harvest:", end=" ")
	time = int(input())
	for i in range(1, time + 1):
		print("Day", end=" ")
		print(i)
	print("Harvest time!")
