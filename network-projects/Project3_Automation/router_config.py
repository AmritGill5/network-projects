from netmiko import ConnectHandler

# Example device (replace with actual if testing with real/simulated router)
router = {
    "device_type": "cisco_ios",
    "host": "192.168.1.1",
    "username": "admin",
    "password": "admin",
}

# Connect and send commands
net_connect = ConnectHandler(**router)
config_commands = ["hostname Router1", "interface g0/0", "ip address 192.168.1.1 255.255.255.0", "no shutdown"]
output = net_connect.send_config_set(config_commands)
print(output)
net_connect.disconnect()
