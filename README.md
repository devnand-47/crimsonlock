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
git clone [https://github.com/devnand-47/CrimsonLock.git](https://github.com/devnand-47/CrimsonLock.git)
cd CrimsonLock
