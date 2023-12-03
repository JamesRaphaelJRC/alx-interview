''' The Pascals triangle '''


def pascal_triangle(n):
    ''' Defines the Pascal triangle

        res_idx = The index of the previous sub-list of the result list
                    initial value = -1 since there is no previous sub-list yet
        prev = index of the previous value in the res_idx list
        current = index of the current value in the res_idx list
    '''
    if type(n) != int or n <= 0:
        return []

    result = []
    res_idx = -1
    for i in range(1, n + 1):
        new = []
        for j in range(i):
            try:
                current = j
                prev = current - 1
                if prev < 0:
                    prev = 0
                    val = 1
                else:
                    val = result[res_idx][prev] + result[res_idx][current]
            except IndexError:
                val = 1
            new.append(val)
        result.append(new)
        res_idx += 1
    return result
