import math

#--value helpers--
def ClampValue(value, minValue, maxValue):
    return max(min(value, maxValue), minValue)

def CopySign(value):
    return math.copysign(1, value)

#Returns bool if its between two values, inclusionary.
def IsBetween(value, minValue, maxValue):
    return maxValue >= value >= minValue