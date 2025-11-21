"""
DRY (Don’t Repeat Yourself).

Twice might be fine, but after that it needs an abstraction.
"""


temp_f = dewpoint_f = windchill_f = 1.0


# Bad example
# Temperature conversion repeated everywhere
temp_c = (temp_f - 32) * 5/9
dewpoint_c = (dewpoint_f - 32) * 5/9
windchill_c = (windchill_f - 32) * 5/9


# Good example
def f_to_c(value_f):
    return (value_f - 32) * 5/9

temp_c = f_to_c(temp_f)
dewpoint_c = f_to_c(dewpoint_f)
windchill_c = f_to_c(windchill_f)

