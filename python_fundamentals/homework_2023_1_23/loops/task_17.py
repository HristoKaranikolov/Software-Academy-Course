# Create a program , that reads number from the console and prints all digits,
# separated by '-', to the number starting from 1.

def give_all_digits_from_1_to_number(num):
    result = []
    for i in range(1, num + 1):
        result.append(i)

    final_result = []
    multiple_digit_num = False
    for el in result:
        if len(str(el)) > 0:
            multiple_digit_num = True
            for j in str(el):
                final_result.append(int(j))

        if not multiple_digit_num:
            final_result.append(el)

    return final_result


number = int(input())

print('-'.join([str(x) for x in give_all_digits_from_1_to_number(number)]))
