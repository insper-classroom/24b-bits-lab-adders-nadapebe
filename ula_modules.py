#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""

"""

from myhdl import *


@block
def halfAdder(a, b, soma, carry):
    @always_comb
    def comb():
        soma.next = a ^ b
        carry.next = a & b

    return instances()


@block
def fullAdder(a, b, c, soma, carry):
    s = [Signal(bool(0)) for i in range(3)]
    haList = [None for i in range(2)]  # (1)

    haList[0] = halfAdder(a, b, s[0], s[1]) 
    haList[1] = halfAdder(c, s[0], soma, s[2])

    @always_comb
    def comb():
        carry.next = s[1] | s[2]

    return instances()


@block
def adder2bits(x, y, soma, carry):
    soma_intermediario = Signal(bool(0))
    carry_intermediario = Signal(bool(0))  
    
    
    full_1 = fullAdder(x[0], y[0], 0, soma[0], carry_intermediario)
    
    full_2 = fullAdder(x[1], y[1], carry_intermediario, soma[1], carry)

    return instances()


@block
def adder(x, y, soma, carry):
    n = len(x)

    vaium = [Signal(bool(0)) for i in range(n)]
    faList = [None for i in range(n)]

    for i in range(n):
        faList[i] = fullAdder(x[i], y[i], vaium[i - 1], soma[i], vaium[i])

    return instances()
