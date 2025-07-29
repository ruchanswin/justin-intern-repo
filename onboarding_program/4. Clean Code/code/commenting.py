# Poor commented code example
def find_longest_increasing_subsequence_bad(nums):
    if not nums:
        return 0 # check

    dp = [1] * len(nums)
    # loop
    for i in range(1, len(nums)):
        for j in range(i):
            if nums[i] > nums[j]:
                dp[i] = max(dp[i], dp[j] + 1)

    return max(dp)

# Example of complex logic with clear comments
def find_longest_increasing_subsequence(nums):
    """
    Finds the length of the longest increasing subsequence in a list of numbers.
    Uses dynamic programming to solve the problem efficiently.
    """
    if not nums:
        return 0

    # dp[i] will hold the length of the longest increasing subsequence ending at index i
    dp = [1] * len(nums)

    # Iterate through the list, updating dp for each element
    for i in range(1, len(nums)):
        for j in range(i):
            # If nums[i] can extend the subsequence ending at nums[j]
            if nums[i] > nums[j]:
                # Update dp[i] if we found a longer subsequence ending at i
                dp[i] = max(dp[i], dp[j] + 1)

    # The result is the maximum value in dp
    return max(dp)
