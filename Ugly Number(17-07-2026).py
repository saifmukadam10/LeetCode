class Solution:
    def isUgly(self, n: int) -> bool:
        # Ugly numbers must be positive
        if n <= 0:
            return False
        
        # Divide out all factors of 2, 3, and 5
        for p in (2, 3, 5):
            while n % p == 0:
                n //= p
                
        # If the remaining number is 1, it's an ugly number
        return n == 1