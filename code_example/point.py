class Point:

    def __init__(self, cordx, cordy):
        self.cordx = cordx
        self.cordy = cordy

    def __str__(self):
        return "[" + str(self.cordx) + ", " + str(self.cordy) + "]"


if __name__ == "__main__":
    p = Point(2, 3)
    print(p)
