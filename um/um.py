import re

def main():
    text = "This is a sample text containing um and umm. Um, um, um!"
    print(count(text))

def count(s):
    regex = r"(^|\W)um($|\W)"
    match = re.findall(regex, s, re.IGNORECASE)
    if match:
        return len(match)

if __name__ == "__main__":
    main()
