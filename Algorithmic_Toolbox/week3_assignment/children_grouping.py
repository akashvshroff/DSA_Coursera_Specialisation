def group_children(ages):
    """
    Given a group of children of different ages, divide them into the least
    number of groups where, in each group, the difference between any 2 children
    is not more than 1 year.
    """
    ages.sort()
    groups = [[ages.pop(0)]]
    while ages:
        while ages and ages[0] - groups[-1][0] <= 1:
            groups[-1].append(ages.pop(0))
        if ages:  # there is some kid who can't be accomodated yet.
            groups.append([ages.pop(0)])
    return groups


print(group_children([1, 3, 2, 4, 5, 4, 2, 1, 2, 3, 9, 8, 7, 6.5,
                      6, 4, 3, 1, 2, 3, 4, 5, 6, 6, 5, 4, 3, 1.5, 2.5, 3.5]))
