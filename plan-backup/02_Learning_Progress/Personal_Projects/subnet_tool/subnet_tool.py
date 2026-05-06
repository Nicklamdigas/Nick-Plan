user_input = input("Enter your IP Address: ").strip()
ip_address = user_input.split(".")

if len(ip_address) == 4 and int(ip_address[0]) in range(0,256):
    print(ip_address)
    network_address = f"{ip_address[0]}.{ip_address[1]}.{ip_address[2]}.0"
    print(f"Network Address: {network_address}")

    broadcast_address = f"{ip_address[0]}.{ip_address[1]}.{ip_address[2]}.255"
    print(f"Broadcast Address: {broadcast_address}")
else:
    print("Invalid IP Address")

