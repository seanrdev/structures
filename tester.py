#!/usr/bin/env python3




class Tester:

  def __init__(self):
    print()

  def conduct_ll(self, structure):
    arbitrary_data = [1,2,3,4,5,6,7,8,9]
    for i in arbitrary_data:
      structure.add_node(i)
      print("adding: {}".format(i))
    size = structure.get_size()
    for i in range(size):
      print(structure.at_pos(i))
    print("This is the information at position 5: {}".format(structure.at_pos(5)))
    structure.remove_at_position(5)
    for i in range(structure.get_size()):
      print(structure.at_pos(i))
    if structure.contains(3):
      print("Contains 3")
    tlist = [10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,20]
    structure.add_list(tlist)
    structure.print_list()


  def run(self, data_structure):
    if data_structure.indentify() == "linkedlist":
      self.conduct_ll(data_structure)
    else:
      return

