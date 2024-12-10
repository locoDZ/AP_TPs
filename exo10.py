def main():
    word = input("Enter a word: ").lower()
    cleaned_word = ''.join(char for char in word if char.isalnum())
    length = len(cleaned_word)
    midpoint = length // 2
    is_palindrome = True
    for i in range(midpoint):
        if cleaned_word[i] != cleaned_word[-(i + 1)]:
            is_palindrome = False
            break
    if is_palindrome:
        print("Yes, it's a palindrome.")
    else:
        print("No, it's not a palindrome.")
if __name__ == "__main__":
    while True:
        main()
        continue_check = input("Do you want to check another word? (yes/no): ").lower()
        if continue_check != 'yes':
            break