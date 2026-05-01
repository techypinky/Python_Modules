class Plant:
    def __init__(self, name, height, age):
        self.name = name
        
        if height < 0:
            print(f"{name}: Error, height can't be negative")
            self._height = 0.0
        else:
            self._height = round(height, 1)
            
        if age < 0:
            print(f"{name}: Error, age can't be negative")
            self._age = 0
        else:
            self._age = age
            
    def set_height(self, new_height):
        if new_height < 0:
            print(f"{self.name}: Error, height can't be negative")
            print("Height update rejected")
        else:
            self._height = round(new_height, 1)
            print(f"Height updated: {int(new_height)}cm")
    
    def set_age(self, new_age):
        if new_age < 0:
            print(f"{self.name}: Error, age can't be negative")
            print("Age update rejected\n")
        else:
            self.age = new_age
            print(f"Age updated: {new_age} days\n")
    
    def get_height(self):
        return self._height

    def get_age(self):
        return self._age

    def show(self):
        print(f"Current state: {self.name}: {self._height}cm, {self.age} days old")
    
if __name__ == "__main__":
    print("=== Garden Security System ===")

    plant = Plant("Rose", 15.0, 10)

    print("Plant created: Rose: 15.0cm, 10 days old\n")

    plant.set_height(25)
    plant.set_age(30)

    plant.set_height(-5)
    plant.set_age(-3)

    plant.show()