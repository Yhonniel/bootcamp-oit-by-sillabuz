# 01 

class Text:

    def invert(self, message):
        list = message.split()
        list.sort(reverse=True)

        text = ""
        for x in list:
            text += x + " "

        return text


# text = Text()
# invert = text.invert("Hello Sillabuz")
# print(invert)


# 02
class Circle :
    def __init__(self, radio):
        self.radio = radio
        self.pi = 3.14

    def area(self):
        return self.pi * self.radio ** 2

    def perimetro(self):
        return 2 * self.pi * self.radio


