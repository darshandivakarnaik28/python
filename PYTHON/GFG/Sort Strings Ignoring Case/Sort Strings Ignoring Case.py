class Solution:
    def sortByComparator(self, arr: list[str]) -> None:
        arr.sort(key=str.lower)