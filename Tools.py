import math

#--value helpers--
def ClampValue(value, minValue, maxValue):
    return max(min(value, maxValue), minValue)

def CopySign(value):
    return math.copysign(1, value)

#If input is less than +-range it will return zero. Helps round down values close to zero.
def RoundToZero(input, rang):
    return 0 if abs(input) < rang else input

#Returns bool if its between two values, inclusionary.
def IsBetween(value, minValue, maxValue):
    return maxValue >= value >= minValue


#Vectors
def VectorMagnitude(xy: tuple[float, float]) -> float:
    return math.sqrt(xy[0]**2 + xy[1]**2)

def VectorAngle(xy: tuple[float, float]) -> float:
    return math.atan2(xy[0],xy[1])

def VectorNew(angleNew: float, magnitudeNew: float) -> tuple[float, float]:
    return (magnitudeNew * math.sin(angleNew), magnitudeNew * math.cos(angleNew))

def VectorNormalize(v: tuple[float, float]) -> tuple[float, float]:
    mag = VectorMagnitude(v)
    return (v[0]/mag, v[1]/mag)

def VectorMultiplyConstant(v: tuple[float, float], m: float) -> tuple[float, float]:
    return (v[0] * m, v[1] * m)

def VectorsAdd(v1: tuple[float, float], v2: tuple[float, float]) -> tuple[float, float]:
    return (v1[0] + v2[0], v1[1] + v2[1])