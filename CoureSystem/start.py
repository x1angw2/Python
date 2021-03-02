# 软件启动入口

import os,sys

sys.path.append(os.path.dirname(__file__))

from core import src

if __name__ == '__main__':
    src.run()
