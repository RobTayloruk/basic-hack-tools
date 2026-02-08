import os
import socket
import requests
from cryptography.fernet import Fernet

# Retro UI
class RetroUI:
    @staticmethod
    def welcome():
        os.system('cls' if os.name == 'nt' else 'clear')
        print("======================\n")
        print("   Welcome to HackTools  \n")
        print("======================\n")

# Port Scanner
class PortScanner:
    @staticmethod
    def scan(target, ports):
        open_ports = []
        print(f'Scanning {target} for open ports...')
        for port in ports:
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            result = sock.connect_ex((target, port))
            if result == 0:
                open_ports.append(port)
            sock.close()
        return open_ports

# Password Analysis
class PasswordAnalyzer:
    @staticmethod
    def analyze(password):
        length = len(password)
        strength = "Weak"
        if length >= 8:
            strength = "Medium"
        if length >= 12:
            strength = "Strong"
        return strength

# Network Utilities
class NetworkUtils:
    @staticmethod
    def get_ip_info(ip_address):
        response = requests.get(f'https://ipinfo.io/{ip_address}/json')
        return response.json()

class EncryptionUtilities:
    @staticmethod
    def generate_key():
        return Fernet.generate_key()

    @staticmethod
    def encrypt_message(key, message):
        f = Fernet(key)
        return f.encrypt(message.encode())

    @staticmethod
    def decrypt_message(key, encrypted_message):
        f = Fernet(key)
        return f.decrypt(encrypted_message).decode()

# Main function to interact with user
def main():
    RetroUI.welcome()
    while True:
        print("Options:")
        print("1. Port Scan")
        print("2. Password Strength Analysis")
        print("3. IP Geolocation Lookup")
        print("4. Encryption/Decryption Utilities")
        print("5. Exit")
        choice = input("Enter your choice: ")

        if choice == "1":
            target = input("Enter target IP: ")
            ports = list(range(1, 1025))
            open_ports = PortScanner.scan(target, ports)
            print(f'Open ports: {open_ports}')

        elif choice == "2":
            password = input("Enter a password to analyze: ")
            strength = PasswordAnalyzer.analyze(password)
            print(f'Password strength: {strength}')

        elif choice == "3":
            ip = input("Enter an IP address to lookup: ")
            info = NetworkUtils.get_ip_info(ip)
            print(info)

        elif choice == "4":
            message = input("Enter a message to encrypt: ")
            key = EncryptionUtilities.generate_key()
            encrypted_message = EncryptionUtilities.encrypt_message(key, message)
            print(f'Encrypted message: {encrypted_message}')
            decrypted_message = EncryptionUtilities.decrypt_message(key, encrypted_message)
            print(f'Decrypted message: {decrypted_message}')

        elif choice == "5":
            break

if __name__ == '__main__':
    main()
