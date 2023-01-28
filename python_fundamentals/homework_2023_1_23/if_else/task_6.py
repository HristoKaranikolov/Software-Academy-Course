def get_pairs_sum_that_is_zero(data: list, needed_sum=0, ):
    pairs = {}
    counter = 0
    for i in range(len(data)):
        for j in range(i + 1, len(data)):
            if data[i] + data[j] == needed_sum:
                counter += 1
                pairs[counter] = [data[i], data[j]]

    return pairs


nums = [-2, -1, 1, 3, -3, 8, -8]

print(get_pairs_sum_that_is_zero(nums))
