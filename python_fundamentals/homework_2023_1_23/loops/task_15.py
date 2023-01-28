# Create a program, that check if a number is prime or not.

def check_if_prime(num):
    if num == 1:
        return False
    if num > 1:
        for i in range(2, num):
            if (num % i) == 0:
                return False

        return True


number = int(input())
if check_if_prime(number):
    print('The number is prime')
else:
    print('The number is not prime.')
