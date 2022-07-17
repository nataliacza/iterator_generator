from generator.simple_prime_generator import prime_generator
from iterator.simple_prime_iterator import PrimeIterator

if __name__ == "__main__":

    iterate = PrimeIterator(100)
    for element in iterate:
        print("Iterate:", element)

    generate = prime_generator(100)
    for element in generate:
        print("Generate:", element)
