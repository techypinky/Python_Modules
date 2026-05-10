import sys
import typing

if len(sys.argv) != 2:
    print("Usage: ft_ancient_text.py <file>")
else:
    filename = sys.argv[1]

    print("=== Cyber Archives Recovery ===")
    print(f"Accessing file'{filename}'")

    io: typing.IO 
    try:
        io = open(filename)        
        content = io.read()        

        print("---")
        print(content, end="")
        print("---")

    except Exception as e:
        print(f"Error opening file'{filename}': {e}")

    finally:
        try:
            io.close()             
            print(f"File '{filename}' closed.")
        except:
            pass