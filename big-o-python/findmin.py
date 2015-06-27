def findmin(list):
    """Takes a number from a list and compares to a set min"""

    min = list[0] #Just a seed

    for item in list:
        if item < min:
            min = item
        else:
            pass

    return min

def findmin2(list):
    """Compares each item in the list to everything else. Continues only
    if it finds that the selected item is the minimum"""

    for item_1 in list:
        is_not_min = True #A seed value
        for item in list:
            if item_1 > item:
                break