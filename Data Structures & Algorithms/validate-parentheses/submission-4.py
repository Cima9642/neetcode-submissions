class Solution:

    def isValid(self, s: str) -> bool:
        # STEP 1: Initialize stack & map (Close -> Open)
        stack = []
        closeToOpen = {")": "(", "]": "[", "}": "{"}

        # STEP 2: Iterate through characters
        for c in s:
            # STEP 3: Handle Closing Bracket vs. Opening Bracket
            if c in closeToOpen:
                if stack and stack[-1] == closeToOpen[c]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(c)

        # STEP 4: Return True if stack is completely empty
        return not stack