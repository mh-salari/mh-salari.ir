---
layout: project
custom_css: project
title: "hafez-fal.ir"
# permalink: /projects/#
date:  2021-02-21 12:00:07 +0000
thumbnail: /assets/projects-images/hafez-fal/logo.png
description: "a minimal site for reading Hafez's poets with and NLP twitter bot!"
---

The story of Hafez-fal site started on the day when I got tired of Hafez fortune-telling sites that were full of advertisements. I shared my discomfort with [Kiavash](https://twitter.com/kiavash) and expressed my wish for a site that did not have so many ads that disturbed the eyes of Hafez readers. This is how we decided to build a fortune-telling site that does not have any ads and is very simple and clean.

![](/assets/projects-images/hafez-fal/landing-page.png)

Everyone did their part of the work: I collected the texts from the web with the help of Python, and Kiavash, who had previously written Mira, converted the data I sent to him into YAML files with the help of Perl, and then converted it into the Mira format. He also created a random function for fortune-telling. That's it, the site http://hafez-fal.ir, a simple, clean, and minimal site for reading Hafez's poets.

![](/assets/projects-images/hafez-fal/447.png)

At the beginning, Hafez-fal.ir did not have many visitors. So, I decided to create a Twitter bot for it that randomly tweets one of Hafez's poems every day at 7:27 AM. Additionally, to attract more audience, I added the ability to lock tweets containing the word "حافظ" to the Twitter bot.

![](/assets/projects-images/hafez-fal/twitter.png)

Since the word "حافظ" has many meanings apart from the poet, I initially implemented a filter that only liked tweets related to the poetry using ULMFit's deep neural network. This network achieved 95.5% accuracy. However, later on, I realized that a deep and heavy neural network was not needed for this task. I conducted some experiments with scikit-learn models on Bag of Words tokens on the same dataset without any preprocessing and achieved 96.7% accuracy!

![](/assets/projects-images/hafez-fal/accuracy.jpeg)

Currently, the Hafez-fal.ir receives an average number of 5.5k monthly visitors.

![](/assets/projects-images/hafez-fal/overview.png)

