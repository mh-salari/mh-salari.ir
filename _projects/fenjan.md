---
layout: project
custom_css: project
title: "Fenjan"
# permalink: /projects/#
date:  2021-02-30 12:00:01 +0000
thumbnail: /assets/projects-images/fenjan/greeting26.png
description: "A bot that finds Ph.D. positions from social media and university websites, delivering daily personalized updates."
---

To simplify the process of finding Ph.D. opportunities, I created Fenjan - a bot that automatically searches for relevant positions. The initial version scanned LinkedIn and Twitter for Ph.D. openings and delivered them to my inbox each morning.

![Fenjan V1 Screenshot](/assets/projects-images/fenjan/v1.png)

As friends expressed interest in using it, I expanded Fenjan to support multiple users with different research interests. The bot now sends tailored emails containing Ph.D. positions from the past 24 hours, with improved formatting for better readability.

![Fenjan V2 Screenshot](/assets/projects-images/fenjan/v2.png)

The project has grown to include university website scanning, with Fenjan currently monitoring 17 universities for open positions, making the job search process more efficient.

I used Python Twitter API and Selenium for searching Twitter and LinkedIn. All the codes for scraping universities' websites are written in Golang, and I save the search results in the SQLite database.

Fenjan also has a Mastodon bot that re-posts Ph.D. positions from Twitter to Sigmoid social. You can find it at [https://sigmoid.social/@fenjan](https://sigmoid.social/@fenjan). Its Mastodon bot has a few more features than the email bot. It downloads tweet images if available and posts them along with the tweet text. It also converts Twitter short links to their non-short format, as link shortening isn't encouraged in Mastodon.

![Fenjan Mastodon Screenshot](/assets/projects-images/fenjan/mastodon.png)

The code for the Fenjan project is available in this GitHub repository: [https://github.com/mh-salari/fenjan](https://github.com/mh-salari/fenjan)