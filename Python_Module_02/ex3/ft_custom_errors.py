class GardenError(Exception):
    def __init__(self, message="Unknown garden error"):
        super().__init__(message)

class PlantError(GardenError):
    def __init__(self, message="Unknown plant error"):
        super().__init__(message)

class WaterError(GardenError):
    def __init__(self, message="Unknown water error"):
        super().__init__(message)

def test_plant_error():
    raise PlantError("The tomato plant is wilting!")

def test_water_error():
    raise WaterError("Not enough water in the tank!")

def test_custom_errors():
    print("=== Custom Garden Errors Demo ===\n")
    
    print("Testing PlantError...")
    try:
        test_plant_error()
    except PlantError as a:
        print(f"Caught PlantError: {a}\n")
    
    print("Testing WaterError...")
    try:
        test_water_error()
    except WaterError as a:
        print(f"Caught WaterError: {a}\n")
    
    print("Testing catching all garden errors...")
    try:
        test_plant_error()
    except GardenError as a:
        print(f"Caught GardenError: {a}")
    try:
        test_water_error()
    except GardenError as a:
        print(f"Caught GardenError: {a}\n")
        
    print("All custom errors types work correctly!")

if __name__ == "__main__":
    test_custom_errors()        
        