def game2():
    class Pov:
        def __init__(self, name, score):
            self.name = name
            self.score = score
    game = 1
    if game == 1:
        p1 = Pov(input("Enter Name "), 20)
        print(p1.name)
        print(p1.score)


game2()
