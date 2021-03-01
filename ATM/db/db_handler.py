# 数据处理层
# 用于处理数据
import json
import os
from conf import settings


# 查
def select(username):
    user_path = os.path.join(
            settings.USER_DATA_PATH,f'{username}.json'
        )

    if os.path.exists(user_path):
        with open(user_path,'r',encoding='utf-8') as f:
            user_dict = json.load(f)
            return user_dict

# 存
def save(user_dict):
    username = user_dict.get('username')
    user_path = os.path.join(
            settings.USER_DATA_PATH,f'{username}.json'
        )

    with open(user_path,'w',encoding='utf-8') as f:
        json.dump(user_dict,f,ensure_ascii=False)
