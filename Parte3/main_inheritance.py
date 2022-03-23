from inheritance import Person, Employee, Guest, VIPGuest

person = Person("Tiago", 36)
guest = Guest("Marilia", 45, 405)
employee = Employee("Gustavo", 27, 69651657)
vip_guest = VIPGuest("Renato", 19, 1404)

person.identify()
person.say_age()
print()
employee.identify()
employee.say_age()
print()
guest.identify()
guest.say_age()
print()
vip_guest.identify()
vip_guest.say_age()
print()