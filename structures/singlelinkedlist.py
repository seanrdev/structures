import structures.node as node
from pprint import pprint
import pdb

"""<-tail->prev->---------<-next-<-head>"""
class SingleLinkedList:
  """A single direction linked list"""
  def __init__(self):
    self.head = node.Node()
    self.tail = node.Node()
    self.head.set_next(self.tail)
    self.tail.set_prev(self.head)
    self.num = 0

  def add_node(self, data):
    if self.head.d == None:
      self.head.set_data(data)
      self.num += 1
    elif self.tail.d == None:
      self.tail.set_data(data)
      self.num += 1
    else:
      temp = self.tail
      self.tail = node.Node(data)
      self.tail.set_prev(temp)
      self.tail.set_next(None)
      temp.set_next(self.tail)
      self.num += 1

  def get_size(self):
    return self.num

  def at_pos(self, index):
    traverse = self.head
    for i in range(index):
      traverse = traverse.get_next()
    return traverse.get_data()

  def ret_hdata(self):
    return self.head.d

  def remove_at_position(self, index):
    traverse = self.head
    for i in range(index):
      traverse = traverse.get_next()
    traverse.get_next().set_prev(traverse.get_prev())
    traverse.get_prev().set_next(traverse.get_next())
    self.num -= 1
