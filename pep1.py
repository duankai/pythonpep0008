#! /usr/bin/python
def long_function_name(name, age,
                       gender, salary):
   print(name, age, gender, salary)
   return name, age

name, age= long_function_name("name", 51,
                          "male", 2000)


if (name != " " and
        age > 50):
    print("You are too old!")


def list():
    list = [
        1, 2, 3,
        4, 5, 6,
        7, 8, 9,
    ]
    

    return list[2]

print(list())
