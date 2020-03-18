#!/usr/bin/python

import argparse


def find_max_profit(prices):
    best_profit = float('-inf')

    for i in range(len(prices)-1, 0, -1):
        for j in range(i-1, -1, -1):
            if prices[i] - prices[j] > best_profit:
                best_profit = prices[i] - prices[j]

    return best_profit


if __name__ == '__main__':
    # This is just some code to accept inputs from the command line
    parser = argparse.ArgumentParser(
        description='Find max profit from prices.')
    parser.add_argument('integers', metavar='N', type=int,
                        nargs='+', help='an integer price')
    args = parser.parse_args()

    print("A profit of ${profit} can be made from the stock prices {prices}.".format(
        profit=find_max_profit(args.integers), prices=args.integers))
