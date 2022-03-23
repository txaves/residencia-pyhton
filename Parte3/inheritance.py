class Person:
    def __init__(self, name: str, age: int) -> None:
        self._name = name
        self._age = age

    def identify(self) -> None:
        print("My name is", self._name)

    def say_age(self) -> None:
        print("I'm", self._age, "years old")

class Employee(Person):
    def __init__(self, name: str, age: int, registration: int) -> None:
        super().__init__(name, age)
        self._registration = registration

    def identify(self) -> None:
        super().identify()
        print("And my id is", self._registration)

class Guest(Person):
    def __init__(self, name: str, age: int, room_number: str) -> None:
        super().__init__(name, age)
        self._room_number = room_number

    def identify(self) -> None:
        super().identify()
        print("And I'm staying in the room", self._room_number)

class VIPGuest(Guest):
    def __init__(self, name: str, age: int, room_number: str) -> None:
        super().__init__(name, age, room_number)

    def identify(self) -> None:
        Person.identify(self)
        print("And I'm staying in the VIP room", self._room_number)