#!/usr/bin/env python
# source angrenv/bin/activate

'''
ais3_crackme has been developed by Tyler Nighswander (tylerni7) for ais3.

It is an easy crackme challenge. It checks the command line argument.
'''

import angr
import claripy


def main():
    project = angr.Project("ais3_crackme", auto_load_libs=False)

    #create an initial state with a symbolic bit vector as argv1
    argv1 = claripy.BVS("argv1",40*8) #since we do not know the length, we use a moderate size 40 bytes
    initial_state = project.factory.entry_state(args=[project.filename, argv1])

    #create a path group using the created initial state 
    sm = project.factory.simulation_manager(initial_state)

    #symbolically execute the program until we reach the wanted value of the instruction pointer
    sm.explore(find=0x400602) #at this instruction the binary will print(the "correct" message)

    found = sm.found

    if len(found) > 0:    #   Make sure we found a path before giving the solution
        found = sm.found[0]
        result = found.solver.eval(argv1, cast_to=bytes)
        #ask to the symbolic solver to get the value of argv1 in the reached state as a string
        try:
            print(result)
            result = result[:result.find(b"\x00")]
            print(result)
        except ValueError:
            pass
    else:   # Aww somehow we didn't find a path.  Time to work on that check() function!
        result = "Couldn't find any paths which satisfied our conditions."
    return result

if __name__ == '__main__':
    main()
