def ft_count_harvest_iterative():
    time = int(input("Days until harvest: "))
    for i in range(1, time + 1):
        print("Day", i, end=" ")
    print("Harvest time!")
