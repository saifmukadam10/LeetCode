class Solution:
    def addDigits(self, num: int) -> int:
        while num >= 10:
            current_sum = 0
            for digit in str(num):
                current_sum += int(digit)
            num = current_sum  # Update num to be the new sum and check the while condition again
        return num
        