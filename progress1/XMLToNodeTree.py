__author__ = 'newcomer'
import xml.etree.ElementTree as ET
from NodeTree import NodeTree

class InvalidELementNode(Exception):
    def __int__(self, *msg):
        pass


class NodeTreeBuilder(object):
    def __init__(self):
        pass

    def build(self, xmlPath):
        tree = ET.parse(xmlPath)
        self.root = tree.getroot()
        if self.root is None:
            self.nodeRoot = None
            pass
        self.nodeRoot = NodeTree(self.root.attrib['val'])
        self.buildNodeTree(self.root, self.nodeRoot)
        return self.nodeRoot

    def buildNodeTree(self, elemetTree, nodeTree):
        for child in elemetTree:
            if child.tag == 'rightnode':
                nodeTree.right = NodeTree(child.attrib['val'])
                self.buildNodeTree(child, nodeTree.right)
            elif child.tag == 'leftnode':
                nodeTree.left = NodeTree(child.attrib['val'])
                self.buildNodeTree(child, nodeTree.left)
            else:
                raise InvalidELementNode("Invalid node tag %s" % child.tag)


def recurse(nodeTree):
    if nodeTree is not None:
        print nodeTree.val
        if nodeTree.left is not None:
            print "has left"
            recurse(nodeTree.left)
        if nodeTree.right is not None:
            print "has right"
            recurse(nodeTree.right)

if __name__ == "__main__":
    builder = NodeTreeBuilder()
    nodeRoot = builder.build("tc/single.xml")
    recurse(nodeRoot)
