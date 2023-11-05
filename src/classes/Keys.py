import random


class GenKeys:
    def __init__(self):
        self.p = 0,
        self.q = 0,
        self.n = 0,
        self.n_prime = 0,
        self.e = 0,
        self.d = 0

    def PrimesInRange(x, y):
        prime_list = []
        for n in range(x, y):
            isPrime = True

            for num in range(2, n):
                if n % num == 0:
                    isPrime = False

            if isPrime:
                prime_list.append(n)

        return prime_list

    def GeneratePrimeNumber(self, MIN, MAX):
        prime_list = self.PrimesInRange(MIN, MAX)
        randomPrime1 = random.choice(prime_list)
        randomPrime2 = random.choice(prime_list)
        while randomPrime1 == randomPrime2:
            randomPrime2 = random.choice(prime_list)
        randomPrime3 = random.choice(prime_list)
        return randomPrime1, randomPrime2, randomPrime3

    def GenerateKeys(self):
        MIN = 1000000000
        MAX = 9999999999

        self.p, self.q, self.e = self.GeneratePrimeNumber(MIN, MAX)
        # self.q = self.GeneratePrimeNumber[2](MIN, MAX)
        self.n = self.p*self.q
        self.n_prime = (self.p-1) * (self.q-1)
        # self.e = self.GeneratePrimeNumber[3](MIN, MAX)

        # ed = 1 mod n_prime
        # d est l'inverse modulaire de e
        # d = pow(n, -1, n_prime)
        self.d = pow(self.n, -1, self.n_prime)





