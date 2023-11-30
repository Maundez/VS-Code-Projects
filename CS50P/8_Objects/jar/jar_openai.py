class Jar:
    def __init__(self, capacity=12):
        if not isinstance(capacity, int) or capacity < 0:
            raise ValueError("Capacity must be a non-negative integer")
        self._capacity = capacity
        self._size = 0

    def __str__(self):
        return "🍪" * self._size

    def deposit(self, n):
        if n < 0 or self._size + n > self._capacity:
            raise ValueError("Cannot deposit that number of cookies")
        self._size += n

    def withdraw(self, n):
        if n < 0 or self._size < n:
            raise ValueError("Not enough cookies to withdraw")
        self._size -= n

    @property
    def capacity(self):
        return self._capacity

    @property
    def size(self):
        return self._size

def main():
    jar = Jar()  # Create a Jar instance with default capacity or ask user for capacity

    while True:
        print("\nJar:", str(jar))
        print("Choose an action: [1] Deposit cookies, [2] Withdraw cookies, [3] Exit")
        choice = input("Enter choice: ")

        if choice == '1':
            try:
                n = int(input("Number of cookies to deposit: "))
                jar.deposit(n)
            except ValueError as e:
                print(f"Error: {e}")
        
        elif choice == '2':
            try:
                n = int(input("Number of cookies to withdraw: "))
                jar.withdraw(n)
            except ValueError as e:
                print(f"Error: {e}")
        
        elif choice == '3':
            print("Goodbye!")
            break
        else:
            print("Invalid choice.")

if __name__ == "__main__":
    main()