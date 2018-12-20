def calc_max(M):
    max = None
    for val in M:
        if max == None or max < val:
            max = val
    return max

def solution(A):
    # write your code in Python 3.6
    max_val = None
    res_pos = -1
    curr_res_diff = -1
    i= 0
    while i < len(A)-1:
        if max_val is None or max_val < A[i]:
            max_val = A[i]
        diff = abs(max_val - calc_max(A[i+1:]))
        
        if (res_pos == -1) or (curr_res_diff < diff):
            res_pos = i
            curr_res_diff = diff
            
        i= i + 1
    
    return curr_res_diff


print(solution([1,3,-3]))