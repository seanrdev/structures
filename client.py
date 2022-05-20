#!/use/bin/env python3
import argparse
import structures.singlelinkedlist as sll
import structures.node

def retrieve_args():
  llhelp = "Implement a single direction linked list"
  parser = argparse.ArgumentParser()
  parser.add_argument('--ll', help=llhelp, default=False,
                      dest='link_list', action='store_true')
  args = parser.parse_args()
  return args


def test_case(structure):
  arbitrary_data = [1,2,3,4,5,6,7,8,9]
  for i in arbitrary_data:
    structure.add_node(i)
    print("adding: {}".format(i))
  size = structure.get_size()
  for i in range(size):
    print(structure.at_pos(i))


if __name__ == '__main__':
  args = retrieve_args()
  if args.link_list is True:
    print("Worked")
    listing = sll.SingleLinkedList()
    test_case(listing)
