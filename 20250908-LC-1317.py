# 1317 - Convert Integer to the Sum of Two No-Zero Integers

class Solution:
    def getNoZeroIntegers(self, n: int) -> List[int]:
        """
        How do we know if a number has 0 in it?
        109, 2048, 11
        From 109, the min a and max b would be 11, 98
        From 2048, the min a and max b would be 49, 1999
        From 11, the min a and max b would be 2, 9
        Naive Approach;
        Let a start from 1, b being n - a
        Increment a and decrement b till both have no 0 present
        Returns 0ms runtime and 17.67mb memory

        Optimized Approach;
        Maybe half? Logn approach
        2000 --> 1000 --> 500 --> 250 --> 125
        2000 - 125 = 1875
        Returns 0ms runtime and 17.67mb memory
        """
        # # Naive Approach
        # a = 1
        # b = n-a
        # while '0' in str(a) + str(b):
        #     a += 1
        #     b -= 1
        # return [a, b]

        # # Optimized Approach
        # a = n
        # b = n - a
        # while '0' in str(a) + str(b):
        #     a = a//2
        #     b = n - a
        # return [a, b]

        # Further Optimization (find the first 0 and fix)
        str_n = str(n)
        max_zero = 0
        a = 1
        b = n - a

        # Find the first 0 that appears
        for i in range(len(str_n)):
            if str_n[i] == '0':
                max_zero = len(str_n) - i
                break
        # print(max_zero)

        # A will be '1' * position of zero
        if max_zero != 0:
            a = int('1' * max_zero)
            b = n-a

        # Sanity check to ensure both a and b have no '0' present
        while '0' in str(a) + str(b):
            a += 1
            b -= 1
        return [a, b]
