def check_for_factor(base, factor):
    return base % factor == 0

base_number = 6
potential_factor= 2

if check_for_factor(base_number, potential_factor):
    print(f"{potential_factor} is a factor of {base_number}")
else:
    print(f"{potential_factor} is not a factor of {base_number}")