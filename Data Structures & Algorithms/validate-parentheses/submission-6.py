class Solution:
    def isValid(self, s: str) -> bool:
        dict1 = {")":"(", "}":"{", "]":"["}
        stack = []
        for i in s:
            if i in "({[":
                stack.append(i)
            elif i in ")}]":
                if not stack or stack[-1] != dict1[i]:
                    return False
                stack.pop()
        return len(stack) == 0
