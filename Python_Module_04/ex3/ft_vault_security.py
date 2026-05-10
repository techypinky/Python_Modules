def secure_archive(filename, mode="r", content=None):
    try:
        if mode == "r":
            with open(filename, "r") as f:
                data = f.read()
                return (True, data)

        elif mode == "w":
            with open(filename, "w") as f:
                f.write(content)
                return (True, "Content successfully written to file")

        else:
            return (False, "Invalid mode")

    except Exception as e:
        return (False, str(e))


print("=== Cyber Archives Security ===")

print("Using'secure_archive' to read from a nonexistent file:")
print(secure_archive("/not/existing/file"))

print("Using'secure_archive' to read from an inaccessible file:")
print(secure_archive("/etc/master.passwd"))

print("Using'secure_archive' to read from a regular file:")
res = secure_archive("ancient_fragment.txt")
print(res)

print("Using'secure_archive' to write previous content to a new file:")
if res[0]:
    print(secure_archive("new_secure_file.txt", "w", res[1]))