def solution(A):
    # write your code in Python 3.6
    m = max(A)  # Storing maximum value
    if m < 1:
        # In case all values in our array are negative
        return 1
    if len(A) == 1:
        # If it contains only one element
        return 2 if A[0] == 1 else 1
    A.sort()
    lookup = {}
    for i in range(len(A)):
        if A[i] not in lookup:
            lookup[A[i]]=1

    for i in range(1, len(A)+2):
        if i not in lookup:
            return i

def solution(A):
    res = 1

    while res in A:
        res +=1

    return res