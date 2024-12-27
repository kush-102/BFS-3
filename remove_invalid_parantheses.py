class Solution:

    def removeInvalidParentheses(self, s: str) -> List[str]:
        # time complexity is n^n
        # space complexity is O(n)
        result = []
        visited = set()
        q = deque()
        q.append(s)
        visited.add(s)
        flag = False

        def isValid(string):
            count = 0
            for char in string:
                if char == "(":
                    count += 1
                elif char == ")":
                    count -= 1
                if count < 0:
                    return False
            return count == 0

        while q:
            size = len(q)
            for i in range(size):
                curr = q.popleft()
                if isValid(curr):
                    result.append(curr)
                    flag = True
                else:
                    if not flag:
                        for k in range(len(curr)):
                            # if char exists in bw
                            if curr[k].isalpha():
                                continue
                            baby = curr[:k] + curr[k + 1 :]
                            if baby not in visited:
                                visited.add(baby)
                                q.append(baby)
        return result if result else [""]

    # dfs method
    def __init__(self):
        self.result = []
        self.visited = set()
        self.maxi = float("-inf")

    def isValid(self, string):
        count = 0
        for char in string:
            if char == "(":
                count += 1
            elif char == ")":
                count -= 1
            if count < 0:
                return False
        return count == 0

    def removeInvalidParentheses(self, s: str) -> List[str]:
        self.dfs(s)
        return self.result

    def dfs(self, s):
        # base case
        if len(s) < self.maxi:
            return
        if self.isValid(s):
            if len(s) > self.maxi:
                self.result = []
                self.maxi = len(s)
            self.result.append(s)
            return
        # logic
        for k in range(len(s)):
            if s[k].isalpha():
                continue
            baby = s[:k] + s[k + 1 :]
            if baby not in self.visited:
                self.visited.add(baby)
                self.dfs(baby)

    # time complexity is O(2^n*n)
    # space complexity is O(2^n*n)
