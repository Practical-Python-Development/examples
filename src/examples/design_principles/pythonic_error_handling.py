"""
EAFP vs LBYL (Pythonic Error Handling).

Often it is preferred to do LBYL (Look Before You Leap).
In Python case EAFP (Easier to Ask Forgiveness than Permission) is preferred,
as it is usually shorter and avoids multiple look-ups.
"""


dataset = {}


# Bad example
if "temperature" in dataset:
    temp = dataset["temperature"]
else:
    temp = None


# Good example
try:
    temp = dataset["temperature"]
except KeyError:
    temp = None
