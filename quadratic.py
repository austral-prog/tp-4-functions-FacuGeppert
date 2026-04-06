# Replace the "ANSWER HERE" for your answer

def roots(a, b, c):
    r1 = (-b + ((b ** 2 - (4 * a * c))**0.5)) / (2 * a)
    r2 = (-b - ((b ** 2 - (4 * a * c))**0.5)) / (2 * a)

    delta = b ** 2 - (4 * a * c)

    if delta < 0:
        return f"( )"

    elif delta == 0:
        return f"({r1})"

    else:
        return f"({r1}, {r2})"

def value_y(a, b, c, x):

    return (a*(x**2)) + (b*x) + c

def to_string(a, b, c):

    if (a == 0) and (b == 0):
        return f"f(x) = {c}"
    elif a == 0:
        return f"f(x) = {b} * X + {c}"
    elif b == 0:
        return f"f(x) = {a} * X^2 + {c}"
    else:
        return f"f(x) = {a} * X^2 + {b} * X + {c}"


def derivation(a, b, c):

    if a == 0 and b == 0:
        return f"f'(x) = 0"
    elif b == 0:
        return f"f'(x) = {2*a} * X"
    elif a == 0:
        return f"f'(x) = {b}"
    else:
        return f"f'(x) = {2*a} * X + {b}"
