# jd商品价格跟踪
## 使用方法

1. 在[jd](https://jd.com)上面，选择自己要跟踪的商品，点击查看商品主页（详情页）。
2. 点击地址栏查看网页的url，如`https://item.jd.com/3290987.html`，或者`https://item.jd.com/3290977.html#crumb-wrap....xxxxxx`等其他各种形式。
3. 定位开头的`https://item.jd.com/num.html`，这个`num`就是商品的ID，记录下来
4. 打开脚本，将刚刚记录的商品ID到赋值给itemId变量
5. ./xjd.py，即可获取商品价格
6. 可定期触发脚本实现商品价格跟踪，如：linux可以用crontab

## 运行效果
```shell
[root@localhost xjd]# ./xjd.py 
===============================
[time]

2018-08-19 22:07:39
-------------------------------
[name]

三星(SAMSUNG) 970 EVO 500G M.2 NVMe 固态硬盘（MZ-V7E500BW）
-------------------------------
[price]

1299.00
-------------------------------
===============================
```
