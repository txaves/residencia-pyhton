def salute():
    print("Hello!")

def salute_with_name(name):
    print("Hello, " + name + "!")

def build_salute_text(name):
    return "Hi, " + name + "!"

def salute_with_default(name = "unknown person"):
     print("Hi, " + name + "!")

#salute()
salute_with_name(build_salute_text("Tiago"))
#print(build_salute_text("Tiago"))
#salute_with_default("Chaves")
#salute_with_default()