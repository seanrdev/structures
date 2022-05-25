class Node:
  """A Single Node To Hold Data"""
  def __init__(self, data=None, sentinel=False):
    self.d = data
    self.next = None
    self.prev = None
    self.sentinel = sentinel

  def set_data(self, data):
    self.d = data

  def set_next(self, Node):
    self.next = Node

  def set_prev(self, Node):
    self.prev = Node

  def get_next(self):
    return self.next

  def get_prev(self):
    return self.prev

  def get_data(self):
    return self.d

  def is_none(self):
    if self.d is None:
      return True
    return False

  def is_sentinel(self):
    return self.sentinel
