def garden_operations(operation_number):
    if operation_number == 0:
        int("abc")
    elif operation_number == 1:
        10 / 0
    elif operation_number == 2:
        open("/non/existent/file")
    elif operation_number == 3:
        "abc" + 5
    else:
        print("Operation completed succesfully\n")

def test_error_types():
    print("=== Garden Error Types Demo ===")
    
    for i in range(5):
        print(f"Testing operation {i}...")
        
        try:
            garden_operations(i)
        except ValueError as a:
            print(f"Caught ValueError: {a}")
        except ZeroDivisionError as a:
            print(f"Caught ZeroDivisionError: {a}")
        except FileNotFoundError as a:
            print(f"Caught FileNotFoundError: {a}")
        except TypeError as a:
            print(f"Caught TypeError: {a}")
        print("All error types succesfully!")

if __name__ == "__main__":
    test_error_types()