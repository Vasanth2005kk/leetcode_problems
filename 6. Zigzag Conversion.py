
class Solution:
  def convert(self, s: str, numRows: int) -> str:
    rows = [''] * numRows
    k = 0
    direction = (numRows == 1) - 1

    for c in s:
      rows[k] += c
      if k == 0 or k == numRows - 1:
        direction *= -1
      k += direction

    return ''.join(rows)
  

string="ABCDEFGH"
row=3

obj=Solution().convert(s=string,numRows=row)
print(obj)