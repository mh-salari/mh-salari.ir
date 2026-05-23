---
layout: project
custom_css: project
title: "Fenjan"
# permalink: /projects/#
date: 2022-12-06
thumbnail: /assets/projects-images/fenjan/fenjan-thumbnail.png
hero: /assets/projects-images/fenjan/fenjan.png
description: "A bot that finds Ph.D. positions from social media and university websites, delivering daily personalized updates."
---

I was searching for PhD positions at the time and was too lazy to do it manually, so I spent endless hours hand-crafting hundreds of lines of code instead. The result was Fenjan — a small bot that scanned LinkedIn and Twitter for PhD openings each night and dropped them into my inbox every morning.

<img src="/assets/projects-images/fenjan/v1.png" alt="Fenjan v1 email" style="max-width: 600px; width: 100%; display: block; margin: 1.5rem auto;">

A few friends asked if they could use it too, so I extended Fenjan to support multiple users with their own keywords. Each morning, everyone got a personalized digest of PhD positions posted in the previous 24 hours.

<img src="/assets/projects-images/fenjan/v2.png" alt="Fenjan v2 email" style="max-width: 600px; width: 100%; display: block; margin: 1.5rem auto;">

Later I added scrapers for university job pages — 17 of them at its peak — to catch positions that never made it to social media.

Under the hood: Python with the Twitter API and Selenium handled the social-media side, Go handled the university scrapers, and SQLite stored everything.

There was also a Mastodon side bot at [sigmoid.social/@fenjan](https://sigmoid.social/@fenjan) that re-posted Twitter PhD positions to Mastodon. It pulled the tweet images along with the text and expanded shortened links, since Mastodon culture doesn't love link shorteners.

<img src="/assets/projects-images/fenjan/mastodon.png" alt="Fenjan Mastodon screenshot" style="max-width: 600px; width: 100%; display: block; margin: 1.5rem auto;">

The funny part: I got my own PhD position from one of these emails. On 2023-03-17, Fenjan delivered the tweet below — Roman Bednarik (now my supervisor) announcing the Eyes4ICU DC3 position. I applied, got in, and that's the position I ended up with.

<img src="/assets/projects-images/fenjan/phd-position-email.png" alt="The PhD position email Fenjan delivered" style="max-width: 600px; width: 100%; display: block; margin: 1.5rem auto;">

Soon after, Elon Musk bought Twitter and gutted the free API, which made the Twitter side of Fenjan impossible to keep running. LinkedIn also kept changing its layout and breaking my scrapers. Eventually I decided to turn the whole thing off. The codebase hasn't been maintained since, but it lives at [github.com/mh-salari/fenjan](https://github.com/mh-salari/fenjan).