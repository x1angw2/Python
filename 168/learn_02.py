import requests
import time

#get_image_url = 'http://183.64.133.160:6186/Function/ADataAshx/Verify_code.ashx?'

headers = {'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.114 Safari/537.36'}


def get_time():
    now_time = time.time()
    now_time = now_time / 1000000000 - 1
    return now_time

now_time = get_time()

get_image = 'http://183.64.133.160:6186/Function/ADataAshx/Verify_code.ashx?time=' + str(now_time)

data = {'time': now_time}



for i in range(100):
    response = requests.get(get_image,headers=headers)
    img_data = response.content
    with open(str(i)+'.jpg','wb') as f:
        f.write(img_data)
