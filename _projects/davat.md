---
layout: project
custom_css: project
title: "Davat(دوات)"
# permalink: /projects/#
date: 2021-05-03
thumbnail: /assets/projects-images/davat/davat-thumbnail.png
hero: /assets/projects-images/davat/davat.png
description: "A Python library for normalizing and cleaning Persian text for NLP applications."
---

<div style="display: flex; flex-wrap: wrap; gap: 6px 8px; align-items: center; justify-content: center; margin: 0 0 1.5rem;">
<a href="https://pypi.org/project/davat/"><img src="https://img.shields.io/pypi/v/davat" alt="PyPI version" style="height: 22px; vertical-align: middle;"></a>
<a href="https://pepy.tech/project/davat"><img src="https://static.pepy.tech/badge/davat" alt="Downloads" style="height: 22px; vertical-align: middle;"></a>
<a href="https://pypi.org/project/davat/"><img src="https://img.shields.io/pypi/l/davat" alt="License" style="height: 22px; vertical-align: middle;"></a>
<a href="https://github.com/mh-salari/davat"><img src="https://img.shields.io/badge/code-GitHub-181717?logo=github" alt="Code on GitHub" style="height: 22px; vertical-align: middle;"></a>
</div>

I wanted to enter the world of NLP in Persian, and the first wall I hit was word normalization. People casually mix Arabic and Persian letters, throw in inconsistent spacing, repeated characters, Arabic numerals next to Persian ones, and a long tail of similar quirks. I couldn't find a simple library for any of this, so I wrote Davat — a small Python package that uses regex to clean and normalize Persian text.

I later used Davat in my [Persian SMS spam classification research]({{ site.baseurl }}/publications/2023-farsi-sms-spam), where it became part of the preprocessing pipeline.

A quick taste of what it does:

```python
>>> from davat import normalize_persian

>>> normalize_persian("بِسْمِ اللَّهِ الرَّحْمنِ الرَّحِيمِ")
'بسم الله الرحمن الرحیم'
```

It also handles repeated-character collapse with an optional dictionary lookup:

```python
>>> normalize_persian("اللله", use_dictionary=True)
'الله'

>>> normalize_persian("موسسسسسه", use_dictionary=True)
'موسسه'
```

And a `clean()` function for end-to-end preprocessing — strips links, mentions, hashtags, emojis, and non-Persian characters in one call:

```python
>>> from davat import clean

>>> text = """متنی برای برسی تابع تمیز کردن متن
... که #هشتگ_ها را خیلی عاااااللللییییی!!!! تبدیل به متن عادی می‌کند!
... منشن‌ها @mh_salari و لینک‌ها www.mh-salari.ir را حذف می‌کند.
... حروف غیر فارسی  a b c d و اموجی‌ها :( 🐈‍ را حذف می‌کند
... علائم دستوری/نگارشی ?!٫ را حذف نمی‌کند
... و ...
... http://localhost:8888"""

>>> print(clean(text))
متنی برای برسی تابع تمیز کردن متن
که هشتگ_ها را خیلی عالی! تبدیل به متن عادی می‌کند!
منشن‌ها و لینک‌ها را حذف می‌کند.
حروف غیر فارسی و اموجی‌ها را حذف می‌کند
علائم دستوری/نگارشی؟!، را حذف نمی‌کند
و …
```
