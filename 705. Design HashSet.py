class MyHashSet:

    def __init__(self):
        self.hstore = []

    def add(self, key: int) -> None:
        if self.contains(key):
            return

        self.hstore.append(key)

    def remove(self, key: int) -> None:
        index = None

        for i in range(len(self.hstore)):
            if self.hstore[i] == key:
                index = i
                break

        if index is not None:
            self.hstore.pop(index)

    def contains(self, key: int) -> bool:
        if key in self.hstore:
            return True
        return False


operations = ["MyHashSet", "add", "add", "contains", "contains", "add", "contains", "remove", "contains"]
values = [[], [1], [2], [1], [3], [2], [2], [2], [2]]


# -------------------------------
# Calling methods automatically
# -------------------------------

obj = None
count = 0
for operation, value in zip(operations, values):
    if operation == "MyHashSet":
        obj = MyHashSet()
        print(f"{count}. {operation} ==> Null")

    elif operation == "add":
        obj.add(value[0])
        print(f"{count}. {operation} ==> Null")

    elif operation == "contains":
        result = obj.contains(value[0])
        print(f"{count}. {operation} ==> {result}")

    elif operation == "remove":
        obj.remove(value[0])
        print(f"{count}. {operation} ==> Null")

    count +=1
