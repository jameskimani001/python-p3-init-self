#!/usr/bin/env python3

# lib/person.py

class Person:
    def __init__(self, name):
        self.name = name

if __name__ == "__main__":
    john = Person("John")
    print(john.name)

