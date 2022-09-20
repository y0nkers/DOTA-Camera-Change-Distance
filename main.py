import struct

if __name__ == '__main__':
    while True:
        try:
            distance = int(input("Enter your preferred camera distance (value must be between 1200 and 1600): "))
            assert 1200 <= distance <= 1600
            break
        except (ValueError, AssertionError):
            print("Camera distance value must be an integer between 1200 and 1600")

    # Converting distance from decimal to hexadecimal value
    distance_hex = hex(struct.unpack('<I', struct.pack('<f', distance))[0])[2:]
    # Reverse bytes of hex value (because this is how it's written in config.dll)
    hex_reversed = "".join([distance_hex[x:x + 2] for x in range(0, len(distance_hex), 2)][::-1])

    default = "0000964400409c440080a2440080b444"  # 1200 as hex value
    new = hex_reversed + "00409c440080a2440080b444"
    default_bytes = bytes.fromhex(default)
    new_bytes = bytes.fromhex(new)
    path = "client.dll"

    try:
        with open(path, "r+b") as file:
            data = file.read()
            offset = data.find(default_bytes)
            file.seek(offset)
            file.write(new_bytes)

        print("The new value is set to " + str(distance))
        input("Press Enter to continue...")
    except FileNotFoundError:
        print("Client.dll could not be found. Place this .exe file in "
              "the same directory as client.dll (dota 2 beta\\game\\dota\\bin\\win64)")
        input("Press Enter to continue...")
    except OSError:
        print("Error while reading data. The client.dll file may have already been modified.")
        input("Press Enter to continue...")
