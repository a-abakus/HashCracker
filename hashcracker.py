import sys
import pyfiglet
import hashlib
import time


def banner():
    ascii_banner = pyfiglet.figlet_format("HashCracker")
    print(ascii_banner)


def usage(usg=False):
    print(usg)
    if not usg:
        print("Usage: python3", sys.argv[0], "<md5/sha256/sha512> <hash> <wordlist>")
    else:
        print("Choose a hash type: md5 - sha256 - sha512")
    sys.exit(1)


def entry():
    hash_type = sys.argv[1]
    to_crack = sys.argv[2]
    wl_path = sys.argv[3]
    
    try:
        with open(wl_path, errors="ignore") as f:
            wordlist = f.read().splitlines()
            main(wordlist, hash_type, to_crack)
    except FileNotFoundError:
        print("File not found!")
    except KeyboardInterrupt:
        print(" Exitting.. ")


def main(wordlist, hash_type, to_crack):
    count = 0
    for word in wordlist:
        time.sleep(0.0075)
        count += 1
        if hash_type == "md5":
            hashTxt = hashlib.md5(word.encode())
        elif hash_type == "sha256":
            hashTxt = hashlib.sha256(word.encode())
        elif hash_type == "sha512":
            hashTxt = hashlib.sha512(word.encode())
        else:
            usage(True)
        if hashTxt.hexdigest() == to_crack:
            print("\nHash >", to_crack, ":", word)
            break
        print("Process in ongoing..", str(count), "/", str(len(wordlist)), end="\r")


if __name__ == "__main__":
    banner()
    if len(sys.argv) < 4:
        usage()
    entry()
