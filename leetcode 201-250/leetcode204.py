import math

class Solution:
    def countPrimes(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n <= 2:
            return 0

        primes = [True] * (n + 1)
        primes[1] = False

        for index in range(2, int(n ** 0.5) + 1):
            if primes[index]:
                for j in range(index * 2, n + 1, index):
                    primes[j] = False

        return len([index for index in range(2, n) if primes[index]])

    def countPrimes2(self, n):
        if n <= 2:
            return 0

        def is_prime(num, prime_lists):
            for index in prime_lists:
                if index * index > num:
                    return True

                if num % index == 0:
                    return False

            return True

        primes = [2]
        for num in range(3, n, 2):
            if is_prime(num, primes):
                primes.append(num)

        return len(primes)

x = Solution()
print(x.countPrimes(3) == 1)
print(x.countPrimes(10) == 4)
print(x.countPrimes(499979))
