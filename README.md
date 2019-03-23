# seleniumLearn
Some cases of using selenium to simulate browser to crawl web page information

下载selenium库和PhantomJS
```
pip install selenium
```

下载和安装PhantomJS [PhantomJS下载地址](http://phantomjs.org/download.html)
```
wget https://bitbucket.org/ariya/phantomjs/downloads/phantomjs-2.1.1-linux-x86_64.tar.bz2 # 此为centos下载方式
tar -jxvf phantomjs-2.1.1-linux-x86_64.tar.bz2 && rm ./phantomjs-2.1.1-linux-x86_64.tar.bz2
mv ./phantomjs-2.1.1-linux-x86_64 /usr/local/
# 配置环境变量
sudo vi /etc/profile 
# 文件末尾增加如下内容（根据自己文件路径进行设置）
export PATH=$PATH:/usr/local/phantomjs-2.1.1-linux-x86_64/bin
# 执行下边命令，使环境变量生效
source /etc/profile
# 执行下面命令，安装成功则有版本号返回
phantojs --version
```
