---
layout: project
custom_css: project
title: "hafez-fal.ir"
# permalink: /projects/#
date: 2018-09-13
thumbnail: /assets/projects-images/hafez-fal/logo.png
description: "A clean, ad-free website for reading Hafez's poetry with an NLP-powered Twitter bot."
---

Hafez-fal.ir started in 2018 because I was fed up with existing Hafez poetry sites cluttered with ads. After discussing it one evening with [Kiavash](https://twitter.com/kiavash), we decided to build a clean, ad-free alternative.

![](/assets/projects-images/hafez-fal/ghazal-128.png)

We split the work based on our strengths. I scraped Hafez's poetry from various sources and maintained the texts. Kiavash designed and implemented the template (based on Bootstrap's cover template) and documented each ghazal for Mira, which handled content management. He also wrote the JavaScript random-selection logic for the fortune-telling feature. The result lives at [hafez-fal.ir](http://hafez-fal.ir).

At first the site had very few visitors, so I built a Twitter bot that tweets a random poem every day at 7:27 AM. To get more eyes on it, I also taught the bot to like any tweet mentioning "حافظ".

<img src="/assets/projects-images/hafez-fal/twitter.png" alt="Twitter bot" style="max-width: 500px; width: 100%; display: block; margin: 1.5rem auto;">

But "حافظ" has many meanings beyond the poet, so I added a filter to only like poetry-related tweets. The first version used ULMFit and reached 95.5% accuracy. Later I realized that was overkill — a few scikit-learn experiments with Bag-of-Words on the same dataset, without any preprocessing, hit 96.7%.

<img src="/assets/projects-images/hafez-fal/accuracy.jpeg" alt="Model accuracy comparison" style="max-width: 600px; width: 100%; display: block; margin: 1.5rem auto;">

In Spring 2026 the site was rewritten into a Progressive Web App with no frameworks or dependencies — you can install it like a native app and use it offline. The codebase lives at [github.com/sandoogh/hafez-fal.ir](https://github.com/sandoogh/hafez-fal.ir).

At the time of writing, Cloudflare reported about **15.48k unique visitors** and **1.32M requests** over the previous 30 days. I suspect a chunk of that is bots and AI crawlers, so the real human number is probably lower — but that's what the dashboard tells me.

<img src="/assets/projects-images/hafez-fal/overview.png" alt="Cloudflare stats overview" style="max-width: 700px; width: 100%; display: block; margin: 1.5rem auto;">

