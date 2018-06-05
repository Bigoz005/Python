#!/usr/bin/python
# -*- coding:  iso-8859-2 -*-
f= open('info.txt', 'w')
import platform
print platform.machine()
f.write(platform.system()+' '+platform.machine()+'\n'+platform.version()+'\n'+platform.platform()+'\n'+platform.processor()+'\n')
f.close
