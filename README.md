
# 🔐 Enhanced Steganography-Based Secure Messaging System with Multi-Layer Encryption  
### *(Python Use Case with Encryption + Steganography Integration)*

> **This project implements a secure message hiding system using multi-layer encryption and image-based steganography, developed as part of the Virtusa Pre-Onboarding Training Assignment.**

This system combines **cryptography (Fernet encryption)** and **image steganography (LSB technique)** to securely hide and retrieve messages inside images, ensuring confidentiality and data protection.

---

## 📌 Project Overview

This application demonstrates a secure communication system where messages are:

- First encrypted using **AES-based Fernet encryption**  
- Then hidden inside image pixels using **LSB steganography**  
- Finally retrieved and decrypted using **password authentication**  

It ensures a **two-layer security mechanism**:

- Encryption layer (cryptographic security)  
- Steganography layer (data hiding security)  

---

## ✨ Key Features

### 🔐 Message Encryption & Decryption

- Uses **Fernet symmetric encryption**  
- Password-based key generation using **SHA-256 + Base64 encoding**  
- Secure encryption and decryption of text messages  

---

### 🖼️ Image Steganography (LSB Technique)

- Hides encrypted data inside image pixels  
- Uses **Least Significant Bit (LSB) manipulation**  
- Supports **PNG image format**  
- Extracts hidden data without visible image distortion  

---

### 🛡️ Multi-Layer Security System

- Layer 1: Password-based encryption  
- Layer 2: Image-based data hiding  
- Ensures high confidentiality and protection  

---

### ✅ Input Validation System

- Validates message length (prevents overflow attacks)  
- Ensures minimum password strength  
- Improves system reliability and security  

---

### 📂 Image Handling System

- Supports multiple input images (`input1.png` to `input10.png`)  
- Generates secure output image (`output.png`)  
- Verifies integrity after embedding process  

---

### 🔄 Encode & Decode Functionality

**Encode Mode:**
- Encrypt message  
- Hide encrypted data inside image  
- Save output image  

**Decode Mode:**
- Extract hidden data from image  
- Decrypt using password  
- Display original message  

---

## 🛠️ Technology Stack

- **Programming Language:** Python  

### Libraries Used:
- `cryptography.fernet` (Encryption)  
- `hashlib` (Key generation)  
- `base64` (Encoding keys)  
- `Pillow (PIL)` (Image processing)  
- `os` (File handling)  

---

## 📁 Project Structure

```

📦 Enhanced Steganography-Based Secure Messaging System
│
├── 📂 Images
│   ├── input1.png
│   ├── input2.png
│   ├── input3.png
│   ├── input4.png
│   ├── input5.png
│   ├── input6.png
│   ├── input7.png
│   ├── input8.png
│   ├── input9.png
│   ├── input10.png
│   └── output.png
│
├── 📂 Source
│   ├── encryption.py
│   ├── steganography.py
│   └── validator.py
│
├── main.py

````

---

## ⚙️ Setup Instructions

### 1. Install Dependencies
```bash
pip install cryptography pillow
````

### 2. Run the Project

```bash
python main.py
```

---

## 🚀 Execution Flow

* Run `main.py`

* Choose operation:

  * `1` → Encode Message
  * `2` → Decode Message
  * `3` → Exit

* Provide:

  * Message
  * Password
  * Image selection

* System performs encryption + steganography

* Output image is generated with hidden message

---

## 🔄 System Workflow

### 🔹 Encoding Process

User Input → Validation → Encryption → LSB Embedding → Output Image

### 🔹 Decoding Process

Output Image → LSB Extraction → Decryption → Original Message

---

## 🌟 Highlights of the Project

* Strong multi-layer security implementation
* Real-world cryptography + steganography integration
* Secure password-based encryption system
* Efficient image-based data hiding technique
* Clean modular Python architecture

---

## 🏆 Learning Outcomes

* Understanding of symmetric encryption (Fernet)
* Practical implementation of steganography (LSB method)
* Secure key derivation using SHA-256
* Image processing using Pillow library
* Modular Python project structuring
* Real-world secure communication system design

---

## 📑 Submission

* **Prepared by:** Kamani Shivani
* **Project Title:** Enhanced Steganography-Based Secure Messaging System with Multi-Layer Encryption
* **Type:** Python Use Case
* **Submitted for:** Virtusa Pre-Onboarding Training Assignment

