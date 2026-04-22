# 🔐 Enhanced Steganography-Based Secure Messaging System with Multi-Layer Encryption  
*(Python Use Case with Encryption + Steganography Integration)*

This project implements a secure message hiding system using multi-layer encryption and image-based steganography, developed as part of the Virtusa Pre-Onboarding Training Assignment.

The system combines cryptography (Fernet encryption) and image steganography (LSB technique) to securely hide and retrieve messages inside images, ensuring confidentiality and data protection.

---

## 📌 Project Overview

This application demonstrates a secure communication system where messages are:

- First encrypted using AES-based Fernet encryption  
- Then hidden inside image pixels using LSB steganography  
- Finally retrieved and decrypted using password authentication  

### 🔒 Two-Layer Security Mechanism:
- **Encryption layer** → Cryptographic security  
- **Steganography layer** → Data hiding security  

---

## ✨ Key Features

### 🔐 Message Encryption & Decryption
- Uses Fernet symmetric encryption  
- Password-based key generation using SHA-256 + Base64  
- Secure encryption and decryption of text messages  

---

### 🖼️ Image Steganography (LSB Technique)
- Hides encrypted data inside image pixels  
- Uses Least Significant Bit (LSB) manipulation  
- Supports PNG image format  
- Extracts hidden data without visible image distortion  

---

### 🛡️ Multi-Layer Security System
- Layer 1: Password-based encryption  
- Layer 2: Image-based data hiding  
- Ensures high confidentiality and protection  

---

### ✅ Input Validation System
- Validates message length (prevents overflow issues)  
- Ensures minimum password strength  
- Improves system reliability and security  

---

### 📂 Image Handling System
- Supports multiple input images (input1.png to input10.png)  
- Generates secure output image (output.png)  
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
- **Libraries Used:**
  - cryptography (Fernet Encryption)
  - hashlib (Key generation)
  - base64 (Encoding keys)
  - Pillow (PIL) (Image processing)
  - os (File handling)

---

## 📁 Project Structure
