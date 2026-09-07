from bs4 import BeautifulSoup
import requests

response = requests.get('https://www.nate.com/')
source = response.text
#print(source)

soup = BeautifulSoup(source, 'html.parser')
# # result = soup.select("#olLiveIssueKeyword > li:nth-child(1) > a > span.txt_rank")
# # result = soup.select("#olLiveIssueKeyword > li > a > span.txt_rank")
# # result = soup.select("#olLiveIssueKeyword")
result = soup.select("#olLiveIssueKeyword > li:nth-child(1)") #list형식
result = soup.select("#olLiveIssueKeyword > li") #list형식
# print(result)

# print(result[0])
# print(result[0].find_all('span'))

for li in result:
    span = li.select_one('.txt_rank')
    # print(span)

    if span:
        print(span.get_text(strip=True))















# from bs4 import BeautifulSoup
# import requests

# response = requests.get('https://www.nate.com/')
# source = response.text
# #print(source)

# soup = BeautifulSoup(source, 'html.parser')
# result = soup.select("#olLiveIssueKeyword > li:nth-child(1)") #list형식
# print(result)