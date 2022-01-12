class Solution:
    def isValid(self, s: str) -> bool:
        length = len(s)
        if length % 2 != 0:
            return False
        stack = []
        for i in s:
            if i == '(':
                stack.append(i)
            elif i == '{':
                stack.append(i)
            elif i == '[':
                stack.append(i)

            print(stack.pop())
            if len(stack) > 0:
                if i == ')':
                    if stack[-1] == '(':
                        stack.pop()
                    else:
                        return False
                elif i == '}':
                    if stack[-1] == '{':
                        stack.pop()
                    else:
                        return False
                elif i == ']':
                    if stack[-1] == '[':
                        stack.pop()
                    else:
                        return False
            else:
                return False
        if len(stack) > 0:
            return False
        return True


def main():
    string = "()"
    s = Solution()
    print(s.isValid(string))


main()
