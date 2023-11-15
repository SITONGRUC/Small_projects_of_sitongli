from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import pandas as pd
import re
import numpy as np

import requests
import pandas as pd
import datetime
import random
import pandas as pd
from collections import Counter
import numpy as np

headers = {"User-Agent": 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/113.0.0.0 Safari/537.36'}
def get_data(x):
    total_data = []
    for i in [str(i+1) for i in range(x)]:
        link = 'https://bbs.pku.edu.cn/v2/thread.php?bid=896&mode=topic&page='+i
        res = requests.get(link,headers = headers)
        total_data.append(res.text)
    total_data = '.'.join(total_data)
    total_list = re.findall('<!-- list item -->(.*?)<div class="time">(.*?)</div>\n',total_data,re.S)
    def trans(data_for_one):
        data_for_one = list(data_for_one)
        name = re.sub('&nbsp;','',re.findall('<div class="title l limit" style="max-width: 4.*?px;">(.*?)</div>',data_for_one[0],re.S)[0])
        link = 'https://bbs.pku.edu.cn/v2/'+re.sub('amp;','',re.findall('<div class="list-item-topic list-item" data-itemid=".*?"><a class="link" href="(.*?)"></a>',data_for_one[0],re.S)[0])
        time = data_for_one[1]
        return name,link,time
    return pd.DataFrame(map(trans, total_list))
