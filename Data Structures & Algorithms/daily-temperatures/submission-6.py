class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        r =[0]*len(temperatures)
        stack = []

        for i in range(len(temperatures)):
            while stack and temperatures[i] > stack[-1][0]:
                val, index = stack.pop()
                r[index] = i-index
            stack.append([temperatures[i], i])
        return r
