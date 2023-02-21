---
layout: project
custom_css: project
title: "Fenjan"
# permalink: /projects/#
date:  2021-02-21 12:00:01 +0000
thumbnail: /assets/projects-images/fenjan/greeting26.png
description: "Fenjan is a bot that searches for the latest Ph.D. positions on social media and universities' websites, and sends personalized emails to users every morning."
---

I'm a bit lazy when it comes to manually searching for Ph.D. programs on social media. So, I decided to build a bot to do it for me. I wrote a hundred lines of code, and thus Fenjan was born. It searches Linkedin and Twitter for the latest Ph.D. positions and sends me a personalized email every morning.

![Fenjan V1 Screenshot](/assets/projects-images/fenjan/v1.png)

A couple of my friends showed interest in the bot, so I added a new feature to Fenjan that lets me add the keywords of other people. Now, every morning, Fenjan sends its customers an email containing all the Ph.D. positions shared on Twitter and LinkedIn in the last 24 hours.
I also added a bit of CSS and HTML to it to make its emails easer to read.

![Fenjan V2 Screenshot](/assets/projects-images/fenjan/v2.png)

I am also slowly adding support for searching through my target universities' websites for open Ph.D. positions. Currently, Fenjan scrapes 17 universities for vacant Ph.D. positions.

I used Python Twitter API and Selenium for searching Twitter and LinkedIn. All the codes for scraping universities' websites are written in Golang, and I save the search results in the SQLite database.

Fenjan also has a Mastodon bot that re-posts Ph.D. positions from Twitter to Sigmoid social. You can find it at [https://sigmoid.social/@fenjan](https://sigmoid.social/@fenjan). Its Mastodon bot has a few more features than the email bot. It downloads tweet images if available and posts them along with the tweet text. It also converts Twitter short links to their non-short format, as link shortening isn't encouraged in Mastodon.

![Fenjan Mastodon Screenshot](/assets/projects-images/fenjan/mastodon.png)