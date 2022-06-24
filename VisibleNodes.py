class newNode(object):
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def create_tree(data):
    if not data:
      return data
    data = list(data)
    root = newNode(data[0])
    root.left = create_tree(data[1])
    root.right = create_tree(data[2])
    return root

def preOrder(node, max_value):
   
    global VisibleNodeCount
     
    if (node == None):
        return
    if (node.val >= max_value):
        VisibleNodeCount += 1
        max_value = max(node.val, max_value)
 
    preOrder(node.left, max_value)
    preOrder(node.right, max_value)

if __name__ == '__main__':

    VisibleNodeCount = 0

    tree = (8, (2, (8, None, None), (7, None, None)), (6, None, (10, None, None)))
    
    root = create_tree(tree)
    preOrder(root, 0)

    assert(VisibleNodeCount == 3)
    print("Number of Visible Nodes = ", VisibleNodeCount)
