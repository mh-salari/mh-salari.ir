---
layout: project
custom_css: project
title: "Davat(دوات)"
# permalink: /projects/#
date:  2021-02-21 12:00:05 +0000
thumbnail: /assets/projects-images/davat/davat.png
description: "A Python library for normalizing and cleaning Persian text for NLP applications."
---

When starting some NLP projects in Farsi, I noticed that the Persian NLP ecosystem lacked many basic text processing tools that are common in other languages. Unable to find a suitable text normalization library for my needs, I created Davat by developing regex patterns in Python to properly clean and normalize Persian text.

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
