from Developers_objs import *
from Company import Company


def info_about_developer(d: Developer):
    d.about()
    d.write_code()


def tasks():
    d1 = JavaDeveloper("Jack", 4)
    d2 = PythonDeveloper("Carl", 10)
    d3 = RubyDeveloper("Nick", 1)

    info_about_developer(d1)
    info_about_developer(d2)
    info_about_developer(d3)

    print(d1)
    print(d2)
    print(d3)

    developer = PythonDeveloper("Brad", 2)
    developer()

    print("\n\n")
    company = Company()
    company += d1
    company += d2
    company += d3
    print(company)
    company.fire("Nick")
    print(company)


if __name__ == "__main__":
    tasks()
