# Hack Tools Script

"""
This script serves as an educational tool for various hacking techniques, presented in a 90s retro visual style. 
Remember, use these tools responsibly and only in legal scenarios.
"""

import os
import time

class RetroStyle:
    def __init__(self):
        self.segments = ["[+] Welcome to the Retro Hack Tools!", "[+] Loading...", "[+] Ready to Hack!"]

    def display(self):
        for segment in self.segments:
            print(segment)
            time.sleep(1)

    def hacking_tool(self, tool):
        print(f"[+] Running tool: {tool}")
        time.sleep(2)
        print("[+] Tool complete!")

if __name__ == '__main__':
    retro = RetroStyle()
    retro.display()
    
    print("Choose a tool to run:")
    tools = ["Port Scanner", "Password Cracker", "Packet Sniffer"]
    for i, tool in enumerate(tools):
        print(f"{i + 1}. {tool}")
    choice = int(input("Enter the number of your choice: ")) - 1
    if 0 <= choice < len(tools):
        retro.hacking_tool(tools[choice])
    else:
        print("Invalid choice! Please run the script again.")

# Note: This script is for educational purposes only. Use responsibly!