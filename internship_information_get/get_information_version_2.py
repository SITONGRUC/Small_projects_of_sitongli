import pandas as pd
import re
import numpy as np
import requests
import pandas as pd
import datetime
headers = {"User-Agent": 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/113.0.0.0 Safari/537.36'}
def get_cicc_intern(x):
    list_total_list = []
    for i in range(x):
        link = 'https://cicc.zhiye.com/project2022/?c=-1&p=3%5E-1%2C1%5E-1&day=-1&PageIndex='+str(i)+'&class=2'
        res = requests.get(link,headers = headers)
        reg ='<a href="/proxq?(.*?)"'
        link_list = list(map(lambda x:'http://cicc.zhiye.com/proxq'+x,list(set(re.findall(reg,res.text,re.S)))))
        list_total_list = list_total_list + link_list
    def get_inform(link):
        res = requests.get(link,headers = headers)
        reg1 = '<h2 class="title2 pb10 pt50">(.*?)</h2>'
        reg2 = '<li class="icon22">需求部门：<span class="col333">(.*?)</span></li> \n    <li class="icon13a">招聘类别：<span class="col333">(.*?)</span></li>\n    <!-- <li class="icon13a">招聘类别：<span class="col333 zhao_pin_lei_bie"></span></li> -->\n    <!--<li class="icon13b">工作形式：<span class="col333">(.*?)</span></li>-->\n    <li class="icon13c">发布时间：<span class="col333">(.*?)</span></li>\n    \n     <li class="icon13d" style="width:100%">工作地点：<span class="col333">(.*?)</span></li>\n     \n    <div class="cb"></div>\n   </ul>\n  </div><!--zwxqt end-->\n  <div class="zwxq"'
        trail_data = res.text
        reg1 = re.findall(reg1,trail_data,re.S)
        reg2 = list(re.findall(reg2,trail_data,re.S)[0])
        result = reg1+reg2 + [link]
        return result
    result = pd.DataFrame(list(map(get_inform,list_total_list)))
    result = result[[0,1,3,4,5,6]]
    result.columns = ['名称','部门','种类','日期','地点','链接']
    return result
  result = get_cicc_intern(4)
