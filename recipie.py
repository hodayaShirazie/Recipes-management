import colors


class Recipie:
    def __init__(self, name=None, content=None, category=None):
        if name == None:
            print(colors.magenta("Enter the name of the recipie"))
            self.name = input()
        else:
            self.name = name
        if content == None:
            print(colors.magenta("Enter recipie content"))
            self.content = self.multi_lines_input()
        else:
            self.content = content
        if category == None:
            print(colors.magenta("select a category from the following categories:\n") + colors.white(
                                 "1- breakfast\n"
                                 "2- lunch\n"
                                 "3- dinner\n"
                                 "4- dessert\n"
                                 "5- fast & easy\n"))
            self.category = int(input())
        else:
            self.category = category




    def multi_lines_input(self):
        lines = []
        while True:
            line = input()
            if line.strip() == "":
                break
            lines.append(line)
        return '\n'.join(lines)



    def print_recipie(self):
        print(colors.red("\n------------------------------------------------------------------------------------------------------------------------------------------------"))
        print(colors.blue(self.name))
        self.print_categories()
        print('\n'.join(self.content.split('\n')))
        print(colors.red("\n------------------------------------------------------------------------------------------------------------------------------------------------"))


    def print_categories(self):
        if self.category == 1:
            print(colors.green("classification category: ") + "breakfast")
        elif self.category == 2:
            print(colors.green("classification category: ") + "lunch")
        elif self.category == 3:
            print(colors.green("classification category: ") + "dinner")
        elif self.category == 4:
            print(colors.green("classification category: ") + "dessert")
        elif self.category == 5:
            print(colors.green("classification category: ") + "fast & easy")





