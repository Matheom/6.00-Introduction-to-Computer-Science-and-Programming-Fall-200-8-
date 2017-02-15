# Problem Set 1 - Problem 1


candidate = 1
prime_count = 1
nth_prime = 1000


while prime_count < nth_prime:
    divisor = 2
    prime = 1
    candidate += 2

    while divisor < candidate:
        if candidate % divisor == 0:
            prime = 0
        divisor += 1

    if prime:
        prime_count += 1

        if prime_count == nth_prime:
            print("The 1000th prime is: ", candidate)






