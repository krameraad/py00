def counter(count, max):
    print("Day", count)
    if count == max:
        return
    counter(count + 1, max)


def ft_count_harvest_recursive():
    print("Days until harvest:", end=" ")
    counter(1, int(input()))
    print("Harvest time!")
