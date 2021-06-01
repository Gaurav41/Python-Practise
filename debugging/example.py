def add(x, y):
	z = x+y
	return z

if __name__ == "__main__":
	x = int(input("Num 1: "))
	y = int(input("Num 2: "))
	z = add(x,y)
	print(z)

#
# Microsoft Windows [Version 10.0.19042.685]
# (c) 2020 Microsoft Corporation. All rights reserved.
# C:\Users\NCS\AppData\Local\Programs\Python\Python39\python.exe: can't o
# pen file 'C:\Users\NCS\PycharmProjects\pythonProject\example.py': [Errn
# o 2] No such file or directory
#
# (PycharmEnv01) C:\Users\NCS\PycharmProjects\pythonProject>python debugg
# ing\example.py
# Num 1: 5
# Num 2: 5
# 55
#
# (PycharmEnv01) C:\Users\NCS\PycharmProjects\pythonProject>python -m pdb
#  example.py
# Error: example.py does not exist
#
# (PycharmEnv01) C:\Users\NCS\PycharmProjects\pythonProject>python -m pdb
# debugging\example.py
# F:\Cuelogic\Training\Python\environments\PycharmEnv01\Scripts\python.ex
# e: Error while finding module specification for 'pdbdebugging\\example.
# py' (ModuleNotFoundError: No module named 'pdbdebugging\\example'). Try
#  using 'pdbdebugging\example' instead of 'pdbdebugging\example.py' as t
# he module name.
#
# (PycharmEnv01) C:\Users\NCS\PycharmProjects\pythonProject>python -m pdb
#  debugging\example.py
# > c:\users\ncs\pycharmprojects\pythonproject\debugging\example.py(1)<mo
# dule>()
# -> def add(x, y):
# (Pdb) h
#
# Documented commands (type help <topic>):
# ========================================
# EOF    c          d        h         list      q        rv       undisp
# lay
# a      cl         debug    help      ll        quit     s        unt
#
# alias  clear      disable  ignore    longlist  r        source   until
#
# args   commands   display  interact  n         restart  step     up
#
# b      condition  down     j         next      return   tbreak   w
#
# break  cont       enable   jump      p         retval   u        whatis
#
# bt     continue   exit     l         pp        run      unalias  where
#
#
# Miscellaneous help topics:
# ==========================
# exec  pdb
#
# (Pdb) help next
# n(ext)
#         Continue execution until the next line in the current function
#         is reached or it returns.
# (Pdb) help continue
# c(ont(inue))
#         Continue execution, only stop when a breakpoint is encountered.
#
# (Pdb) w
#   c:\users\ncs\appdata\local\programs\python\python39\lib\bdb.py(580)ru
# n()
# -> exec(cmd, globals, locals)
#   <string>(1)<module>()
# > c:\users\ncs\pycharmprojects\pythonproject\debugging\example.py(1)<mo
# dule>()
# -> def add(x, y):
# (Pdb) n
# > c:\users\ncs\pycharmprojects\pythonproject\debugging\example.py(5)<mo
# dule>()
# -> if __name__ == "__main__":
# (Pdb)
# > c:\users\ncs\pycharmprojects\pythonproject\debugging\example.py(6)<mo
# dule>()
# -> x = input("Num 1: ")
# (Pdb)  2
# 2
# (Pdb)
# 2
# (Pdb) c
# Num 1: 55
# Num 2: 44
# 5544
# The program finished and will be restarted
# > c:\users\ncs\pycharmprojects\pythonproject\debugging\example.py(1)<mo
# dule>()
# -> def add(x, y):
# (Pdb) n
# > c:\users\ncs\pycharmprojects\pythonproject\debugging\example.py(5)<mo
# dule>()
# -> if __name__ == "__main__":
# (Pdb) n
# > c:\users\ncs\pycharmprojects\pythonproject\debugging\example.py(6)<mo
# dule>()
# -> x = input("Num 1: ")
# (Pdb) n
# Num 1: 3
# > c:\users\ncs\pycharmprojects\pythonproject\debugging\example.py(7)<mo
# dule>()
# -> y = input("Num 2: ")
# (Pdb) print(x)
# 3
# (Pdb) n
# Num 2: 4
# > c:\users\ncs\pycharmprojects\pythonproject\debugging\example.py(8)<mo
# dule>()
# -> z = add(x,y)
# (Pdb) print(y)
# 4
# (Pdb) h
#
# Documented commands (type help <topic>):
# ========================================
# EOF    c          d        h         list      q        rv       undisp
# lay
# a      cl         debug    help      ll        quit     s        unt
#
# alias  clear      disable  ignore    longlist  r        source   until
#
# args   commands   display  interact  n         restart  step     up
#
# b      condition  down     j         next      return   tbreak   w
#
# break  cont       enable   jump      p         retval   u        whatis
#
# bt     continue   exit     l         pp        run      unalias  where
#
#
# Miscellaneous help topics:
# ==========================
# exec  pdb
#
# (Pdb) whatis x
# <class 'str'>
# (Pdb)  s
# --Call--
# > c:\users\ncs\pycharmprojects\pythonproject\debugging\example.py(1)add
# ()
# -> def add(x, y):
# (Pdb) n
# > c:\users\ncs\pycharmprojects\pythonproject\debugging\example.py(2)add
# ()
# -> z = x+y
# (Pdb) c
# 34
# The program finished and will be restarted
# > c:\users\ncs\pycharmprojects\pythonproject\debugging\example.py(1)<mo
# dule>()
# -> def add(x, y):
# (Pdb) c
# Num 1: 5
# Num 2: 5
# 55
# The program finished and will be restarted
# > c:\users\ncs\pycharmprojects\pythonproject\debugging\example.py(1)<mo
# dule>()
# -> def add(x, y):
# (Pdb) c
# Num 1: 5
# Num 2: 5
# 10
# The program finished and will be restarted
# > c:\users\ncs\pycharmprojects\pythonproject\debugging\example.py(1)<mo
# dule>()
# -> def add(x, y):
# (Pdb) help break
# b(reak) [ ([filename:]lineno | function) [, condition] ]
#         Without argument, list all breaks.
#
#         With a line number argument, set a break at this line in the
#         current file.  With a function name, set a break at the first
#         executable line of that function.  If a second argument is
#         present, it is a string specifying an expression which must
#         evaluate to true before the breakpoint is honored.
#
#         The line number may be prefixed with a filename and a colon,
#         to specify a breakpoint in another file (probably one that
#         hasn't been loaded yet).  The file is searched for on
#         sys.path; the .py suffix may be omitted.
# (Pdb) break 8
# Breakpoint 1 at c:\users\ncs\pycharmprojects\pythonproject\debugging\ex
# ample.py:8
# (Pdb) c
# Num 1: 5
# Num 2: 5
# > c:\users\ncs\pycharmprojects\pythonproject\debugging\example.py(8)<mo
# dule>()
# -> z = add(x,y)
# (Pdb) whatis x
# <class 'int'>
# (Pdb) c
# 10
# The program finished and will be restarted
# > c:\users\ncs\pycharmprojects\pythonproject\debugging\example.py(1)<mo
# dule>()
# -> def add(x, y):
# (Pdb) c
# Num 1: 5
# Num 2: 5
# > c:\users\ncs\pycharmprojects\pythonproject\debugging\example.py(8)<mo
# dule>()
# -> z = add(x,y)
# (Pdb) c
# 10
# The program finished and will be restarted
# > c:\users\ncs\pycharmprojects\pythonproject\debugging\example.py(1)<mo
# dule>()
# -> def add(x, y):
# (Pdb) q
#
# (PycharmEnv01) C:\Users\NCS\PycharmProjects\pythonProject>python -m pdb
#  debugging\example.py
