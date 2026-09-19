class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        cars = [(p, s) for p, s in zip(position, speed)]
        stack = []

        for p, s in sorted(cars, reverse=True):
            t = (target - p) / s

            if stack and t <= stack[-1]:
                continue

            stack.append(t)

        return len(stack)
