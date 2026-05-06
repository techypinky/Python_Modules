def input_temperature(temp_str):
    temp = int(temp_str)

    if temp > 40:
        raise Exception(f"{temp}°C is too hot for plants (max 40°C)\n")
    if temp < 0:
        raise Exception(f"{temp}°C is too cold for plants (min 0°C)\n")
    return temp

def test_temperature():
    print("=== Garden Temperature Checker ===\n")
    tests = ["25", "abc", "100", "-50"]
    
    for temp in tests:
        print(f"Input data is '{temp}'")
        
        try:
            result = input_temperature(temp)
            print(f"Temperature is now {result}°C\n")
        except Exception as a:
            print(f"Caught input_temperature error: {a}\n")
    print("All tests completed - program didn't crash!")

if __name__ == "__main__":
    test_temperature()
             