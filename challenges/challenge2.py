def digit_sum(n):
    return sum(int(digit) for digit in str(n))

def max_digit_sum_pair(arr):
    max_sum = -1
    found_pair = False

    for i in range(len(arr)):
        for j in range(i + 1, len(arr)):
            sum_i = digit_sum(arr[i])
            sum_j = digit_sum(arr[j])

            if sum_i == sum_j:
                found_pair = True
                current_sum = arr[i] + arr[j]
                max_sum = max(max_sum, current_sum)

    return max_sum  

print(max_digit_sum_pair([51, 71, 17, 42]))  
print(max_digit_sum_pair([42, 33, 60]))     
print(max_digit_sum_pair([51, 32, 43]))
