class TimeMap:

    def __init__(self):
        self.keystore = {}

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.keystore:
            self.keystore[key] = {
                "value": [], 
                "timestamp": []
            }
            
        self.keystore[key]["value"].append(value)
        self.keystore[key]["timestamp"].append(timestamp)

    def get(self, key: str, timestamp: int) -> str:
        if key not in self.keystore:
            return ""
            
        timestamps = self.keystore[key]["timestamp"]
        values = self.keystore[key]["value"]

        l, r = 0 , len(timestamps) - 1
        res = ''
        while l <= r:
            mid = (l + r) // 2

            if timestamps[mid] <= timestamp:
                # Fix 3: This is a valid candidate! Store the corresponding string value.
                res = values[mid]
                # Move the left pointer to see if there is a closer timestamp to the right
                l = mid + 1
            else:
                # The timestamp at mid is too big, search the left half
                r = mid - 1
                
        return res
