# 存放配置信息

import os

# 获取项目根目录路径
BASE_PATH = os.path.dirname(os.path.dirname(__file__))


# 获取user_data文件夹路径
USER_DATA_PATH = os.path.join(BASE_PATH,'db','user_data')

# 商品信息文件夹
ChanPin1 = os.path.join(BASE_PATH,'db','shop_data','产品.json')
