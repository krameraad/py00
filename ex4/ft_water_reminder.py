def ft_water_reminder():
	print("Days since last watering:", end=" ")
	time = int(input())
	if time > 2:
		print("Water the plants!")
	else:
		print("Plants are fine")
