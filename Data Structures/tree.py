class TreeNode:
    def __init__(self, data):
        self.data = data
        self.children = []
        self.parent = None
    
    def add_child(self, child):
        child.parent = self
        self.children.append(child)

    def get_level(self):
        level = 0
        current_parent = self.parent
        while current_parent:
            level += 1
            current_parent = current_parent.parent
        return level

    def print_tree(self):
        spaces = "  " * self.get_level()
        prefix = spaces + "|__" if self.parent else ""
        print(prefix + self.data)
        if self.children:
            for child in self.children:
                child.print_tree()
            
    
    def __str__(self):
        return self.data

def build_product_tree():
    root = TreeNode("Electronics")
    laptop = TreeNode("Laptop")
    cellphones = TreeNode("Cell Phones")
    televisions = TreeNode("Televisions")

    mac = TreeNode("Macbook")
    microsoft = TreeNode("Microsoft Surface")
    thinkpad = TreeNode("Thinkpad")

    iphone = TreeNode("iPhone")
    pixel = TreeNode("Google Pixel")
    vivo = TreeNode("Vivo")

    samsung = TreeNode("Samsung")
    lg = TreeNode("LG")

    laptop.add_child(mac)
    laptop.add_child(microsoft)
    laptop.add_child(thinkpad)

    cellphones.add_child(iphone)
    cellphones.add_child(pixel)
    cellphones.add_child(vivo)

    televisions.add_child(samsung)
    televisions.add_child(lg)

    root.add_child(laptop)
    root.add_child(cellphones)
    root.add_child(televisions)
    return root

if __name__ == "__main__":
    build_product_tree().print_tree()
    pass