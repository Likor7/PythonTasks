class Developer:
    language = ""

    def __init__(self, name, years_experience):
        self.name = name
        self.years_experience = years_experience

    def __lt__(self, other):
        return self.years_experience < other.years_experience

    def about(self):
        if self.years_experience <= 3:
            print(f"My name is {self.name} and I am a Junior Developer.")
        elif self.years_experience <= 5:
            print(f"My name is {self.name} and I am a Middle Developer.")
        else:
            print(f"My name is {self.name} and I am a Senior Developer.")

    def write_code(self):
        print("I am a developer and I write code")

    def __str__(self):
        return f'{self.name} - {self.years_experience} ' + 'year' + f', {self.language}' if self.years_experience <= 1 \
            else f'{self.name} - {self.years_experience} ' + 'years' + f', {self.language}'

    def __call__(self):
        self.write_code()


class PythonDeveloper(Developer):
    language = "Python"

    def write_code(self):
        print(f"I use {self.language} to write code")


class JavaDeveloper(Developer):
    language = "Java"

    def write_code(self):
        print(f"I use {self.language} to write code")


class RubyDeveloper(Developer):
    language = "Ruby"

    def write_code(self):
        print(f"I use {self.language} to write code")
