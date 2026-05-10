import sys
import typing

if len(sys.argv) != 2:
    print("Usage: ft_stream_management.py <file>")
else:
    filename = sys.argv[1]

    print("=== Cyber Archives Recovery & Preservation ===")
    print(f"Accessing file'{filename}'")

    io: typing.IO

    try:
        io = open(filename)
        content = io.read()

        print("---")
        print(content, end="")
        print("---")

    except Exception as e:
        print(f"[STDERR] Error opening file'{filename}': {e}", file=sys.stderr)
        try:
            io.close()
        except:
            pass
        exit()

    finally:
        try:
            io.close()
            print(f"File '{filename}' closed.")
        except:
            pass

    print("Transform data:")
    print("---")

    lines = content.split("\n")
    new_lines = []

    for line in lines:
        if line != "":
            new_lines.append(line + "#")
        else:
            new_lines.append(line)

    new_content = "\n".join(new_lines)

    print(new_content)
    print("---")

    print("Enter new file name (or empty): ", end="")
    sys.stdout.flush()

    new_filename = sys.stdin.readline().strip()

    if new_filename == "":
        print("Not saving data.")
    else:
        print(f"Saving data to'{new_filename}'")

        try:
            io = open(new_filename, "w")
            io.write(new_content)
            io.flush()
            io.close()
            print(f"Data saved in file '{new_filename}'")
            print(".")
        except Exception as e:
            print(f"[STDERR] Error opening file'{new_filename}': {e}", file=sys.stderr)
            print("Data not saved.")