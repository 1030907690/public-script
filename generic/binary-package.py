# -*- coding: utf-8 -*-
'''
zhouzhongqing
2019年12月23日20:49:37
打包成二进制可执行文件
'''

'''
打包单个exe文件
-F 选项可以打出一个exe文件，默认是 -D，意思是打成一个文件夹。
pyinstaller -F TestDataGen.py
打出的桌面程序去掉命令行黑框 -w 选项可以打桌面程序，去掉命令行黑框
pyinstaller -F -w TestDataGen.py
修改程序默认图标 -i 可以设置图标路径，将图标放在根目录：
pyinstaller -F -w -i gen.ico TestDataGen.py
'''


import sys

import os


if __name__ == '__main__':
    os.system("pip install  PyInstaller   -i https://pypi.tuna.tsinghua.edu.cn/simple/")
    file = sys.argv[1]
    os.system("pyinstaller -F  %s " % file)

'''
linux打包

[root@localhost binary-package]# /usr/local/python3.5/bin/pyinstaller -F binary-package.py 
145 INFO: PyInstaller: 3.5
146 INFO: Python: 3.5.2
147 INFO: Platform: Linux-5.3.12-1.el7.elrepo.x86_64-x86_64-with-centos-7.5.1804-Core
149 INFO: wrote /home/zzq/binary-package/binary-package.spec
154 INFO: UPX is not available.
158 INFO: Extending PYTHONPATH with paths
['/home/zzq/binary-package', '/home/zzq/binary-package']
158 INFO: checking Analysis
158 INFO: Building Analysis because Analysis-00.toc is non existent
159 INFO: Initializing module dependency graph...
163 INFO: Initializing module graph hooks...
168 INFO: Analyzing base_library.zip ...
9689 INFO: running Analysis Analysis-00.toc
9714 INFO: Caching module hooks...
9728 INFO: Analyzing /home/zzq/binary-package/binary-package.py
9742 INFO: Loading module hooks...
9742 INFO: Loading module hook "hook-xml.py"...
10536 INFO: Loading module hook "hook-encodings.py"...
10693 INFO: Loading module hook "hook-pydoc.py"...
10728 INFO: Looking for ctypes DLLs
10760 INFO: Analyzing run-time hooks ...
10777 INFO: Looking for dynamic libraries
11224 INFO: Looking for eggs
11225 INFO: Python library not in binary dependencies. Doing additional searching...
Traceback (most recent call last):
  File "/usr/local/python3.5/bin/pyinstaller", line 9, in <module>
    load_entry_point('PyInstaller==3.5', 'console_scripts', 'pyinstaller')()
  File "/usr/local/python3.5/lib/python3.5/site-packages/PyInstaller/__main__.py", line 111, in run
    run_build(pyi_config, spec_file, **vars(args))
  File "/usr/local/python3.5/lib/python3.5/site-packages/PyInstaller/__main__.py", line 63, in run_build
    PyInstaller.building.build_main.main(pyi_config, spec_file, **kwargs)
  File "/usr/local/python3.5/lib/python3.5/site-packages/PyInstaller/building/build_main.py", line 844, in main
    build(specfile, kw.get('distpath'), kw.get('workpath'), kw.get('clean_build'))
  File "/usr/local/python3.5/lib/python3.5/site-packages/PyInstaller/building/build_main.py", line 791, in build
    exec(code, spec_namespace)
  File "/home/zzq/binary-package/binary-package.spec", line 17, in <module>
    noarchive=False)
  File "/usr/local/python3.5/lib/python3.5/site-packages/PyInstaller/building/build_main.py", line 243, in __init__
    self.__postinit__()
  File "/usr/local/python3.5/lib/python3.5/site-packages/PyInstaller/building/datastruct.py", line 158, in __postinit__
    self.assemble()
  File "/usr/local/python3.5/lib/python3.5/site-packages/PyInstaller/building/build_main.py", line 575, in assemble
    self._check_python_library(self.binaries)
  File "/usr/local/python3.5/lib/python3.5/site-packages/PyInstaller/building/build_main.py", line 681, in _check_python_library
    raise IOError(msg)
OSError: Python library not found: libpython3.5m.so.1.0, libpython3.5m.so, libpython3.5mu.so.1.0, libpython3.5.so.1.0
This would mean your Python installation doesn't come with proper library files.
This usually happens by missing development package, or unsuitable build parameters of Python installation.

* On Debian/Ubuntu, you would need to install Python development packages
  * apt-get install python3-dev
  * apt-get install python-dev
* If you're building Python by yourself, please rebuild your Python with `--enable-shared` (or, `--enable-framework` on Darwin)

Clearly, rebuild your Python by ./configure --enable-shared, and make sure the $LD_LIBRARY_PATH does include your python3.6/lib path. Say if your python3.6.8 is installed 
at /home/bibao/python3.6, than use   export LD_LIBRARY_PATH=$LD_LIBRARY_PATH:/usr/local/python3.5/lib to add PATH.
'''

