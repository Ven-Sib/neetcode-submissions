class TimeMap:

    def __init__(self):
        self.hashmap = {}

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.hashmap:
            self.hashmap[key] = []
        self.hashmap[key].append([value, timestamp])


    def get(self, key: str, timestamp: int) -> str:
        result, values = '', self.hashmap.get(key,[])

        l, r = 0, len(values)-1
        while l <= r:
            mid = (l+r)//2
            if values[mid][1] <= timestamp:
                l = mid + 1
                result = values[mid][0]
            else:
                r = mid - 1
        return result


