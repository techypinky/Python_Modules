class Plant:
    def __init__(self, name, height, age):
        self.name = name
        self.height = round(height, 1)
        self.age = age
    def show(self):
        print(f"Created: {self.name}: {self.height}cm, {self.age} days old")
if __name__ == "__main__":
    plants = [
        Plant("Rose", 25.0, 30),
        Plant("Oak", 200.0, 365),
        Plant("Cactus", 5.0, 90),
        Plant("Sunflower", 80.0, 45),
        Plant("Fern", 15.0, 120)
    ]
    
    print("=== Plant Factory Output ===")
    
    for i in range(len(plants)):
        plants[i].show()
    