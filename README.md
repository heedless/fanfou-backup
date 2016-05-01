# fanfou-backup
使用python2写的饭否消息备份工具，通过oauth验证方式登录账号备份饭否消息（未来可能会添加饭否follow列表备份，备份内容的统计功能）。

## 使用方法
1. 填写申请的fanfou api，在fanfou_api_key.py中填入consumer_key和consumer_secret。
2. 获取token
```
$ python2 get_token.py
```
把获取到的链接用浏览器打开，点击“同意”。回到终端输入“y”回车然后把输入授权码(pin码)，回车。
3. 备份(xml或者json两种格式, 默认是在程序根目录生成backup.xml或者backup.json)，json的数据直接从饭否的拉下来只是进行文件合并处理，没有处理汉字编码。
```
$ python2 fanfou.py backup xml
```
格式为:
<?xml version="1.0" encoding="UTF-8"?>
<statuses>
<status><created_at>...</created_at>
		<id>...</id>
		<rawid>...</rawid>
		<text><![CDATA[...]]></text>
		...
</status>
</statuses>
或者
```
$ python2 fanfou.py backup json
```
格式为:
```
[{"created_at":" ... ","id":" ... ", ... },{"created_at":" ... ","id":" ... ", ... }, ...]
```


我的2万条消息共1000页花了七八分钟，大约55.4MB。

