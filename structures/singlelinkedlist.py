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

  def contains(self, value):
    traverse = self.head
    for i in range(self.num):
      traverse = traverse.get_next()
      if traverse.get_data() == value:
        return True
    return False

  def build_list(self):
    traverse = self.head
    ret_list = []
    for i in range(self.num):
      traverse = traverse.get_next()
      ret_list.append(traverse.get_data())
    return ret_list

  def replace_at_pos(self, pos, value):
    traverse = self.head
    for i in range(pos):
      traverse = traverse.get_next()
    traverse.set_data(value)

  def replace_vals(self, value, nvalue):
    traverse = self.head
    for i in range(self.num):
      traverse = traverse.get_next()
      if traverse.get_data() == value:
        traverse.set_data(nvalue)

  def add_list(self, lst):
    for i in range(len(lst)):
      tempnode = node.Node(lst[i])
      tempnode.set_next(self.tail)
      tempnode.set_prev(self.tail.get_prev())
      self.tail.get_prev().set_next(tempnode)
      self.tail.set_prev(tempnode)
      self.num += 1

  def print_list(self):
    traverse = self.head
    for i in range(self.num):
      traverse = traverse.get_next()
      print(traverse.get_data())

  def indentify(self):
    return "linkedlist"
