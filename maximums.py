# Replace the "ANSWER HERE" for your answer

def max_of_two(x, y):
    """Given x and y, that are 2 numbers, return the biggest number."""

    if x > y:
        largest_number_2 = x
    else:
        largest_number_2 = y
    return largest_number_2 # Remove this line and implement

def max_of_three(x, y, z):
    """Given x, y and z, that are 3 numbers, return the biggest number of the three."""
    if (x > y) and (x > z):
        largest_number_3 = x
    elif (y > x) and (y > z):
        largest_number_3 = y
    else:
        largest_number_3 = z

    return largest_number_3
