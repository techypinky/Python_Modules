class Plant:
    def __init__(self, name, height, age):
        self.name = name
        self._height = round(height, 1)
        self._age = age
    def grow(self):
        self._height = self._height + 2.1
    def age_up(self):
        self._age += 1
    def show(self):
        print(f"{self.name}: {self._height:.1f}cm, {self._age} days old")
    
    
class Flower(Plant):
    def __init__(self, name, height, age, color):
        super().__init__(name, height, age)
        self.color = color
        self.bloomed = False
    def bloom(self):
        self.bloomed = True
    def show(self):
        super().show()
        print(f"Color: {self.color}")
        
        if self.bloomed:
            print(f"{self.name} is blooming beautifully!\n")
        else:
            print(f"{self.name} has not bloomed yet")


class Tree(Plant):
    def __init__(self, name, height, age, trunk_diameter):
        super().__init__(name, height, age)
        self.trunk_diameter = trunk_diameter
    def produce_shade(self):
        print(f"Tree {self.name} now produces a shade of {self._height:.1f}cm long and {self.trunk_diameter:.1f}cm wide.\n")
    def show(self):
        super().show()
        print(f"Trunk diameter: {self.trunk_diameter:.1f}cm")


class Vegetable(Plant):
    def __init__(self, name, height, age, harvest_season):
        super().__init__(name, height, age)
        self.harvest_season = harvest_season
        self.nutritional_value = 0
    def grow(self):
        self._height += 2.1
        self.nutritional_value += 1

    def show(self):
        super().show()
        print(f"Harvest season: {self.harvest_season}")
        print(f"Nutritional value: {self.nutritional_value}")
        
if __name__ == "__main__":
    print("=== Garden Plant Types ===")
    #flower
    print("=== Flower")
    rose = Flower("Rose", 15.0, 10, "red")
    rose.show()
    print("[asking the rose to bloom]")
    rose.bloom()
    rose.show()
    #tree
    print("=== Tree")
    oak = Tree("Oak", 200.0, 365, 5.0)
    oak.show()
    print("[asking the oak to produce shade]")
    oak.produce_shade()
    #vegetable
    print("=== Vegetable")
    tomato = Vegetable("Tomato", 5.0, 10, "April")
    tomato.show()
    
    print("[make tomato grow and age for 20 days]")
    
    for i in range(20):
        tomato.grow()
        tomato.age_up()
    tomato.show()
    
            
    

    