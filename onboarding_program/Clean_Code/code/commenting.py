# Complex algorithm without proper comments
def knapsack_01_bad(weights, values, capacity):
    """
    This is an extremely complex algorithm: a classic dynamic programming problem that's genuinely hard to 
    understand without proper comments explaining the logic and state transitions.
    """
    n = len(weights)
    dp = [[0] * (capacity + 1) for _ in range(n + 1)]
    
    for i in range(1, n + 1):
        for w in range(capacity + 1):
            if weights[i-1] <= w:
                dp[i][w] = max(dp[i-1][w], dp[i-1][w - weights[i-1]] + values[i-1])
            else:
                dp[i][w] = dp[i-1][w]
    
    # backtrack
    selected = []
    i, w = n, capacity
    while i > 0 and w > 0:
        if dp[i][w] != dp[i-1][w]:
            selected.append(i-1)
            w -= weights[i-1]
        i -= 1
    
    return dp[n][capacity], selected[::-1]

# Before refactoring, the code was hard to understand and debug, and I cannot understand the logic of the code.
# After rewriting the comments, I can understand the logic of the code and the code is easier to understand and debug.

# Well-commented complex algorithm
def knapsack_01(weights, values, capacity):
    """
    Solves the 0/1 Knapsack problem using dynamic programming.
    
    The 0/1 Knapsack problem: Given items with weights and values,
    find the maximum value that can be obtained by selecting items
    without exceeding the weight capacity. Each item can only be used once.
    
    Algorithm:
    1. Create a 2D DP table where dp[i][w] represents the maximum value
       achievable using the first i items with capacity w
    2. For each item, decide whether to include it or not
    3. If item fits (weights[i-1] <= w): take max of including vs excluding
    4. If item doesn't fit: exclude the item (use previous value)
    5. Backtrack through the table to find which items were selected
    
    Args:
        weights: List of item weights
        values: List of item values
        capacity: Maximum weight capacity
        
    Returns:
        tuple: (maximum_value, list_of_selected_item_indices)
        
    Example:
        >>> knapsack_01([2, 1, 3], [4, 2, 3], 4)
        (6, [0, 1])  # Items 0 and 1 give value 6 with weight 3
    """
    n = len(weights)
    # dp[i][w] = maximum value achievable using first i items with capacity w
    dp = [[0] * (capacity + 1) for _ in range(n + 1)]
    
    # Fill the DP table
    for i in range(1, n + 1):
        for w in range(capacity + 1):
            # Check if current item can fit in capacity w
            if weights[i-1] <= w:
                # Take maximum of: including item i vs excluding item i
                # Including: dp[i-1][w - weights[i-1]] + values[i-1]
                # Excluding: dp[i-1][w]
                dp[i][w] = max(dp[i-1][w], dp[i-1][w - weights[i-1]] + values[i-1])
            else:
                # Item doesn't fit, so exclude it (use value from previous row)
                dp[i][w] = dp[i-1][w]
    
    # Backtrack to find which items were selected
    selected = []
    i, w = n, capacity
    while i > 0 and w > 0:
        # If current value differs from value without this item,
        # then this item was included in the optimal solution
        if dp[i][w] != dp[i-1][w]:
            selected.append(i-1)  # Add item index (convert to 0-based)
            w -= weights[i-1]     # Reduce remaining capacity
        i -= 1  # Move to previous item
    
    return dp[n][capacity], selected[::-1]  # Reverse to get correct order
