MAX = 100

def get_number_of_elements():
    while True:
        try:
            n = int(input("Enter the number of elements (1-100): "))
            if 1 <= n <= MAX:
                return n
            else:
                print(f"Number of elements must be between 1 and {MAX}.")
        except ValueError:
            print("Invalid input. Please enter an integer.")

def get_elements(n):
    elements = []
    for i in range(n):
        while True:
            try:
                element = int(input(f"Enter element {i+1}: "))
                elements.append(element)
                break
            except ValueError:
                print("Invalid input. Please enter an integer.")
    return elements

def calculate_sum(arr):
    return sum(arr)

def main():
    n = get_number_of_elements()
    elements = get_elements(n)
    total = calculate_sum(elements)
    print(f"The sum of the elements is: {total}")

if __name__ == "__main__":
    main()