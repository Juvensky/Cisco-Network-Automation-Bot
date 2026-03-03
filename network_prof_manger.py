import os
import requests
from netmiko import ConnectHandler
from dotenv import load_dotenv
from datetime import datetime

load_dotenv()

def discord_alert(content, color=3066993):
    payload = {
        "username": "Jay Bot",
        "embeds": [{
            "title": "Network Event Detected",
            "description": content,
            "color": color,
            "timestamp": datetime.now().isoformat()
        }]
    }
    requests.post(os.getenv("DISCORD_URL"), json=payload)

device = {
    'device_type': 'cisco_ios',
    'host': os.getenv("ROUTER_HOST"),
    'username': os.getenv("ROUTER_USER"),
    'password': os.getenv("ROUTER_PASS"),
    'port': 22,
}
try:
    with ConnectHandler(**device) as ssh:
        print("Connected! Running checks...")

        config = ssh.send_command("show run")
        filename = f"backup_{datetime.now().strftime('%Y%m%d')}.txt"
        with open(filename, "w") as f:
            f.write(config)
            interfaces = ssh.send_command("show ip interface brief")
        if "down" in interfaces.lower():
            discord_alert(" **Error:** Interface 'Down' status detected! Please correct!", color=15158332) 
        else:
            discord_alert(" Health check passed. Configuration running.", color=3066993) 

except Exception as e:
    discord_alert(f"❌ **Critical:** Connection to {device['host']} failed: {e}", color=15158332)
