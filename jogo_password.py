import string

password = " "
symbols = "!@#$%^&*()_-+={}[].,"
roman_numerals = "I,V,X,L,C,D,M"
def rule1(password):
    print("rule1(Your password must contain at least 5 letters")
    password = input("please choose a password: ")
    count = 0
    for letra in password:
        count = count + 1

    if count >= 5:
        return True

def rule2(password):
    print("rule2(Your password must contain at least 1 number")
    password = input("please choose a password: ")
    count = 0
    for elemento in password:
        count = count + 1

    for elemento in password:
        if elemento.isnumeric():
            return True


def rule3(password):
    print("rule3(Your password must contain at least 1 upercase letter")
    password = input("please choose a password: ")
    count = 0
    for elemento in password:
        if elemento.isupper():
            return True


def rule4(password):
    print("rule4(Your password must contain at least 1 special character")
    password = input("please choose a password: ")
    for elemento in password:
        if password:
            return True

def rule5(password):
    print("Rule 6: Your password must include a month of the year")
    password = input("please choose a password: ")
    for elemento in password:
        if password.find("january"):
            count = 1
        elif password.find("february"):
            count = 1
        elif password.find("march"):
            count = 1
        elif password.find("april"):
            count = 1
        elif password.find("may"):
            count = 1
        elif password.find("june"):
            count = 1
        elif password.find("july"):
            count = 1
        elif password.find("august"):
            count = 1
        elif password.find("september"):
            count = 1
        elif password.find("october"):
            count = 1
        elif password.find("november"):
            count = 1
        elif password.find("december"):
            count = 1
        else:
            count = 0

        if count >= 1:
            return True


def checkIfRomanNumeral(password):
    validRomanNumerals = ("M", "D", "C", "L", "X", "V", "I")
    for letter in password:
        if letter in validRomanNumerals:
            return True
def rule6(password):
    print("rule3(Your password must contain at least 1 roman numeral")
    password = input("please choose a password: ")
    if checkIfRomanNumeral(password):
        return True


if rule1(password):
    if rule2(password):
        if rule3(password):
            if rule4(password):
                if rule5(password):
                    if rule6(password):
                        print("GG's")