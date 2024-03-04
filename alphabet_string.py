def repeating_pattern(N, num_letters):
    if N % num_letters != 0:
        raise ValueError(f"N must be a multiple of {num_letters}")

    letters = [chr(ord('a') + i) for i in range(num_letters)]
    result = ""

    for i in range(N // num_letters):
        result += ''.join(letters)

    return result

N1 = 3
result_string1 = repeating_pattern(N1, 3)
print(f"Example 1 (N = {N1}): {result_string1}")

N2 = 5
result_string2 = repeating_pattern(N2, 5)
print(f"Example 2 (N = {N2}): {result_string2}")

N3 = 30
result_string3 = repeating_pattern(N3, 2)
print(f"Example 3 (N = {N3}): {result_string3}")
