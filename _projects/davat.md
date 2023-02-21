---
layout: project
custom_css: project
title: "Davat(دوات)"
# permalink: /projects/#
date:  2021-02-21 12:00:05 +0000
thumbnail: /assets/projects-images/davat/davat.png
description: "A very simple python library for normalizing and cleaning Persian text."
---

I wanted to do a couple of NLP projects in Farsi, but soon realized that Farsi NLP community is very young and many components required for text processing are not available in Farsi. Text normalization and cleaning was one of the tools I needed for my project, and I couldn't find a good one. So, I spent a couple of nights writing regex codes in Python to normalize and clean Persian text.

Here is an example of the output of Davat:

```python 
>>> import davat

>>> sample_text = "بِسْمِ اللَّهِ الرَّحْمنِ الرَّحِيمِ"

>>> davat.normalize(sample_text)
'بسم الله الرحمن الرحیم'

>>> sample_text = """این یك متن تست است که حروف عربي ، کشیـــــده 
'اعداد 12345' و... دارد     که می خواهیم آن را نرمالایز کنیم ."""

>>> print(davat.normalize(sample_text))
این یک متن تست است که حروف عربی، کشیده
«اعداد ۱۲۳۴۵» و …  دارد  که می‌خواهیم آن را نرمالایز کنیم.

>>> sample_text = """
... متنی برای برسی تابع تمیز کردن متن
... که #هشتگ_ها را خیلی عاااااللللییییی!!!! تبدیل به متن عادی می‌کند!
... منشن‌ها @mh_salari و لینک‌ها www.mh-salari.ir را حذف می‌کند.
... حروف غیر فارسی  a b c d و اموجی‌ها :( 🐈‍ را حذف می‌کند
... علائم دستوری/نگارشی ?!٫ را حذف نمی‌کند
... و ...
... http://localhost:8888
... """

>>> text = davat.clean(sample_text)
>>> print(text)
متنی برای برسی تابع تمیز کردن متن 
 که هشتگ‌ها را خیلی عااللیی! تبدیل به متن عادی می‌کند! 
 منشن‌ها و لینک‌ها را حذف می‌کند. 
 حروف غیر فارسی و اموجی‌ها را حذف می‌کند 
 علائم دستوری/نگارشی؟!، را حذف نمی‌کند 
 و …
```


I created a PyPI page for it, which you can find at this link: [https://pypi.org/project/davat/](https://pypi.org/project/davat)

GitHub link: [https://github.com/mh-salari/davat](https://github.com/mh-salari/davat)
