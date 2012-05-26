creghead
--------

creghead saves a lot of time when defining register access macros in C.
registers and bit(field)s are defined in a python input file using
simple lists and tuples, without any external configuration language.

features:
* bit access: set, clear, get
* field access: set, get
* reserved/unused fields

to generate and test the example header, cd to creghead and type:

    ./creghead.py examples/regs_ex1.py > examples/regs_ex1.h
    gcc examples/ex1.c -o ex1
    ./ex1

