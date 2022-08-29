# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

def identificaLiterais(Exp):
    alfabeto = "ABCDEFGHIJLKWMNOPQRSTUVXZ"
    subTexto = str(Exp).replace("(", "").replace(")", "").replace("not", "").replace("and", "").replace("or", "").replace("not", "").split(' ')
    subTexto = list(filter(lambda x: x != '', subTexto))

    print(subTexto)


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    identificaLiterais("not(A and B) and (C and D)")
# See PyCharm help at https://www.jetbrains.com/help/pycharm/
