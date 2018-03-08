# 微信开发代码

## /check
验证腾讯服务器

## /taiga/*
taiga小程序服务器端


## test
```bash
cd wechat
cp wechat/wechat/settings/locals.py.example wechat/wechat/settings/locals.py

pip install -r requirements.txt
python wechat/manage.py migrate
python wechat/manage.py runserver

open 'http://localhost:8000' 
```

## deploy 
/deploy: 配置文件目录

参考命令:
```bash
cd wechat
cp wechat/wechat/settings/locals.py.example wechat/wechat/settings/locals.py

pip install -r requirements.txt
python wechat/manage.py migrate
mkdir logs

ln -s /home/deploy/github/wechat/deploy/supervisor.conf /etc/supervisor/conf.d/wechat.conf
ln -s /home/deploy/github/wechat/deploy/nginx.conf /etc/nginx/sites-available/wechat
nginx -t
nginx -s reload

```

各种文件 仅供参考
