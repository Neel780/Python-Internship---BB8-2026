def make_validator(min_value):
    def validate(number):
        return number >= min_value
    return validate

min_10 = make_validator(10)
min_50 = make_validator(50)

print(min_10(15))
print(min_10(5))
print(min_50(45))
print(min_50(60))