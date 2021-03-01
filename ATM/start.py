# 程序入口

import sys
import os
from core import src


# 添加环境变量
ATM_path = os.path.dirname(__file__)
sys.path.append(ATM_path)

# 软件启动 ===> 用户视图层
if __name__ == '__main__':
    src.run()
