def main():
    n = int(input("What n: "))
    for s in sheep(n):
        print(s)


def sheep(n):
    for i in range(n):
        yield "🐄" * i # Yield returns only one value at a time. The function generates a single row at a time. Use for lots of rows where otherwise too big and would crash.




if __name__ == "__main__":
    main()   