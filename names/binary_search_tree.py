class BinarySearchTree:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    # Insert the given value into the tree
    def insert(self, value):
        # LEFT CASE
        # check if our new nodes value is less than the current nodes value
        if value < self.value:
            # does it have a child to the left?
            if not self.left:
                # place our new node here
                self.left = BinarySearchTree(value)
            # otherwise
            else:
                # repeat process for the left
                self.left.insert(value)

        # RIGHT CASE
        # check if the new nodes value is greater than or equal to the current nodes value
        if value >= self.value:
            # does it have a child to the right?
            if not self.right:
                # place our new node here
                self.right = BinarySearchTree(value)
            # otherwise
            else:
                # repeat the process for the right
                self.right.insert(value)

    # Return True if the tree contains the value
    # False if it does not
    def contains(self, target):
        # BASE CASE
        # check if the value matches the target
        if self.value == target:
            # return true
            return True  
        # LEFT CASE if target less than value
        if target < self.value:
            # check if the left child exists if not
            if not self.left:
                # return false
                return False
            # otherwise
            else:
                # call the contains method of the left child
                return self.left.contains(target)
        # RIGHT CASE otherwise
        else:
            # check if right child exists if not
            if not self.right:
                # return false
                return False
            # otherwise
            else:
                # call the contains method of the right child
                return self.right.contains(target)