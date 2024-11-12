# Problem: Given a string containing just the characters '(', ')', '{', '}', '[', and ']', determine if the input string is valid. 
# An input string is valid if: - Open brackets are closed by the same type of brackets. - Open brackets are closed in the correct order.

# Example:

#     Input: "()[]{}"
#     Output: True
#     Input: "(]"
#     Output: False

# Explanation: Use a stack to keep track of open parentheses. Push each open bracket onto the stack, and for each close bracket, check if it matches the one on the stack. 
# If there’s a mismatch or unbalanced count, return false.

s = '{({}{({[[(([]))]]})})}'
cb_o = 0
cb_c = 0
p_o = 0
p_c = 0
sb_o = 0
sb_c = 0
for i in range(len(s)):
    if s[i] == '{':
        cb_o += 1
    elif s[i] == '}':
        cb_c += 1
    elif s[i] == '[':
        sb_o += 1
    elif s[i] == ']':
        sb_c += 1
    elif s[i] == '(':
        p_o += 1
    elif s[i] == ')':
        p_c += 1
        print(p_c)
    else:
        pass
print( f'curly: {cb_o}, {cb_c} | Square: {sb_o}, {sb_c} | paranthesis: {p_o}, {p_c}')
if cb_o == cb_c and p_o == p_c and sb_o == sb_c:
    print('True')
else:
    print('False')