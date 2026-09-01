class MyHashMap:

    def __init__(self):
        self.hstore = []

    def put(self, key: int, value: int) -> None:
        Maplength = len(self.hstore)
        if Maplength == 0:
            self.hstore.append([key,value])
            return 
        for i in range(Maplength):
            if key == self.hstore[i][0]:
                self.hstore[i][1] = value
                return
        self.hstore.append([key,value])

    def get(self, key: int) -> int:        
        for i in self.hstore:
            if i[0] ==  key:
                return i[1]
        else:
            return -1

    def remove(self, key: int) -> None:
        Maplength = len(self.hstore)
        find = False

        for i in self.hstore:
            if i[0] == key:
                find = True
                break

        if find:
            store = [None] * (Maplength - 1)
            j = 0

            for i in range(Maplength):
                if key == self.hstore[i][0]:
                    continue
                else:
                    store[j] = self.hstore[i]
                    j += 1

            self.hstore = store

operations =["MyHashMap","put","put","get","get","put","get","remove","get"]

values = [[],[1,1],[2,2],[1],[3],[2,1],[2],[2],[2]]

# -------------------------------
# Calling methods automatically
# -------------------------------

obj = None
count = 0
for operation, value in zip(operations, values):
    
    if operation == "MyHashMap":
        obj = MyHashMap()
        print(f"{count}. {operation} ==> Null")

    elif operation == "put":
        obj.put(value[0], value[1])
        print(f"{count}. {operation} ==> Null")

    elif operation == "get":
        result = obj.get(value[0])
        print(f"{count}. {operation} ==> {result}")


    elif operation == "remove":
        obj.remove(value[0])
        print(f"{count}. {operation} ==> Null")

    count +=1