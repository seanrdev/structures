#!/bin/python3
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

if __name__ == '__main__':
  args = retrieve_args()
  if args.link_list is True:
    print("Worked")
    listing = sll.SingleLinkedList()
    listing.add_node(5)
    test = listing.ret_hdata()
    print(test)
