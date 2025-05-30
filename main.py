from CircularLinkedListClass import CircularLinkedList

def menu():
    print("\nCircular Linked List CLI")
    print("1. Append")
    print("2. Insert")
    print("3. Delete")
    print("4. Delete All")
    print("5. Get")
    print("6. Find First")
    print("7. Find Last")
    print("8. Reverse")
    print("9. Clone")
    print("10. Clear")
    print("11. Length")
    print("12. Show List")
    print("13. Exit")

def main():
    cll = CircularLinkedList()
    cloned = None

    def append():
        val = input("Enter character to append: ")
        cll.append(val)

    def insert():
        val = input("Enter character to insert: ")
        idx = int(input("Enter index: "))
        cll.insert(val, idx)

    def delete():
        idx = int(input("Enter index to delete: "))
        print("Deleted:", cll.delete(idx))

    def delete_all():
        val = input("Enter character to delete all: ")
        cll.deleteAll(val)

    def get():
        idx = int(input("Enter index: "))
        print("Value:", cll.get(idx))

    def find_first():
        val = input("Enter character to find first: ")
        print("Index:", cll.findFirst(val))

    def find_last():
        val = input("Enter character to find last: ")
        print("Index:", cll.findLast(val))

    def reverse():
        cll.reverse()

    def clone():
        nonlocal cloned
        cloned = cll.clone()
        print("List cloned")

    def clear():
        cll.clear()
        print("List cleared")

    def length():
        print("Length:", cll.length())

    def show():
        print("List:", cll)
        if cloned:
            print("Cloned List:", cloned)

    def exit_program():
        exit()

    actions = {
        "1": append,
        "2": insert,
        "3": delete,
        "4": delete_all,
        "5": get,
        "6": find_first,
        "7": find_last,
        "8": reverse,
        "9": clone,
        "10": clear,
        "11": length,
        "12": show,
        "13": exit_program
    }

    while True:
        menu()
        choice = input("Choose an option: ")
        try:
            action = actions.get(choice)
            if action:
                action()
            else:
                print("Invalid option")
        except Exception as e:
            print("Error:", e)

if __name__ == "__main__":
    main()
