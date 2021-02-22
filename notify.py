import smtplib,requests,urllib.parse

def readFile(filepath):
    with open(filepath,'r',encoding='UTF-8') as fp:
        content=fp.read()
    return content

def sendEnterpriseWechat(url):
    content = readFile(cupath.get_current_path() + '/log.txt')
    title = urllib.parse.quote("每日签到!")
    body = urllib.parse.quote(content)
    payload='title=' + title + '&body=' + body + '&touser=fengjijiao'
    headers = {
        'Content-Type': 'application/x-www-form-urlencoded'
    }
    response = requests.post(url, headers=headers, data=payload)
    print(response.text)
