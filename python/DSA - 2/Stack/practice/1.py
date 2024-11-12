# Given an array of temperatures, return an array answer such that answer[i] is the number of days you have to wait until a warmer temperature. 
# If there is no future day for which this is possible, keep answer[i] = 0.

# Example:

#     Input: [73, 74, 75, 71, 69, 72, 76, 73]
#     Output: [1, 1, 4, 2, 1, 1, 0, 0]

# Explanation: Use a stack to keep track of indices of days with temperatures. For each temperature, check if it's warmer than the temperature at the index 
# stored in the stack. If yes, calculate the difference and pop the stack.