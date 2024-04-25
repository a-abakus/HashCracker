# Hash Cracker

## Introduction
This script is a simple MD5, SHA256, and SHA512 hash cracker that takes a hash and a wordlist as input to find the corresponding plaintext password.

## Usage
- `pip3 install -r requirements`
- `python3 md5_cracker.py <md5/sha256/sha512> <hash> <wordlist>`
- `<md5/sha256/sha512>`: Specify the type of hash to crack.
- `<hash>`: Provide the hash to crack.
- `<wordlist>`: Specify the path to the wordlist file containing potential passwords.

## Example
```
python3 hashcracker.py sha256 f15c16b99f8.. rockyou.txt
 _   _           _      ____                _             
| | | | __ _ ___| |__  / ___|_ __ __ _  ___| | _____ _ __ 
| |_| |/ _` / __| '_ \| |   | '__/ _` |/ __| |/ / _ \ '__|
|  _  | (_| \__ \ | | | |___| | | (_| | (__|   <  __/ |   
|_| |_|\__,_|___/_| |_|\____|_|  \__,_|\___|_|\_\___|_|   

Process in ongoing.. 697 / 14344393
Hash > f15c16b99f8.. : tiger
```
