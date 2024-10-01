from math import sqrt, log10
import random

class RSA:
    def __init__(self,
                 upper_limit,
                 randomseed=None):
        random.seed(randomseed)
        primes = self.prime_list(upper_limit)
        self.p = [0,0]
        p = [int(pow(10, random.random() + log10(upper_limit) - 1)) - 1 for i in range(2)]
        for i,x in enumerate(p):
            while not primes[x-2]:
                x = x-1
            self.p[i] = x
        self.n = self.p[0] * self.p[1]
        self.euler = (self.p[0] - 1) * (self.p[1] - 1)
        x = int(pow(10, random.random() + log10(upper_limit) - 1)) - 1
        while not primes[x-2]:
            x = x-1
        self.e = x
        self.d = self._set_public_key()

    @staticmethod
    def prime_list(n):
        def mark(primes,x):
            for i in range(2*x, n, x):
                primes[i-2] = False
        primes = [(i%2!=0 and i%3!=0 and i%5!=0) for i in range(2,n)]
        primes[0] = primes[1] = primes[3] = True
        for x in range(7, int(sqrt(n))+1):
           if primes[x-2]: mark(primes,x)
        return primes

    @staticmethod
    def pow_mod(x, y, z):
        n = 1
        while y:
            if y & 1:
                n = n * x % z
            y >>= 1
            x = x * x % z
        return n

    def _set_public_key(self):
        def xgcd(b, n):
            x0, x1, y0, y1 = 1, 0, 0, 1
            while n != 0:
                q, b, n = b // n, n, b % n
                x0, x1 = x1, x0 - q * x1
                y0, y1 = y1, y0 - q * y1
            return  b, x0, y0
        g,x,_ = xgcd(self.e, self.euler)
        d = x % self.euler
        return d

    def encrypt(self, plain):
        cipher = self.pow_mod(plain, self.e, self.n)
        return cipher

    def encrypt_with_external_pubkey(self, plain, e, n):
        cipher = self.pow_mod(plain, e, n)
        return cipher

    def decrypt(self, cipher):
        plain = self.pow_mod(cipher, self.d, self.n)
        return plain

    def decrypt_with_external_seckey(self, cipher, d, n):
        plain = self.pow_mod(cipher, d, n)
        return plain

    def get_secret_keys(self):
        return [self.p, self.euler, self.d]

    def get_public_keys(self):
        return [self.n, self.e]


def decrypt_test():
    rsa = RSA(1000000)
    plain = int(random.random()*100000000)
    print("plain:%d"%plain)
    cipher = rsa.encrypt(plain)
    print("cipher:%d"%cipher)
    replain = rsa.decrypt(cipher)
    print("replain:%d"%replain)
    pubkeys = rsa.get_public_keys()
    seckeys = rsa.get_secret_keys()
    print("public keys -- n:%d, e:%d"%(pubkeys[0],pubkeys[1]))
    print("secret keys -- (p, q):(%d, %d), euler:%d, d:%d"%(seckeys[0][0], seckeys[0][1], seckeys[1], seckeys[2]))

if __name__=="__main__":
    decrypt_test()