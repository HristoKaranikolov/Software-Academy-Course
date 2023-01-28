nums_in_bg = {
    'edinici': {'0': "нула", '1': "едно", '2': "две", '3': "три", '4': "четири",
                '5': "пет", '6': "шест", '7': "седем", '8': "осем", '9': "девет"},
    'desetici': {'10': "десет", '11': "единадесет", '12': "дванадесет", '13': "тринадесет", '14': "четиринадесет",
                 '15': "петнадесет", '16': "шестнадесет", '17': "седемнадесет", '18': "осемнадесет",
                 '19': "деветнадесет"},
    'desetici2': {'20': "двадесет", '30': "тридесет", '40': "четирдесет", '50': "петдесет",
                  '60': "шестдесет", '70': "седемдесет", '80': "осемдесет", '90': "деветдесет"},
    'stotici': {'100': "сто", '200': "двеста", '300': "триста", '400': "четиристотин", '500': "петстотин",
                '600': "шестстотин", '700': "седемстотин", '800': "осемстотин", '900': "деведстотин"}
}

num = int(input())
num_as_str = str(num)

result = []
if 0 <= num <= 9:
    result = nums_in_bg['edinici'][num_as_str]
elif 10 <= num <= 19:
    result = nums_in_bg['desetici'][num_as_str]
elif 20 <= num <= 99:
    if num_as_str in nums_in_bg['desetici2']:
        result = nums_in_bg['desetici2'][num_as_str]
    else:
        pass

elif 100 <= num <= 999:
    if num_as_str in nums_in_bg['stotici']:
        result = nums_in_bg['stotici'][num_as_str]
    else:
        first_num_digit = num_as_str[0] + '00'
        second_num_digit = num_as_str[1] + '0'
        third_num_digit = num_as_str[2]
        if int(num_as_str[1]) == 0:
            result = nums_in_bg['stotici'][first_num_digit]
            result += ' и '
            result += nums_in_bg['edinici'][third_num_digit]

        elif int(num_as_str[1]) == 1:
            result = nums_in_bg['stotici'][first_num_digit]
            result += ' и '
            result += nums_in_bg['desetici'][third_num_digit]
        else:

            result = nums_in_bg['stotici'][first_num_digit]
            result += ' '
            result += nums_in_bg['desetici2'][second_num_digit]
            result += ' и '
            result += nums_in_bg['edinici'][third_num_digit]

print(result)
