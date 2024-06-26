---
layout: fa-post
custom_css: fa-post

title: "اجرای کدهای python در لینوکس با استفاده از systemd"
date: 2020-05-29 5:07
tags: [ Python, Linux]
image: /assets/post-images/linux/autorun-a-python-script-using-systemd/python_systemd.png
headerImage: true
description: "آموزش اجرای اتوماتیک کدهای python هنگام روشن شدن سیستم با استفاده از systemd در لینوکس و اجرای مجدد اسکریپ python در صورت بروز خطا"
category: Linux
author: Mohammadhossein Salari
externalLink: false
---


صوت مساله بسیار ساده‌ست، ما کد pythonمون رو نوشتیم، تست کردیم، حالا می‌خوایم بذاریمش یک گوشه به شکل دائم اجرا شه.  
حداقل خواستمون اینه که:

1. موقع روشن شدن سیستم کد به شکل خودکار اجرا شه  
2. اگر در هر صورت خطایی رخ داد که باعث کرش کردن برنامه شد به شکل خودکار کدمون مجددا راه اندازی شده

در بین همه‌ی گزینه‌های ممکن برای انجام این کار systemd راحت‌ترین و سرراست ترین راه رسیدن به خواسته‌های بالاست و کیه که ندونه من چقدر تنبلی رو دوست دارم!

## ایجاد یک برنامه‌ی نمونه:

اول یک برنامه ساده درست کنیم که صرفا یک متن رو در یک حلقه‌ی بینهایت هر یک دقیقه یک بار در انتهای یک فایل اضافه کنه:



{% highlight python linenos %}
#!/usr/bin/python
from time import sleep

if __name__ == "__main__":
    n = 0
    while True:
        n += 1
        with open("/dos/codes/systemd_demo.txt", "a") as file:
            # get further user input/do stuff here
            file.write(f"{n} mississippi\n")
        sleep(1)
{% endhighlight %}

این برنامه رو به اسم systemd_demo.py ذخیره می‌کنیم.

اگر کد برنامه رو اجرا کنیم یک فایل به اسم systemd_demo.txt ایجاد خواهد شد:

![systemd tail](/assets/post-images/linux/autorun-a-python-script-using-systemd/systemd_tail.png)

دقت کنید که برای اجرای این کد از آدرس کامل محیط آناکوندام و آدرس فایلم استفاده کردم، در مرحله‌ی بعد به این آدرس کامل احتیاج داریم.

<span style="color:red">هشدار:</span>. حتما یک بار توی ترمینال آدرس کامل رو بزنید و برنامه رو اجرا کنید، به خاطر ساختار import کردن ماژول‌ها و … در python ممکنه کد شما وقتی این شکلی اونو فرا می‌خونی با مشکل مواجه شه.


## ایجاد فایل service:

با ویرایشگر دلخواهتون یک فایل با اسم مورد نظر خودتون (که مرتبط با اسم برنامه‌ای شما باشه) در آدرس /lib/systemd/system/ و با پسوند
service. ایجاد کنید.

من از ویرایشگر nano استفاده می‌کنم، اگر nano رو نصب دارید کافیه در دستور زیر جای YOUR_SERVICE_NAME اسم مورد نظر خودتون رو بذارید.

&nbsp;
{% highlight bash%}
sudo nano /lib/systemd/system/YOUR_SERVICE_NAME.service
{% endhighlight %}
&nbsp;

ساختار کلی‌ای که برای ایجاد یک service لازم داریم به شکل زیره:


{% highlight bash linenos %}
[Unit]
Description=YOUR SERVICE DESCRIPTION FOR HUMANS
After=multi-user.target
Conflicts=getty@tty1.service

[Service]
Type=simple
ExecStart=YOUR PYTHON CODE EXECUTE COMMAND
StandardInput=tty-force
RemainAfterExit=yes
Restart=on-failure
RestartSec=5s

[Install]
WantedBy=multi-user.target
{% endhighlight %}



در ساختار بالا:

 - بجای YOUR SERVICE DESCRIPTION FOR HUMANS توضیحات مرتبط با اینکه این کد/سرویس چی هست رو می‌نویسیم.
 -  بجای YOUR PYTHON CODE EXECUTE COMMAND دستور اجرای فایل خودمون وارد می‌کنیم.
 - اگر می‌خوایم بعد از اتمام حلقه‌ی اصلی برنامه python اون service فعال بمونه مقدار RemainAfterExit رو برابر yes قرار می‌دیم.
 -  همچنین پارامتر RestartSec مقدار تاخیر هنگام اجرای مجدد کدمون رو مشخص می‌کنه.

ساختار فایل بالا رو من برای انجام برنامه‌ی مثال این پست به شکل زیر ویرایش کردم:


![systemd demo service-1](/assets/post-images/linux/autorun-a-python-script-using-systemd/systemd_demo_service-1.png)

## فعال سازی و اجرای service:

هر بار که ما در آدرس /lib/systemd/system/ فایلی می‌سازیم و یا در اون فایل‌ها تغییری ایجاد می‌کنیم نیازه تا systemctl رو راه اندازی مجدد کنیم تا تغییراتمون اعمال بشن، این کار با دستور زیر انجام می‌شه:

&nbsp;
{% highlight bash%}
sudo systemctl daemon-reload
{% endhighlight %}

&nbsp;
حال با دستورات زیر می‌تونیم serviceای که ایجاد کردیم رو مدیریت کنیم:



{% highlight bash linenos %}
#To enable running service
sudo systemctl enable YOUR_SERVICE_NAME.service

#To stop running service
sudo systemctl stop YOUR_SERVICE_NAME.service

#To start running service
sudo systemctl start YOUR_SERVICE_NAME.service

#To restart running service
sudo systemctl restart YOUR_SERVICE_NAME.service
{% endhighlight %}

اگر همه‌چیز به خوبی پیش رفته باشه چنین خروجی‌ای خواهید دید و دیتا شروع می‌کنه وارد فایل systemd_demo.txt شدن.


![sysemd status](/assets/post-images/linux/autorun-a-python-script-using-systemd/sysemd_status.png)

## منابع:

<div dir="ltr">

<a href="https://singlebrook.com/2017/10/23/auto-restart-crashed-service-systemd/">Auto-recovery of crashed services with systemd</a><br>
<a href="https://tecadmin.net/setup-autorun-python-script-using-systemd/">How To Setup Autorun a Python Script Using Systemd</a><br>
<a href="https://github.com/torfsen/python-systemd-tutorial">Writing a systemd Service in Python</a><br>
<a href="https://stackoverflow.com/questions/44136655/why-standardinput-tty-in-oneshot-systemd-unit-files">https://stackoverflow.com/questions/44136655/why-standardinput-tty-in-oneshot-systemd-unit-files</a><br>

</div>
