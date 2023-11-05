import random
import math


def is_prime(number):
  if number <= 1:
    return False
  if number <= 3:
    return True
  if number % 2 == 0 or number % 3 == 0:
    return False
  i = 5
  while i * i <= number:
    if number % i == 0 or number % (i + 2) == 0:
      return False
    i += 6
  return True


def generate_prime_number(size):
  while True:
    num = random.randint(10 ** (size - 1), 10 ** size - 1)
    if is_prime(num):
      return num


def mod_inverse(e, phi):
  for d in range(3, phi):
    if (d * e) % phi == 1:
      return d
  raise ValueError('No mod_inverse for {} and {}'.format(e, phi))


def generate_keypair(bits):
  p, q = generate_prime_number(bits), generate_prime_number(bits)
  n = p * q
  phi = (p - 1) * (q - 1)
  e = random.randint(3, phi - 1) 
  while math.gcd(e, phi) != 1:
    e = random.randint(3, phi - 1)
  d = mod_inverse(e, phi)
  return (n, e), (n, d)
