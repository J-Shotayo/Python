class Superhero:
    def __init__(self, name, power, secret_identity):
        self.name = name          # Attribute 1
        self.power = power        # Attribute 2
        self.secret_identity = secret_identity  # Encapsulated attribute

    def introduce(self):          # Method 1
        print(f"⚡ I'm {self.name}, and my power is {self.power}!")

    def reveal_identity(self):    # Method 2 (encapsulation)
        print(f"🕵️ My real name is {self.secret_identity}.")

class Avenger(Superhero):  # Inherits from Superhero
    def __init__(self, name, power, secret_identity, weapon):
        super().__init__(name, power, secret_identity)  # Calls parent constructor
        self.weapon = weapon  # New attribute

    def assemble(self):      # New method
        print(f"🛡️ {self.name} is assembling with the Avengers!")

    # Overriding the parent's method (polymorphism)
    def introduce(self):
        print(f"🌟 I'm {self.name}, an Avenger with {self.power}!")
        
thor = Superhero("Thor", "lightning", "Thor Odinson")
iron_man = Avenger("Iron Man", "tech genius", "Tony Stark", "Repulsor Beams")

thor.introduce()          # Output: ⚡ I'm Thor, and my power is lightning!
iron_man.introduce()      # Output: 🌟 I'm Iron Man, an Avenger with tech genius!
iron_man.assemble()       # Output: 🛡️ Iron Man is assembling with the Avengers!