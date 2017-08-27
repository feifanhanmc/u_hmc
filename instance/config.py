# -*- coding: utf-8 -*-
'''
这个文件包含不应该出现在版本控制的配置变量。
其中有类似调用密钥和数据库URI连接密码。
同样也包括了你的应用中特有的不能放到阳光下的东西。
比如，你可能在config.py中设定DEBUG = False，
但在你自己的开发机上的instance/config.py设置DEBUG = True。
因为这个文件可以在config.py之后被载入，它将覆盖掉DEBUG = False，并设置DEBUG = True。
'''
DEBUG = True
SQLALCHEMY_ECHO = True
SECRET_KEY = 'Sm9obiBTY2hyb20ga2lja3MgYXNzasaf'
STRIPE_API_KEY = 'SmFjb2IgS2FwbGFuLU1vc3MgaXMgYSBoZXJvsfs'
SQLALCHEMY_DATABASE_URI= "mysql://root:root@localhost/hmc"