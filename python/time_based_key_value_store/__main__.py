import unittest

class TimeMap:

    def __init__(self):
        self.store = {} # keys : values[[]]
    
    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.store:
            self.store[key] = []
        self.store[key].append([value,timestamp])

    def get(self, key: str, timestamp: int) -> str:
        res = ""
        values = self.store.get(key,[])
        
        # binary search
        l,r = 0,len(values) -1
        while l<=r:
            mid = (l+r) // 2
            if values[mid][1] <= timestamp:
                res = values[mid][0]
                l = mid + 1
            else:
                r = mid - 1


        return res
            

class Test(unittest.TestCase):
    
    def test_set_and_get(self):
        obj = TimeMap()
        obj.set("foo", "bar", 1)
        obj.set("foo", "baz", 2)
        obj.set("foo", "qux", 3)
        self.assertEqual(obj.get("foo", 0), "")
        self.assertEqual(obj.get("foo", 1), "bar")
        self.assertEqual(obj.get("foo", 2), "baz")
        self.assertEqual(obj.get("foo", 3), "qux")
        self.assertEqual(obj.get("foo", 4), "qux")
        
    def test_get_nonexistent_key(self):
        obj = TimeMap()
        self.assertEqual(obj.get("foo", 1), "")
        
    def test_get_empty_store(self):
        obj = TimeMap()
        self.assertEqual(obj.get("foo", 1), "")
        
if __name__ == '__main__':
    unittest.main()