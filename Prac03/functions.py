__author__ = 'Cue'
def square_number(num):
    return(num * num)
print(square_number(5))

def is_prime(value):
    i = 2
    while i < value:
        remainder = value % i
        if remainder == 0:
            return False
        i += 1
    return True

print(is_prime(5))

def celsius_to_fahrenheit(celsius):
    return celsius * 1.8 + 32.0
f = celsius_to_fahrenheit(25)
print("{}".format(f))

def inch_to_meter(inches):
    meter = inches/39.37
    return meter
inch = float(input("Enter number of inches: "))
meter  = inch_to_meter(inch)
print("{} inches is {:.4f} meters".format(inch,meter))