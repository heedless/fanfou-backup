# fanfou-backup
使用 **python2** 写的饭否消息备份工具，通过 **oauth** 验证方式登录账号备份饭否消息（也许未来可能会添加饭否follow列表备份，备份内容的统计功能）。

## 使用方法
1. 填写申请的fanfou api，在 **fanfou_api_key.py** 中填入**consumer_key**和**consumer_secret**。
2. 第一次运行会获取oauth的token,把获取到的链接用浏览器打开，点击“同意”。回到终端输入“y”回车然后把输入授权码(pin码)，回车。 **oauth_token** 和 **oauth_token_secret** 会保存在程序根目录下的oauth2.db里面。
3. 备份xml或者json这两种格式, 只是执行`$ python2 fanfou.py`默认是在程序根目录生成xml格式 **backup时间.xml**，json的数据是直接从饭否的拉下来的，只是进行简单文件合并处理，并没有处理汉字解码。

### xml格式
```
$ python2 fanfou.py backup xml
```
输出格式为:
```
<?xml version="1.0" encoding="UTF-8"?>
<statuses>
<status><created_at>...</created_at>
		<id>...</id>
		<rawid>...</rawid>
		<text><![CDATA[...]]></text>
		...
</status>
</statuses>
```

### json格式
```
$ python2 fanfou.py backup json
```
输出格式为:
```
[{"created_at":" ... ","id":" ... ", ... },{"created_at":" ... ","id":" ... ", ... }, ...]
```


我的2万条消息共1000页花了七八分钟，大约55.4MB。

