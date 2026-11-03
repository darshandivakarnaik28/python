class MyMap:

    def insert(self, mp, x, y):
        mp[x] = y

    def get(self, mp, x):
        return mp.get(x, -1)

    def size(self, mp):
        return len(mp)

    def remove(self, mp, x):
        mp.pop(x, None)