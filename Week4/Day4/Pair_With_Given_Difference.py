class Solution:
    # @param A : list of integers
    # @param B : integer
    # @return an integer
    def solve(self, A, B):
        start = 0
        end = 1
        A.sort()
        n = len(A)
        
        while start < n and end < n:
            if start != end:
                diff = A[end] - A[start]
                if diff == B:
                    return 1
                elif diff < B:
                    end += 1
                else:
                    start += 1
            else:
                end += 1
        return 0
