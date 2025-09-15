#
# @lc app=leetcode id=170 lang=python3
#
# [170] Two Sum III - Data structure design
#

# @lc code=start
class TwoSum:

    def __init__(self):
        self.numbers = {}
        

    def add(self, number: int) -> None:
        if number in self.numbers:
            self.numbers[number] += 1
        else:
            self.numbers[number] = 1
            
        

    def find(self, value: int) -> bool:
        for num in self.numbers:
            complement = value - num
            if complement in self.numbers:
                if complement != num or self.numbers[num] > 1:
                    return True
        return False
        


# Your TwoSum object will be instantiated and called as such:
# obj = TwoSum()
# obj.add(number)
# param_2 = obj.find(value)
# @lc code=end

