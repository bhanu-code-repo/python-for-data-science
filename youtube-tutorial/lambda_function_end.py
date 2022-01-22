# lambda function implementation


# Function to convert temperature ( C -> F)
def celsius_to_fahrenheit(temp):
    return (temp * 9 / 5) + 32


# Function to convert temperature ( F -> C)
def fahrenheit_to_celsius(temp):
    return (temp - 32) * 9 / 5


def main():
    # list of celsius temperature
    c_temp = [17, 20, 35, 0, -2, -18, 68]

    # list of fahrenheit temperature
    f_temp = [89, 90, 61, 20, 72, 56, 104.4]

    # TODO: Use regular functions to convert temperature
    print(list(map(celsius_to_fahrenheit, c_temp)))
    print(list(map(fahrenheit_to_celsius, f_temp)))

    # TODO: Use lambda functions to convert temperature
    print(list(map(lambda t: (t * 9 / 5) + 32, c_temp)))
    print(list(map(lambda t: (t - 32) * 9 / 5, f_temp)))


if __name__ == '__main__':
    main()
