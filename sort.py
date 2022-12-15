#data = [4, -30, 100, -100, 123, 1, 0, -1, -4]

def abs_sort(data):
    return sorted(data, key=abs, reverse=True)


def abs_sort_lambda(data):
    return sorted(data, key = lambda x: abs(x), reverse = True)