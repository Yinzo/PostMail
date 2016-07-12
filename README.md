# PostMail
A simple mail server which can let you send a email only sending a POST request

# Quick start

0. install Flask
```bash
sudo pip install Flask
```
1. set up the configurations at the beginning of **postmail.py**
```python
DEFAULT_RECEIVER = ""       # 缺省的邮件接收邮箱
DEFAULT_SENDER_NAME = ""    # 缺省的发送者姓名
MAIL_HOST = ""              # SMTP服务器地址, 如 smtp.126.com
MAIL_ADDRESS = ""           # 服务器登录的邮箱地址
PASSWORD = ""               # 服务器登录的邮箱密码
```
2. run the server, the server is default running on port 80 and set on url of '/mail'.
```bash
python run.py
```
3. **use POST to send the mail!**
you don't even need to set the mail receiver!
```python
import requests

response = requests.post('http://www.yourserver.com/mail', data={
    'subject': "PostMail!",
    'content': "This mail is sent by PostMail!"
})
```

# Requirement
- Flask

# Advance

- Use a key to enchance security
modify the string at the beginnin of **postmail.py**
```python
SECRET_KEY = "your_key"             # 用于验证身份的key, 留空表示不启用key验证机制
```
Then all the request must contain the valid key as parameter
```python
import requests

response = requests.post('http://www.yourserver.com/mail', data={
    'key': "your_key",
    'subject': "PostMail!",
    'content': "This mail is sent by PostMail!"
})
```

# License
MIT

