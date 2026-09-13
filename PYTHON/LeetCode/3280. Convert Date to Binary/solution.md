class Solution:
    def convertDateToBinary(self, date: str) -> str:
        year=int(date[0:4])
        month=int(date[5:7])
        dat=int(date[8:10])
        return f"{year:b}-{month:b}-{dat:b}"




