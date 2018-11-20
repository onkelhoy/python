import string 
import random 
import hashlib 
import time 
import math
import copy 

example_challenge = 'FODVXemVdfpoihXPQujQNcGtceWvJSijGppwQyamADRVHLmLngoeazAFkIKBEJnX'
tree = None 

def generation (challenge = example_challenge, size=25):
    answer = GiveMeRandom()

    attempt = challenge+answer
    return attempt, answer



def randomString ():
    return random.choice(
        string.ascii_lowercase + 
        string.ascii_uppercase +
        string.digits)


shaHash = hashlib.sha1()
def testAttempt (startwith = '0000'):
    found = False
    start = time.time()

    while not found:
        attempt, answer = generation()
        shaHash.update(attempt)
        solution = shaHash.hexdigest()


        if solution.startswith(startwith):
            timetook = time.time() - start 
            print solution
            print 'time took:',timetook
            found = True 
    print 'answer:',answer


class Tree:
    original = None 
    root = None 
    nextNodeIndex = 0 

    def __init__ (self, size = 25):
        self.root = Node(['0']*size, 0, size)
        self.stack = [self.root]

    def next (self):
        if self.root.dead and len(self.stack) == 0:
            return False, ''

        target = self.stack.pop()
        if target.marked:
            if target.left != None:
                self.stack.append(target.left)
                self.stack.append(target.right)
        else:
            con, left, right = target.nextGen()
            if con:
                self.stack.append(left)
                self.stack.append(right)
            elif len(self.stack) == 0:
                self.stack.append(self.root)
        return True, target.toString()
                
            
        

        

class Node:
    leftpointer = 0
    rightpointer = 0

    left = None 
    right = None 
    marked = False 
    dead = False
    array = []

    def __init__ (self, array, left, right):
        self.array = copy.copy(array)

        self.leftpointer = left 
        self.rightpointer = right 

        for i in range(left, right):
            self.array[i] = randomString()


    def toString (self):
        if self.marked:
            self.dead = True 
            return ''.join(reversed(self.array))
        else:
            self.marked = True 
            return ''.join(self.array)

    def nextGen (self):
        if (self.rightpointer - self.leftpointer < 3):
            return False, None, None 
        middle = int(math.floor((self.leftpointer + self.rightpointer) / 2))
        self.left = Node(self.array, self.leftpointer, middle)
        self.right = Node(self.array, middle, self.rightpointer)
        return True, self.left, self.right  




tests = 0
smallinc = 0
tree = Tree(10)
def GiveMeRandom ():
    global smallinc
    global tests 
    smallinc += 1
    if smallinc == 100000:
        smallinc = 0
        tests += 1 
        print 'Tests:',100000*tests 
    global tree 
    ok, val = tree.next()
    if ok:
        return val
    else:
        tree = Tree(10)
        return GiveMeRandom()


testAttempt('0000')