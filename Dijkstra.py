import sys

INFTY = 1E10

class Heap:
    def __init__(self):
        self.nelem = 0
        self.A = []
    def parent(self,n):
        return (n-1)//2
    def left(self,n):
        return 2*n+1
    def right(self,n):
        return 2*n+2
    def compare(self,a,b):
        return a - b > 0
    def exchange(self,i,j):
        A = self.A
        A[i],A[j] = A[j],A[i]
    def heapify(self,i):
        A = self.A
        l = self.left(i)
        r = self.right(i)
        if l < self.nelem and self.compare(A[l], A[i]):
            largest = l
        else:
            largest = i
        if r < self.nelem and self.compare(A[r], A[largest]):
            largest = r
        if largest != i:
            self.exchange(i,largest)
            self.heapify(largest)
            
class PrioNode:
    def __init__(self, key, n):
        self.ndx = 0
        self.n = n
        self.key = key
    def __repr__(self):
        return "(%d:%d,%d)" % (self.ndx,self.n, self.key)

class MaxQueue(Heap):
    def __init__(self):
        super().__init__()
    def compare(self,a,b):
        return a.key > b.key
    def exchange(self,i,j):
        A = self.A
        A[i].ndx = j
        A[j].ndx = i
        super().exchange(i,j)
    def update_key(self,i):
        parent = lambda x: self.parent(i)
        compare = lambda a,b: self.compare(a,b)
        A = self.A
        while i > 0 and not compare(A[parent(i)], A[i]):
            self.exchange(i,parent(i))
            i = parent(i)
    def increase_key(self,i,key):
        A = self.A
        if key < A[i].key:
            print ("Error")
            sys.exit(-1)
        A[i].key = key
        self.update_key(i)
    def insert(self,n):
        A = self.A
        while (len(A) < self.nelem):
            A.append(None)
        i = self.nelem
        A.append(None)
        self.nelem = self.nelem + 1
        A[i] = n
        A[i].ndx = i
        self.update_key(i)
    def extract(self):
        elem = self.A[0]
        self.exchange(0,self.nelem-1)
        self.nelem = self.nelem - 1
        self.heapify(0)
        return elem
    def is_empty(self):
        return self.nelem == 0

class MinQueue(MaxQueue):
    def __init__(self):
        super().__init__()
    def compare(self,a,b):
        return a.key < b.key
    def update_key(self,i):
        parent = lambda x: self.parent(i)
        A = self.A
        while i > 0 and not self.compare(A[parent(i)], A[i]):
            self.exchange(i,parent(i))
            i = parent(i)
    def decrease_key(self,i,key):
        A = self.A
        if key > A[i].key:
            print ("Error")
            sys.exit(-1)
        A[i].key = key
        self.update_key(i)
    def __repr__(self):
        return "%a %a" % (self.nelem,self.A)

class Adj:
    def __init__(self, n):
        self.n = n
        self.next = None

class Weight(Adj):
    def __init__(self, n, w):
        super().__init__(n)
        self.w = w

class Vertex:
    def __init__(self, name):
        self.parent = -1
        self.name = name
        self.n = 0
        self.first = None
    def add(self, v):
        a = Adj()
        a.n = v.n
        a.next = self.first
        self.first = a
    def copy(self, other):
        self.parent = other.parent
        self.name = other.name
        self.n = other.n
        self.first = other.first

class DijkVertex(Vertex):
    def __init__(self, name):
        super().__init__(name)
        self.d = INFTY
        self.priority = None
    def __repr__(self):
        return "(%a %a %a)" % (self.name,self.n,self.d)
    def add(self, v, w):
        a = Weight(v, w)
        a.next = self.first
        self.first = a
    def set_priority(self,n):
        self.priority = n
    def decrease_key(self, q):
        prio = self.priority
        ndx = prio.ndx
        q.decrease_key(ndx, self.d)
        

class Dijkstra:
    def __init__(self):
        self.vertices = []
        self.q = MinQueue()
    def add_vertex(self,name):
        n = len(self.vertices)
        v = DijkVertex(name)
        v.n = n
        self.vertices.append(v)
        return v
    def get_vertex(self,name):
        for v in self.vertices:
            if v.name == name:
                return v
        return None        
    def print_vertex(self,n):
        print (self.vertices[n].name, end=' ')
        print (self.vertices[n].parent, end=' ')
        print (self.vertices[n].d, end=' ')
        p = self.vertices[n].first
        while p:
            print (p.n.name, end = ' ')
            print (p.w, end = ' ')
            p = p.next
        print('')
    def print_vertices(self):
        for i in range(len(self.vertices)):
            self.print_vertex(i)
    def relax(self, u):
        vset = self.vertices
        q = self.q
        p = u.first
        while p:
            v = p.n;
            d = u.d + p.w
            if d < v.d:
                v.d = d
                v.parent = u.n
                print(v)
                v.decrease_key(q)
            p = p.next
    def shortest_path(self):
        q = self.q
        vset = self.vertices
        for v in vset:
            n = PrioNode(v.d, v.n)
            v.set_priority(n)
            q.insert(n)
        while not q.is_empty():
            u = q.extract()
            self.relax(vset[u.n])

def main():
    print("---- dijkstra main ----")
    g = Dijkstra()
    s = g.add_vertex('s')
    t = g.add_vertex('t')
    x = g.add_vertex('x')
    y = g.add_vertex('y')
    z = g.add_vertex('z')
    s.add(t,10)
    s.add(y,5)
    t.add(y,2)
    t.add(x,1)
    x.add(z,4)
    y.add(t,3)
    y.add(x,9)
    y.add(z,2)
    z.add(s,7)
    z.add(x,6)
    s.d = 0
    g.print_vertices()
    g.shortest_path()
    g.print_vertices()

main()
