def custom_greeting(greeting: str):
    def greet_person(name: str):
        return f"{greeting}, {name}"
    return greet_person


if __name__ == "__main__":
    greet_hello = custom_greeting("Hello")
    print(greet_hello("Andrew"))
    greet_kudos = custom_greeting("Kudos")
    print(greet_kudos("Ian"))
