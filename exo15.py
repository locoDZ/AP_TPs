def check_vowels(text):
    vowels = ['a', 'e', 'o']
    for vowel in vowels:
        if vowel in text:
            print(f"{vowel} found")
        else:
            print(f"{vowel} not found")
def main():
    text = input("Please type in a string: ")
    check_vowels(text)
if __name__ == "__main__":
    main()