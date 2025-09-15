#
# @lc app=leetcode id=631 lang=python3
#
# [631] Design Excel Sum Formula
#

# @lc code=start
class Excel:

    def __init__(self, height: int, width: str):
        """
        Initialize your data structure here.
        :type height: int
        :type width: str
        """
        self.height = height
        self.width = width
        self.data = {}
        self.formulas = {}
        
    def evaluate_formula(self, formula: List[str]) -> int:
        total = 0
        for cell in formula:
            if ':' in cell:
                start, end = cell.split(':')
                start_row, start_col = int(start[1:]), start[0]
                end_row, end_col = int(end[1:]), end[0]
                for r in range(start_row, end_row + 1):
                    for c in range(ord(start_col), ord(end_col) + 1):
                        total += self.get(r, chr(c))
            else:
                row = int(cell[1:])
                col = cell[0]
                total += self.get(row, col)
        return total

    def set(self, row: int, column: str, val: int) -> None:
        """
        Set the value of cell (row, column) to val.
        :type row: int
        :type column: str
        :type val: int
        :rtype: void
        """
        self.data[(row, column)] = val
        if (row, column) in self.formulas:
            del self.formulas[(row, column)]
        

    def get(self, row: int, column: str) -> int:
        """
        Get the value of cell (row, column).
        :type row: int
        :type column: str
        :rtype: int
        """
        if (row, column) in self.data:
            return self.data[(row, column)]
        
        if (row, column) in self.formulas:
            formula = self.formulas[(row, column)]
            return self.evaluate_formula(formula)
        
        return 0
        

    def sum(self, row: int, column: str, numbers: List[str]) -> int:
        """
        Calculate the sum of the cells specified in numbers.
        :type row: int
        :type column: str
        :type numbers: List[str]
        :rtype: int
        """
        self.formulas[(row, column)] = numbers
        return self.evaluate_formula(numbers)
        


# Your Excel object will be instantiated and called as such:
# obj = Excel(height, width)
# obj.set(row,column,val)
# param_2 = obj.get(row,column)
# param_3 = obj.sum(row,column,numbers)
# @lc code=end

