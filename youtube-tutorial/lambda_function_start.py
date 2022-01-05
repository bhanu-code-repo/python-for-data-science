# lambda function implementation


# Function to convert temperature ( C -> F)
def celsius_to_fahrenheit(temp):
    return (temp * 9 / 5) + 32


# Function to convert temperature ( F -> C)
def fahrenheit_to_celsius(temp):
    return (temp - 32) * 9 / 5


def main():
    # list of celsius temperature
    c_temp = [17, 20, 35, 0, -2, -18]

    # list of fahrenheit temperature
    f_temp = [89, 90, 61, 20, 72, 56]

    # TODO: Use regular functions to convert temperature

    # TODO: Use lambda functions to convert temperature


if __name__ == '__main__':
    main()
