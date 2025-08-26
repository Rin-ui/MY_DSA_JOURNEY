class Solution:
    def findPages(self, arr, k):
        # code here
        n = len(arr)
        # if there are more students than books (or no books / no students) it's impossible
        if n == 0 or k == 0 or k > n:
            return -1

        start = max(arr)
        end = sum(arr)
        ans = -1
        while start <= end:
            mid = (start + end) // 2
            pages = 0
            student = 1   # start with student 1
            # to add pages of book from the array
            for i in range(n):
                if pages + arr[i] > mid:
                    # go to next student
                    student += 1
                    pages = arr[i]
                else:
                    pages += arr[i]
            if student <= k: # student not exceeded the range
                ans = mid
                end = mid - 1
            else: # student exceeded the range
                start = mid + 1
        return ans
