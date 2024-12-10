def print_hash_rectangle(width, height):
    for _ in range(height):
        print('#' * width)
def main():
    while True:

            width = int(input("Width: "))
            if width <= 0:
                print("Please enter a positive width.")
                continue

            height = int(input("Height: "))
            if height <= 0:
                print("Please enter a positive height.")
                continue

            print_hash_rectangle(width, height)

            another = input("Do you want to print another rectangle? (yes/no): ").lower()
            if another != 'yes':
                break

if __name__ == "__main__":
    main()