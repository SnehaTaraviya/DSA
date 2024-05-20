print("Hello")
class Node:
    def __init__(self,data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def insertAtBegin(self,val):
        newNode = Node(val)
        if self.head == None:
            self.head = newNode
            return
        else:
            newNode.next = self.head
            self.head = newNode

    def insertAtEnd(self,val):
        newNode = Node(val)
        if self.head == None:
            self.head = newNode
            return
        else:
            current = self.head
            while current.next != None:
                current = current.next
            current.next = newNode

    def insertAtSpecificPoint(self,val,index):
        newNode = Node(val)
        n = self.countEle()
        count=1
        if index <= 0:
            print("Index Invaild!")
        elif index > n+1:
            print("Index outof Bound!")
        else:
            if index == 1:
                self.insertAtBegin(val)
            elif index == (n+1):
                self.insertAtEnd(val)
            else:
                current = self.head
                while count < (index+1):
                    if count == (index-1):
                        newNode.next = current.next
                        current.next = newNode
                        return
                    count+=1
                    current = current.next
                
    def removeNodeByVal(self,val):
        if self.head == None:
            print("List is Empty!")
        elif self.head.data == val:
            self.head = self.head.next
            return
        else:
            current = self.head
            while current.next != None:
                if current.next.data == val:
                    current.next = current.next.next
                    return
                current = current.next
        return f"{val} isn't in List!"

    def removeNodeByIndex(self,index):
        n = self.countEle()
        count = 1
        if index <= 0:
            print("Index Invaild!")
        elif index > n:
            print("Index outof Bound!")
        else:
            if index == 1:
                self.head = self.head.next
                return
            else:
                current = self.head
                while count < index:
                    if count == (index-1):
                        current.next = current.next.next
                        return
                    current = current.next
                    count+=1
            

    def displayList(self):
        result = []
        if self.head == None:
            return "No elements in List!!!"
        else:
            current = self.head
            while current:
                result.append(current.data)
                current = current.next
        return f"List: {result}"

    def countEle(self):
        count = 0
        if self.head == None:
            return count
        else:
            current = self.head
            while current:
                count+=1
                current=current.next
        return count

    def lengthOfList(self):
        count = 0
        if self.head == None:
            return f"Length of list: {count}"
        else:
            current = self.head
            while current:
                count+=1
                current=current.next
        return f"Length of list: {count}"

    def exit(self):
        return f"Final List is {self.displayList()}"



linkedList = LinkedList()
linkedList.insertAtBegin(10)
print(linkedList.sortTheList())


# print("~~~~~~ singlyLinkedList ~~~~~~~\n")
# while True:
#     print(" 1. Add Node at Begin\n",
#           "2. Add Node at a any spesific point (Enter index Number)\n",
#           "3. Remove any Node using value\n",
#           "4. Remove any specific Node (Enter index Number)\n",
#           "5. Sort the List \n",
#           "6. Print LinkedList\n",
#           "7. Return Lenght of List\n",
#           "8. Exit\n",)
#     i = int(input("Which operation do want to perform?"))
#     print("\n")
#     m = int(input("How many ele do you want to add?"))
#     nums = [int(input("")) for i in range(m)]
#     if i == 1:
#         for i in range(len(nums)):
#             linkedList.insertAtBegin(nums[i])
#         print("Current list: ",linkedList.displayList())
#         print("\n")
#     elif i == 2:
#         m = int(input("Enter index number: "))
#         num = int(input("Enter val of node: "))
#         linkedList.insertAtSpecificPoint(num,m)
#         print("Current list: ",linkedList.displayList())
#         print("\n")
#     elif i == 3:
#         num = int(input("Which val do you want to remove? "))
#         linkedList.removeNodeByVal(num)
#         print("Current list ",linkedList.displayList())
#         print("\n")
#     elif i == 4:
#         m = int(input("which node do you want to remove? "))
#         linkedList.removeNodeByIndex(m)
#         print("Current list: ",linkedList.displayList())
#         print("\n")
#     elif i == 5:
#         for i in range(len(nums)):
#             linkedList.sortTheList(nums[i])
#     elif i == 6:
#         print(linkedList.displayList())
#     elif i == 7:
#         print(linkedList.lengthOfList())
#     elif i == 8:
#         print(linkedList.exit())
#         break
