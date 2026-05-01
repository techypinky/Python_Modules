class Plant:
    def __init__(self, name, height, age):
        self.name = name
        self.height = height
        self.age = age
        
    def grow(self):
            self.height += 0.8
    def age_up(self):
            self.age += 1
    def show(self):
            print(f"{self.name}: {self.height:.1f}cm, {self.age} days old")
        
if __name__ == "__main__":
    plant = Plant("Rose", 25.0, 30)
    init_height = plant.height
            
    print("=== Garden Plant Growth ===")
    plant.show()
            
    for day in range(1, 8):
        print(f"=== Day {day} ===")
        plant.grow()
        plant.age_up()
        plant.show()
    weekly_growth  = plant.height - init_height
    print(f"Growth this week: {round(weekly_growth, 1)}cm")
                    
        
            
        
        
        