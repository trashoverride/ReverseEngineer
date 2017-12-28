	#!/bin/python
#
#
#use r2 -i script.py -d <target>
#
#trashoverride

import r2pipe

r2=r2pipe.open()

r2.cmd("aaa;afl")

#comand = "ood -m "
#comand = comand + "a"*800
#r2.cmd(comand)

r2.cmd("db main")
r2.cmd("dc")
#r2.cmd("s sym.sum ")






