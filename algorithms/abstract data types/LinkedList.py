class Node:
    __elm = None
    __child = None
    __parent = None

    def __init__(self, elm, child):
        self.__elm = elm
        self.__child = child
    def setParent (parent):
        self.__parent = parent
    def setChild (child):
        self.__child = child

    def getElm ():
        return self.__elm
    def getChild ():
        return self.__child
    def getParent ():
        return self.__parent

# Trying to do it as OO as possible
class LinkedList:
    __size = 0
    __startNode = None
    __lastNode = None
    def __init__(self):
        self.__size = 0 # just do something not float around !
    def add (value):
        node = Node(value, None)
        if (self.__size < 1)
            self.__startNode = node
            self.__lastNode = node
        else
            self.__lastNode.setChild(node)
            self.__lastNode = node
    def remove (elm):
        if (self.__startNode.getElm() == elm)
            self.__startNode = self.__startNode.getChild()
        else
            c = self.__startNode
            while((c = c.getChild()).getElm() != elm and c != None)
            # store the parent also 







                                                                                                                    m
