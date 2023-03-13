---
layout: project
custom_css: project
title: "arXivSquirrel"
# permalink: /projects/#
date:  2021-02-21 12:00:02 +0000
thumbnail: /assets/projects-images/arXivSquirrel/arXivSquirrel.png
description: "arXivSquirrel is a Go program that generates personalized RSS feeds from arXiv.org based on user keywords. It helps you stay up to date on the latest research papers in your field."
---

arXivSquirrel is a Go program that I developed to keep up to date on the latest computer vision papers. As a computer vision researcher, staying up to date on the latest papers is essential. However, keeping track of all the papers being published on arXiv.org can be a daunting task. That's why I decided to create arXivSquirrel to make my life easier.

One of the unique features of arXivSquirrel is that it includes the image version of the first five pages of each paper in the RSS feed. This means that I can quickly get a sense of the content of the paper without having to read the full title or abstract. This feature can save a lot of time and help to identify papers that I may want to read in more detail.

I wrote the arXivSquirrel code in a way that other people can use it and deploy it on their servers. To use arXivSquirrel, all you need to do is to provide a list of keywords related to your research interests. The bot then automatically generates an RSS feed that includes all the latest papers that match your keywords. You can use any RSS reader to subscribe to the feed and get updates whenever new papers are published.

![lifera Screenshot](/assets/projects-images/arXivSquirrel/lifera.png)
![feedreader Screenshot](/assets/projects-images/arXivSquirrel/feedreader.png)

In my experience, NewsFlash is the best RSS reader for arXivSquirrel. It's an open-source, simple-to-use application with an amazingly good user interface.

![NewsFlash Screenshot](/assets/projects-images/arXivSquirrel/NewsFlash.png)

To build arXivSquirrel, I used several go modules, including:

- xml                                # to generate new RSS file
- github.com/mmcdole/gofeed          # to parse arXiv.org RSS feed
- github.com/cavaliergopher/grab/v3  # to download papers pdf files
- github.com/karmdip-mi/go-fitz      # to extract images from the pdf files.

If you're a AI researcher, I highly recommend giving arXivSquirrel a try. It's a great tool for staying up to date on the latest papers and saving time in the process. You can find the source code for arXivSquirrel on its GitHub page at [https://github.com/mh-salari/arXivSquirrel](https://github.com/mh-salari/arXivSquirrel).

you can also find my personalized arXiv feed at this link: [https://arxiv.ai-hue.ir/arxiv.xml](https://arxiv.ai-hue.ir/arxiv.xml)
