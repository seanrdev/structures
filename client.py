#!/usr/bin/env python3
import argparse
import structures.singlelinkedlist as sll
import structures.node
import tester as test

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
    listing = sll.SingleLinkedList()
    testcase = test.Tester()
    testcase.run(listing)
