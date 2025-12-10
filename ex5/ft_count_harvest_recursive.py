i = 0

def ft_count_harvest_recursive():
	if i == 0:
		i = int(input())
	print("Day", i)
	i -= 1
	if i == 0:
		print("Harvest time!")
		return
	ft_count_harvest_recursive()