import structures.node as node

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
      temp = node.Node(data)
      tail.set_next(temp)
      temp.set_prev(tail)
      self.tail = temp

  def ret_hdata(self):
    return self.head.d
