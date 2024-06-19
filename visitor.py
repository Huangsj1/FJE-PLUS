from abc import ABC, abstractmethod

class NodeVisitor(ABC):
    '''
    访问者
    '''
    @abstractmethod
    def visit(self, node, icon_family=None):
        pass

class TreeDisplayVisitor(NodeVisitor):
    def visit(self, node, icon_family=None):
        node.display_without_root(icon_family)

class RectangleDisplayVisitor(NodeVisitor):
    def visit(self, node, icon_family=None):
        node.display_without_root(icon_family)
