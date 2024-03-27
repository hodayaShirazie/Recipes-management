import colors


class List_of_recipies:
    def __init__(self):
        self.num_of_recipies = 0
        self.recipies = []

    def add_recipie(self, recipie):
        self.recipies.append(recipie)
        self.num_of_recipies += 1

    def remove_recipie(self, recipie):
        for each_recipie in self.recipies:
            if recipie.name == each_recipie.name:
                if recipie.content == each_recipie.content:
                    self.recipies.remove(each_recipie)
                    self.num_of_recipies -= 1


    def print_recipies(self):
        for recipie in self.recipies:
            recipie.print_recipie()




if __name__ == '__main__':
    r = List_of_recipies()
    r.add_recipie("chocolate cookies", "this is my first recipie")
