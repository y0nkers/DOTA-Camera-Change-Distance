if __name__ == '__main__':
    distance_1200 = "0000964400409c440080a2440080b444"
    distance_1500 = "0080bb4400409c440080a2440080b444"
    distance_1200_bytes = bytes.fromhex(distance_1200)
    distance_1500_bytes = bytes.fromhex(distance_1500)
    path = "client.dll"

    with open(path, "r+b") as file:
        data = file.read()
        offset = data.find(distance_1200_bytes)
        file.seek(offset)
        file.write(distance_1500_bytes)
