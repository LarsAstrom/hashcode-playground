#!/usr/bin/env python3
import argparse
import sys
import glob

from dataparser import parse, nl, ni
from util import path

try:     import matplotlib.pyplot as plt
except:  pass

# ns is the namespace.
# If needed write a simple parser which returns ns.
def test(tc_name, inp):
    print(tc_name)
    print('==============')
    ns = parse(inp)
    plt.scatter([2,3,4], [ns.T2, ns.T3, ns.T4])
    plt.show()
    ingredients = {}
    plt.scatter([i for i in range(len(ns.pizzas))], [len(pizza['ingredients']) for pizza in ns.pizzas])
    plt.show()
    for pizza in ns.pizzas:
        for ing in pizza['ingredients']:
            if ing not in ingredients:
                ingredients[ing]=0
            ingredients[ing]+=1
    print(len(ingredients))
    plt.scatter([i for i in range(len(ingredients))], ingredients.values())
    plt.show()
    # TODO: display inp in readable form!

def get_tasks():
    parser = argparse.ArgumentParser()
    parser.add_argument('testcase', nargs='?', default=None)
    parser.add_argument('-a', '--all', action='store_true')
    args = parser.parse_args()
    if not (args.testcase or args.all):
        print('provide either all: -a or a testcase.')
        exit()
    tasks = []
    if args.all:
        for f in sorted(glob.glob('in/*.in')):
            tc_name = path(f).name
            tasks.append(tc_name)
    else:
        tc_name = path(args.testcase).name
        tasks.append(tc_name)
    return tasks

if __name__=='__main__':
    tasks = get_tasks()

    for tc_name in tasks:
        in_file_name = 'in/{}.in'.format(tc_name)
        f = open(in_file_name)
        inp = f.read()
        f.close()
        test(tc_name, inp)
