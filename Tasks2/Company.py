from Developers_objs import *


class Company:
    list_of_developers = []

    def __add__(self, d: Developer):
        if d.years_experience < 3:
            print(f"The developer {d.name} doesn't have enough experience for the job\n")
            return self
        self.list_of_developers.append(d)
        self.list_of_developers.sort()
        return self

    def fire(self, name: str):
        for elem in self.list_of_developers:
            if elem.name == name:
                self.list_of_developers.remove(elem)
                print(f"The developer {elem.name} fired\n")
                break
        else:
            print("This developer doesn't exist in this company\n")
        return self

    def __str__(self):
        return ' '.join([str(elem) + '\n' for elem in self.list_of_developers])
