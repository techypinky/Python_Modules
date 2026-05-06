def input_temperature(temp_str):
    return int(temp_str)

def test_temperature():
    print("=== Garden Temperature ===\n")

    temp = "25"
    print(f"Input data is '{temp}'")
    
    result = input_temperature(temp)
    print(f"Temperature is now {result}°C\n")
    
    temp = "abc"
    print(f"Input data is '{temp}")
    
    try:
        result = input_temperature(temp)
        print(f"Temperature is now {result}°C")
    except Exception as a:
        print(f"Caught input_temperature error: {a}\n")
    print("All tests completed - program didn't crash!")

if __name__ == "__main__":
    test_temperature()  