#!/usr/bin/python3

# modify with https://www.cnblogs.com/king-ding/p/pythonchaintable.html


class Node():
    def __init__(self, node_data=0, node_next=0):
        self.node_data = node_data
        self.node_next = node_next

    def __repr__(self):
        return str({"data": self.node_data, "next": self.node_next})


class ChainTable():
    def __init__(self):
        self.head = 0
        self.length = 0

    def isEmpty(self):
        return (self.length == 0)

    def append(self, node_data):
        item = None
        if isinstance(node_data, Node):
            item = node_data
        else:
            item = Node(node_data)

        if not self.head:
            # self.head == first Node-object
            self.head = item
        else:
            node = self.head
            while node.node_next:
                node = node.node_next
            node.node_next = item

        self.length += 1

    def delete(self, index):
        if self.isEmpty():
            print('this chain table is empty')
            return

        if index < 0 or index >= self.length:
            print('error: out of index')
            return

        if index == 0:
            self.head = self.head.node_next
            self.length -= 1
            return

        cursor = 0
        node = self.head
        prev = self.head
        while node.node_next and cursor < index:
            prev = node
            node = node.node_next
            cursor += 1

        if cursor == index:
            prev.node_next = node.node_next
            self.length -= 1

    def insert(self, index, dataOrNode):
        if self.isEmpty():
            print('this chain tabale is empty')
            return

        if index < 0 or index >= self.length:
            print('error: out of index')
            return

        item = None
        if isinstance(dataOrNode, Node):
            item = dataOrNode
        else:
            item = Node(dataOrNode)

        if index == 0:
            item._next = self.head
            self.head = item
            self.length += 1
            return

        cursor = 0
        node = self.head
        prev = self.head
        while node.node_next and cursor < index:
            prev = node
            node = node.node_next
            cursor += 1

        if cursor == index:
            item._next = node
            prev._next = item
            self.length += 1

    def update(self, index, data):
        if self.isEmpty() or index < 0 or index >= self.length:
            print('error: out of index')
            return
        cursor = 0
        node = self.head
        while node.node_next and cursor < index:
            node = node.node_next
            cursor += 1

        if cursor == index:
            node.node_data = data

    def getItem(self, index):
        if self.isEmpty() or index < 0 or index >= self.length:
            print('error: out of index')
            return
        cursor = 0
        node = self.head
        while node.node_next and cursor < index:
            node = node.node_next
            cursor += 1

        return node.node_data

    def getIndex(self, data):
        cursor = 0
        if self.isEmpty():
            print('this chain table is empty')
            return
        node = self.head
        while node:
            if node.node_data == data:
                return cursor
            node = node.node_next
            cursor += 1

        if cursor == self.length:
            print("%s not found" % str(data))
            return

    def clear(self):
        del self.head
        self.head = 0
        self.length = 0

    def __str__(self):
        if self.isEmpty():
            return 'empty chain table'

        node = self.head
        node_list = []
        while node:
            node_list.append(node.node_data)
            node = node.node_next
        return str(node_list)

    def __repr__(self):
        if self.isEmpty():
            return 'empty chain table'

        node = self.head
        return str(node)

    def __getitem__(self, index):
        if self.isEmpty() or index < 0 or index >= self.length:
            print('error: out of index')
            return
        return self.getItem(index)

    def __setitem__(self, index, value):
        if self.isEmpty() or index < 0 or index >= self.length:
            print('error: out of index')
            return
        self.update(index, value)

    def __len__(self):
        return self.length
