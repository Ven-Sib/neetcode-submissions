class UndergroundSystem:
    def __init__(self):
        # maps id > (startstation, t)
        self.dict1 = {} 

        # maps (startstation, endstation) > [total,count]
        self.dict2 = {}

    def checkIn(self, id: int, stationName: str, t: int) -> None:
        self.dict1[id] = (stationName,t)
    def checkOut(self, id: int, stationName: str, t: int) -> None:
        station, time = self.dict1[id]
        route = (station,stationName)
        if route not in self.dict2:
            self.dict2[route] = [0,0]
        self.dict2[route][0] += t-time
        self.dict2[route][1] += 1

    def getAverageTime(self, startStation: str, endStation: str) -> float:
        total, count = self.dict2[(startStation,endStation)]
        return total/count
