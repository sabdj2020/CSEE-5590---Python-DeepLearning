def string_alternative(string):

    return string[::2]


if __name__ == '__main__':

    string = input("Enter >> : ")

    alt = string_alternative(string)

    print("Alternative characters in the given string are : " + alt)