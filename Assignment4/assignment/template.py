'''
This is a template for the Symbolic Execution Assignment.
The original files is taken from https://github.com/angr/angr-doc

It contains the function strcpy which is known to be vulnerable. The goal
of this assignment is to find strcpy(), identify an input that reaches it,
and in the end, input a custom message.
'''

import angr
import claripy
from pathlib import Path

def main():
    '''
     getFuncAddress is a helper function.

     For the assignment, you don't need to understand how it works —just 
     that you can use this function to get a function's address if the binary 
     is not stripped.

     If the binary is stripped, you won't be able to use this function.
     Then you will have to open the binary in a disassembler and find the 
     addresses of the functions you are trying to find/avoid rather than 
     using this helper function.
    '''
    def getFuncAddress( funcName, plt=None):
        found = [
            addr for addr,func in cfg.kb.functions.items()
            if funcName == func.name and (plt is None or func.is_plt == plt)
            ]
        if len( found ) > 0:
            print("Found "+funcName+"'s address at "+hex(found[0])+"!")
            return found[0]
        else:
            raise Exception("No address found for function : "+funcName)

    '''
     PART I:
     - load the binary SE_binary by replacing "None" below
     - optional: you can save time/memory if you avoid loading extra libs
    '''
    se_binary = Path(__file__).parent / "SE_binary"
    project = angr.Project("SE_binary", auto_load_libs=False) # PART I: replace None
    print(project.filename)
    '''
     PART II:
     We want a Control Flow Graph that we can use for getting the function addresses from symbols.
     - make a CFG from the project. Hint: You can read the documentation here https://docs.angr.io/en/latest/analyses/cfg.html
     - Optional: you can set fail_fast option to True to minimize how long this process takes.
    '''
    cfg = project.analyses.CFGFast() # PART II: replace None

    '''
     PART III:
     We know that strcpy can be vulnerable, so we want to locate its address in the binary. Since strcpy 
     is part of a shared library, we must set plt=True to search for its address in the Procedure Linkage 
     Table (PLT).
     - Use the getFuncAddress function to assign the correct addresses to addrStrcpy.
    '''
    addrStrcpy = getFuncAddress("strcpy", plt=True) # PART III: replace None

    '''
    PART IV:
    We want to create a list of arguments for the entry state.
    This list consists of
    - the filename of the binary. You can either write it as a string or get it by "project.filename".
    - a symbolic variable for the password buffer which we are trying to find. 
      Use claipy's BVS (bit-vector symbol) to make the symbolic variable.
      You can call the variable what ever you want. You also have to specify the maximum 
      number of bits, you will try to solve for. 40 bytes should be sufficient (so 8*40 bits).
    - a buffer we will use to copy in if the password is correct. When we find 
      a path to strcpy, we will check to make sure that this is the value that 
      is being copied. You can try with different strings, but "you can do it!" works.
    '''
    # PART IV: replace None with your list of the three arguments
    argv = [project.filename, claripy.BVS("password", 8*40), "you can do it!"]

    '''
    PART V:
     We want to specify the entry state and give it the arguments in argv.
     - Initialize an entry state starting at the address of the program entry point using entry_state().
       The entry_state() function takes "args" as argument.
    '''
    # PART V: replace None with the entry state
    initial_state = project.factory.entry_state(args=argv)
    
    '''
    PART VI:
     - Create a new SimulationManager from the entry state.
    '''
    sm = project.factory.simulation_manager(initial_state) # PART VI: replace None with the simulation manager

    '''
     This is a helper function that finds the path to strcpy where we control the source
     buffer. It examines a given program state, and ensures that execution has reached strcpy, and 
     that the source buffer contains our controlled input.
    '''
    def check(state):
        '''
          First we ensure that we're at strcpy
        '''
        if (state.ip.args[0] == addrStrcpy):
            '''
              Since RSI holds the memory adress of the source buffer being copied to strcpy,
              we can dereference RSI to get the actual buffer contents.
              We read the length matching our controlled input such that we can check if it equals
              the buffer we try to insert.
            '''
            BV_strCpySrc = state.memory.load( state.regs.rsi, len(argv[2]) )
            '''
              Now that we have the contents of the source buffer in the form of a bit
              vector, we grab its string representation using the current state's
              solver engine's function "eval" with cast_to set to str so we get a python string.
            '''
            strCpySrc = state.solver.eval( BV_strCpySrc , cast_to=bytes )
            '''
               Now we simply return True (found path) if we've found a path to strcpy
               where we control the source buffer, or False (keep looking for paths) if we
               don't control the source buffer
            '''
            return True if argv[2].encode() in strCpySrc else False
        else:
            '''
             If we aren't in the strcpy function, we need to tell angr to keep looking
             for new paths.
            '''
            return False

    '''
      PART VII:
      Now we want to automate finding the state, where we control the buffer.
      - Use the simulation manager's .explore() function with a find argument
        as well as the check() function to run until a state is found that matches 
        the specified conditions in check().
      - Store the result of calling explore() in the variable sm by replacing None below.
      - Optional: You can read more about the explore() function here: 
        https://docs.angr.io/en/latest/core-concepts/pathgroups.html
    '''
    sm = project.factory.simulation_manager(initial_state).explore(find=check) # PART VII: replace None with the simulation manager

    '''
      The following line retrieves all program states where the specified condition is met.
    '''
    found = sm.found
    '''
     Retrieve a concrete value for the password value from the found path.
     If you put this password in the program's first argument, you should be
     able to strcpy() any string you want into the destination buffer and
     cause a segmentation fault if it is too large.
    '''
    if len(found) > 0:    #   Make sure we found a path before giving the solution
        found = sm.found[0]
        result = found.solver.eval(argv[1], cast_to=bytes)
        print('The password is "%s"' % result)
    else:  
        print ("Couldn't find any paths which satisfied our conditions.")

if __name__ == "__main__":
    main()

'''
  PART VIII: To submit
  - Submit this file along with a screenshot of the password

  - Optional: Run the binary file SE_binary with the password and a message to store:
    ./SE_binary <password> <message_to_store>
    This may require linux. I used multipass to run the file on MacOS.

    The output should be:
    "Your Message: <message_to_store>"

    If you haven't got the right password, the output will be:
    "Your Message: Wrong password!"

    OBS. The password doesn't contain backslash x even though Angr gives you this. This may be due to that
    the argument has more bytes
'''