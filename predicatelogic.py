# 🔹 Predicate Logic Example in AI
# Statement: All humans are mortal. Socrates is a human. Therefore, Socrates is mortal.

humans = ["Socrates", "Plato", "Aristotle"]

def is_human(x):
    return x in humans

def is_mortal(x):
    if is_human(x):
        return True
    return False

person = "Socrates"

print("🧠 Predicate Logic Example")
print(f"Is {person} a human? -> {is_human(person)}")
print(f"Therefore, is {person} mortal? -> {is_mortal(person)}")
