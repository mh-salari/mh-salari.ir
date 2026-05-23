---
layout: project
custom_css: project
title: "WOTW"
# permalink: /projects/#
date:  2021-02-25 12:00:07 +0000
thumbnail: /assets/projects-images/wotw/archive.png
description: "A search platform for finding Tehran stock market and cryptocurrency mentions across Telegram channels."
---

A stock market fever swept Iran a few years back, and I wanted in. As an entry point I decided to build my own prediction models. There was no API for Tehran Stock Exchange data at the time, so I scraped it in real time.

Then I realized doing my own technical analysis was probably not the wisest move. Better to mine it from people who actually knew what they were doing — and a lot of them were posting charts on Telegram. The problem: Telegram doesn't really have search; it's basically deep web. So I built a Telegram scraper, added a computer-vision model on top to separate technical charts from random images, and pushed everything into Elasticsearch to make it searchable.

The stack: Telethon for Telegram, Elasticsearch for storage and search, Flask for the web frontend, and a ResNet18 model for chart classification.

It's not a nice ending: I was broke at the time, and still am, but back then broke enough that I had to turn off an $8 server. I never even took a screenshot of the site. The only trace left online is in the [Wayback Machine](https://web.archive.org/). The data sits on a hard disk somewhere, the code in a private GitHub repo. I'm not touching either. Pure nostalgia at this point.

Later, a friend told me about an Iranian startup with a full team doing the same thing. Since then, every few years we still bring it up, half-shaking our heads — if we hadn't been that broke, we could have bought a few of the stocks we were tracking, kept the servers running, and ended up rich!

Anyway, I learned a lot from this one. Maybe I'll reboot it someday...
