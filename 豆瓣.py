import requests


headers = {
    'User-Agent':  'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.183 Safari/537.36'


}
response = requests.get('https://movie.douban.com/j/search_subjects?type=movie&tag=%E7%83%AD%E9%97%A8&sort=recommend&page_limit=2000&page_start=0',headers=headers)
json_text = response.json()
text = []
gg = []
rate=[]
id = []
cover_y = []
# print(json_text['subjects'])
for i in json_text['subjects']:
    text.append(i['title'])
    gg.append(i['cover_x'])
    rate.append(i['rate'])
    id.append(i['id'])
    cover_y.append(i['cover_y'])




data = pd.DataFrame({'title':text,'cover_x':gg,"rate":rate,'cover_y':cover_y,'id':id})
data.to_csv('豆瓣.csv')


# print(dict(text))
#     print(i['title'])
