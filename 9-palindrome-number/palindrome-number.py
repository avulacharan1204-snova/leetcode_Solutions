class Solution:
    def isPalindrome(self, x: int) -> bool:
        original = x
        revNum = 0
        while x > 0:
            lastDigit = x%10
            revNum = revNum*10 + lastDigit
            x = x//10
        if original == revNum :
            return True
        else:
            return False

        