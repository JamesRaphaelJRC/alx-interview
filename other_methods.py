''' METHOD 1: Explicit handling of edge cases.
    Easier to understand the logic
 '''
def pascal_triangle(n):
    ''' Pascal triangle '''
    if n <= 0:
        return []
    
    pascal = []
    prev_arr_idx = -1
    for i in range(1, n + 1):
        new = []
        for j in range(i):
            if prev_arr_idx < 0: # That means we are at the top of the triangle (has no prev array)
                val = 1
            else:
                prev_arr = pascal[prev_arr_idx]
                preceeding_idx = j - 1
                current_idx = j

                if preceeding_idx < 0 or current_idx >= len(prev_arr): # That means we are in the first or last element of the array
                    val = 1
                else:
                    val = prev_arr[preceeding_idx] + prev_arr[current_idx]
            new.append(val)
        pascal.append(new)
        prev_arr_idx += 1
    return pascal


''' METHOD 2: Using try-except block for edge cases.
    Uses a try-except block to catch IndexError and assumes it's at the top
    of the triangle, the end edge or an array that doesn't exist.
'''
def pascal_triangle(n):
    ''' Pascal triangle '''
    if n <= 0:
        return []
    
    pascal = []
    prev_arr_idx = -1
    for i in range(1, n + 1):
        new = []
        for j in range(i):
            try:
                prev_arr = pascal[prev_arr_idx]
                preceeding_idx = j - 1
                current_idx = j

                if preceeding_idx < 0:
                    val = 1
                else:
                    val = prev_arr[preceeding_idx] + prev_arr[current_idx]
            except IndexError:
                val = 1
            new.append(val)
        pascal.append(new)
        prev_arr_idx += 1
    return pascal
