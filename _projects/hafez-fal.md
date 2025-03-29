---
layout: project
custom_css: project
title: "hafez-fal.ir"
# permalink: /projects/#
date:  2021-02-21 12:00:07 +0000
thumbnail: /assets/projects-images/hafez-fal/logo.png
description: "A clean, ad-free website for reading Hafez's poetry with an NLP-powered Twitter bot."
---

Hafez-fal.ir came about when I grew frustrated with existing Hafez poetry sites cluttered with advertisements. After discussing this with [Kiavash](https://twitter.com/kiavash), we decided to create a simple, ad-free alternative that would provide a better reading experience.

![](/assets/projects-images/hafez-fal/landing-page.png)

We divided the work based on our strengths: I used Python to collect the poetry texts from various sources, while Kiavash processed the data into YAML files using Perl and his Mira framework. He also implemented the JavaScript random selection function for the fortune-telling feature. The result is http://hafez-fal.ir - a clean, minimalist site focused entirely on Hafez's poetry.

![](/assets/projects-images/hafez-fal/447.png)

At the beginning, Hafez-fal.ir did not have many visitors. So, I decided to create a Twitter bot for it that randomly tweets one of Hafez's poems every day at 7:27 AM. Additionally, to attract more audience, I added the ability to like tweets containing the word "حافظ" to the Twitter bot.

![](/assets/projects-images/hafez-fal/twitter.png)

Since the word "حافظ" has many meanings apart from the poet, I initially implemented a filter to only like tweets related to the poetry using ULMFit's deep neural network. This network achieved 95.5% accuracy. However, later on, I realized that a deep and heavy neural network was not needed for this task. I conducted some experiments with scikit-learn models on Bag of Words tokens on the same dataset without any preprocessing and achieved 96.7% accuracy!

![](/assets/projects-images/hafez-fal/accuracy.jpeg)

Currently, the Hafez-fal.ir receives an average number of 5.5k monthly visitors.

![](/assets/projects-images/hafez-fal/overview.png)

