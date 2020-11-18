from bs4 import BeautifulSoup
import requests
import csv
import bs4


# 检查url地址
def check_link(url):
    try:

        r = requests.get(url)
        r.raise_for_status()
        r.encoding = 'gbk'    //解决部分名字中含生僻字乱码问题
        return r.text
    except:
        print('无法链接服务器！！！')


# 爬取资源
def get_contents(ulist, rurl):
    soup = BeautifulSoup(rurl, 'lxml')
    trs = soup.find_all('tr')
    for tr in trs:
        ui = []
        for td in tr:
            ui.append(td.string)
        ulist.append(ui)

# 保存资源


def save_contents(urlist):
    with open("D:/2020年积分落户公示名单.csv", 'w') as f:
        writer = csv.writer(f)
        writer.writerow(['2020年积分落户公示名单'])
        for i in range(len(urlist)):
            writer.writerow([urlist[i][1],urlist[i][3],urlist[i][5],urlist[i][7],urlist[i][9]])

def main():
    urli = []
    url = "http://fuwu.rsj.beijing.gov.cn/nwesqintegralpublic/settlePerson/tablePage?name=&rows=6032&page=0"
    rs = check_link(url)
    get_contents(urli, rs)
    save_contents(urli)


main()
