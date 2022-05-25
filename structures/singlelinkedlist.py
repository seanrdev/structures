import structures.node as node
from pprint import pprint
import pdb

"""<-tail->prev->---------<-next-<-head>"""
class SingleLinkedList:
  """A single direction linked list"""
  def __init__(self):
    self.head = node.Node(sentinel=True)
    self.tail = node.Node(sentinel=True)
    self.head.set_next(self.tail)
    self.tail.set_prev(self.head)
    self.num = 0

  def add_node(self, data):
    tempnode = node.Node(data)
    tempnode.set_next(self.tail)
    tempnode.set_prev(self.tail.get_prev())
    self.tail.get_prev().set_next(tempnode)
    self.tail.set_prev(tempnode)
    self.num += 1

  def get_size(self):
    return self.num

  def at_pos(self, index):
    traverse = self.head.get_next()
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
