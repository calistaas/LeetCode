class Solution:
    #without converting to string
    def isPalindrome(self, x: int) -> bool:
        #stored the target num to do the comparison
        target  = x #121
        reverse = 0
        while x > 0:
            #extract the last digit by using modulo
            digit   = x%10 #1
            reverse = reverse*10 + digit #10
            x       = x//10 #12
            print(reverse)
        if target == reverse:
            return True
        return False

        