def underline_string(text):
    print(text)
    print('-' * len(text))

def main():
    while True:
        text = input("Please type in a string: ")
        if text == "":
            break
        underline_string(text)

if __name__ == "__main__":
    main()