import sys


def find_closest_palindrome(num):
    # Check if num is palindrome
    if str(num) == str(num)[::-1]:
        return num

    # check numbers from given number down, to number 10,
    # until it finds number palindrome, closest to the given number.
    first_result = 0
    for j in range(num - 1, 9, -1):
        i_as_str = str(j)
        if i_as_str == i_as_str[::-1]:
            first_result = j
            break

    # check numbers, starting from given number up,
    # until it finds a number palindrome, closest to the given number.
    second_result = 0
    for i in range(num + 1, sys.maxsize):
        i_as_str = str(i)
        if i_as_str == i_as_str[::-1]:
            second_result = i
            break

    # compare the two results to see which is closest to the num
    first_diff = num - first_result
    second_diff = second_result - num

    if first_diff < second_diff or first_diff == second_diff:
        return first_result
    return second_result


number = int(input())
print(find_closest_palindrome(number))
