def string_alternative(string):

    return string[::2]


if __name__ == '__main__':

    string = input("Enter a message : ")

    alternative_message = string_alternative(string)

    print("Alternative characters in message : " + alternative_message)