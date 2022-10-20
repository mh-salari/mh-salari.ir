---
layout: fa-post
custom_css: fa-post

title: "دستورات کاربردی بعد از نصب اوبونتو"
date: 2018-01-18T14:19:59+03:30
tags: [Linux]
image: /assets/post-images/linux/ubuntu-essentials/ubuntu_essentials.png
headerImage: true
description: "مجموعه دستورات کاربردی بعد از نصب اوبونتو"
category: Linux
author: Hue Salari
externalLink: false
---

من توی لینوکس تازه کارم و خیلی پیش میاد که می‌زنم همه‌چیز رو آجر می‌کنم و مجبور می‌شم کل سیستم عامل رو از اول نصب کنم، برای راحت‌تر شدن زندگیم کارهایی که بعد از نصب سیستم‌عامل جدید انجام می‌دم رو اینجا نوشته‌ام.

## Git رو نصب کنیم:
{% highlight bash linenos %}
sudo apt update
sudo apt upgrade
sudo apt install git
{% endhighlight %}

تنظیمات اولیه گیت رو انجام بدیم:

{% highlight bash linenos %}
git config --global user.name "your name"
git config --global user.email "your@email.com"
{% endhighlight %}

## zsh رو نصب کنیم:

{% highlight bash linenos %}
sudo apt install zsh
{% endhighlight %}

فعالش کنیم:

{% highlight bash linenos %}
sudo usermod -s /user/bin/zsh ${USER}
{% endhighlight %}

تنظیمات «اوه مای زیشل» رو نصب کنیم:

{% highlight bash linenos %}
sh -c "$(wget https://raw.githubusercontent.com/robbyrussell/oh-my-zsh/master/tools/install.sh -O -)"
{% endhighlight %}

zsh رو به فایل ترمینال‌هامون اضافه کنیم:

{% highlight bash linenos %}
command -v zsh | sudo tee -a /etc/shells
{% endhighlight %}

ترمینال پیشفرض رو zsh کنیم:

{% highlight bash linenos %}
sudo chsh -s "$(command -v zsh)" "${USER}"
{% endhighlight %}



## ویدئو پلیر کله قندی رو نصب کنیم:

{% highlight bash linenos %}
sudo apt install vlc
{% endhighlight %}

## دانلود منیجر _uGet_ رو نصب کنیم:

{% highlight bash linenos %}
sudo add-apt-repository ppa:plushuang-tw/uget-stable
sudo apt update
sudo apt install uget
{% endhighlight %}

## برای انجام  شخصی سازی _(GNOME) Tweaks_ رو نصب کنیم:

{% highlight bash linenos %}
sudo apt install gnome-tweak-tool
{% endhighlight %}

## برای گرفتن اسکرین شات از صفحه _shutter_ رو نصب کنیم:
{% highlight bash linenos %}
sudo apt-repository ppa:linuxuprising/shutter
sudo apt install shutter
{% endhighlight %}


