class Solution:
    def simplifyPath(self, path: str) -> str:
        stack = []

        split_path = path.split("/")
        print(split_path)
        for p in split_path:
            if p == "..":
                if stack: stack.pop()
            elif p == "" or p == ".": continue
            else:
                stack.append(p)
        
        return "/" + "/".join(stack)