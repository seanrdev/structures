class Node:
  """A Single Node To Hold Data"""
  def __init__(self, data=None):
    self.d = data
    self.next = next
    self.prev = prev

  def set_data(self, data):
    self.d = data

  def set_next(self, Node):
    self.next = Node

  def set_prev(self, Node):
    self.prev = Node

  def get_next():
    return self.next

  def get_prev():
    return self.prev

  def is_none():
    if self.d is None:
      return True
    return False
