def print_framed_word(word):
    frame_width = 30
    frame_line = '*' * frame_width

    print(frame_line)
    padding_total = frame_width - len(word) - 2
    left_padding = padding_total // 2
    right_padding = padding_total - left_padding

    framed_line = f"*{' ' * left_padding}{word}{' ' * right_padding}*"
    print(framed_line)
    print(frame_line)
def main():
    while True:
        word = input("Word: ")
        if word == "":
            break
        print_framed_word(word)
if __name__ == "__main__":
    main()