# Stockholm Ransomware Simulation

## Introduction

This project aims to develop a small program to understand how malware, specifically ransomware, operates. The program is designed for educational purposes only and should not be used maliciously.

## Features

- The program targets only a specific folder named `infection` in the user's HOME directory.
- It will encrypt files with extensions affected by Wannacry, which need to be researched.
- The program supports encryption and decryption using a 16-character key.
- Encrypted files will have the `.ft` extension added to them.
- The program provides options for help, version display, and silent operation.

## Usage

### Running the Program

1. **Help Menu**:
    ```sh
    ./Stockholm --help
    ```
    or
    ```sh
    ./Stockholm -h
    ```

2. **Display Version**:
    ```sh
    ./Stockholm --version
    ```
    or
    ```sh
    ./Stockholm -v
    ```

3. **Encrypt Files**:
    - By default, the program will show each encrypted file.
    ```sh
      ./Stockholm
      ```
    - To run silently:
      ```sh
      ./Stockholm --silent
      ```
      or
      ```sh
      ./Stockholm -s
      ```

4. **Decrypt Files**:
    ```sh
    ./Stockholm --reverse <key>
    ```
    or
    ```sh
    ./Stockholm -r <key>
    ```

### Program Requirements

- **Environment**: The program should be run in a Linux environment, preferably within a virtual machine or Docker.
- **Folder**: Ensure the `infection` folder exists in your HOME directory.
- **Dependencies**: Install necessary libraries like `openssl` or `libsodium` as per the chosen encryption method.

## Compilation

If required, compile the program using the provided `Makefile`:

- **Encrypt files**: make or make encrypt
- **Encrypt files silently**: make silent
- **Decrypt files**: make decrypt
- **Decrypt files silently**: make decrypt-silent
- **Display version**: make version
- **Help**: make help
