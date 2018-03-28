#!/bin/bash
import random

if __name__ == '__main__':
    if random.random() > 0.8:
        print('\n Hmm ... cat might be dead\n')
    else:
        print('\n Cat\'s alive\n')
