class Solution:
    def isValid(self, s: str) -> bool:
        brackets = {
            ")": "(",
            "]": "[",
            "}": "{"
        }
        br_stack = []
        for c in s:
            if c in brackets.values():
                br_stack.append(c) 
            if c in brackets:
                if br_stack and brackets[c] == br_stack[-1]:
                    br_stack.pop()
                else:
                    return False
        return not br_stack