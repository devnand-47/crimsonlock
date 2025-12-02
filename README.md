<div align="center">

  <a href="https://git.io/typing-svg">
    <img src="https://readme-typing-svg.demolab.com?font=Fira+Code&weight=600&size=50&pause=1000&color=F70000&center=true&vCenter=true&width=800&lines=CRIMSON+LOCK;RANSOMWARE+SIMULATOR;AES-256+ENCRYPTION+LAB" alt="Typing SVG" />
  </a>

  <p>
    <img src="https://img.shields.io/badge/Python-3.10+-3776AB?style=for-the-badge&logo=python&logoColor=white" />
    <img src="https://img.shields.io/badge/Cryptography-AES_256-red?style=for-the-badge&logo=lock&logoColor=white" />
    <img src="https://img.shields.io/badge/Type-Malware_Sim-orange?style=for-the-badge&logo=hackthebox&logoColor=white" />
  </p>

</div>

---

### ⚠️ CRITICAL WARNING
> **This software is a MALWARE SIMULATOR designed for EDUCATIONAL PURPOSES ONLY.**
>
> * **DO NOT** run this on critical systems.
> * **DO NOT** use this to encrypt files you do not own.
> * **ALWAYS** keep the generated `the_key.key` file safe, or data recovery will be impossible.
>
> The developer (`Dev_Nand`) accepts no responsibility for data loss or misuse of this code.

---

### 🔐 About The Project
**CrimsonLock** is a Python-based ransomware simulator designed to demonstrate the mechanics of **Availability Attacks** and **Symmetric Encryption**.

It utilizes the `Fernet` (AES-128 in CBC mode) implementation from the `cryptography` library to securely lock files within a designated sandbox environment. This tool allows security researchers to understand how ransomware operates, how keys are generated, and the importance of key management.

* **💥 Attack Phase:** Encrypts target files into unreadable ciphertext.
* **🔑 Key Generation:** Generates a cryptographically strong master key.
* **🚑 Recovery Phase:** Decrypts and restores files using the master key.

---

### ⚙️ Installation

#### 1. Clone the Repository
```bash
git clone https://github.com/devnand-47/CrimsonLock.git
cd CrimsonLock
```
2. Install Dependencies
   ```
   pip install -r requirements.txt
   ```
   3. Setup the Sandbox
Create the sandbox folder and add some dummy files to test:
```
mkdir sandbox
echo "This is a secret" > sandbox/secret.txt
echo "Bank Password: 123" > sandbox/bank.txt
```
Usage Guide
Run the main script to enter the command menu:
```
python main.py
```
Step 1: Generate Key
Select `[1]`. This creates `the_key.key`.
Note: In a real attack, this key is sent to the attacker. If you lose this file, the data in the sandbox is lost forever.
Step 2: Encrypt (The Attack)
Select `[2]`. The script will iterate through the `sandbox` folder and encrypt every file.

Check `sandbox/secret.txt` -> It will now be gibberish.

A `RANSOM_NOTE.txt` will be dropped.

Step 3: Decrypt (The Fix)
Select `[3]`. The script reads `the_key.key` and reverses the encryption.

Check `sandbox/secret.txt` -> It will be readable again.
📂 Project Structure
```
CrimsonLock/
├── sandbox/             # ⚠️ TARGET ZONE: Put dummy files here
│   ├── secret.txt
│   └── bank.txt
├── main.py              # The Malware Logic
├── requirements.txt     # Dependencies
└── the_key.key          # Generated Master Key (Do not delete!)
```
⚠️ Legal Disclaimer
This tool is provided for EDUCATIONAL PURPOSES only.

The developer `(Dev_Nand)` demonstrates this code to teach Cryptography and Malware Analysis. Using encryption logic to lock files on systems you do not own is illegal and classified as a cybercrime.

Always run this tool in a controlled environment.
<div align="center"> <h3>Developed with 💀 by <a href="https://github.com/devnand-47">Dev_Nand</a></h3> </div>
### **Why this is better:**

  * **Reliability:** The Typing SVG service is much more stable than the Capsule Render service for complex headers.
  * **Aesthetic:** The animated typing text (`CRIMSON LOCK... RANSOMWARE SIMULATOR...`) fits the "hacker" vibe of this specific project perfectly.

**Once you confirm this is working, we can finally move on to Project 2: Payload-Viper (The Code Obfuscator).**
