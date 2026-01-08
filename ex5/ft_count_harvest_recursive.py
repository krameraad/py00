def ft_count_harvest_recursive():

    def counter(count, max):
        print("Day", count)
        if count != max:
            counter(count + 1, max)

    counter(1, int(input("Days until harvest: ")))
    print("Harvest time!")
