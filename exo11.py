def print_hash_line(width):
    print('#' * width)
def main():
    while True:

            width = int(input("Width: "))
            if width <= 0:
                print("Please enter a positive number.")
                continue
            print_hash_line(width)
            another = input("Do you want to print another line? (yes/no): ").lower()
            if another != 'yes':
                break
if __name__ == "__main__":
    main()