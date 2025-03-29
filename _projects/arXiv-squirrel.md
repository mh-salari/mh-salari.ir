---
layout: project
custom_css: project
title: "arXivSquirrel"
# permalink: /projects/#
date:  2021-02-29 12:00:02 +0000
thumbnail: /assets/projects-images/arXivSquirrel/arXivSquirrel.png
description: "A Go program that creates personalized RSS feeds from arXiv.org based on your research keywords."
---

arXivSquirrel is a tool I built to help keep track of new computer vision papers. Following all the publications on arXiv.org can be overwhelming, so I created this program to filter papers based on my interests.

What makes arXivSquirrel different is that it includes images of the first five pages of each paper directly in the RSS feed. This visual preview helps quickly assess papers without reading through titles and abstracts, making it easier to identify which ones deserve closer attention.

The program is designed to be user-friendly and deployable by anyone. You simply provide a list of keywords related to your research interests, and arXivSquirrel generates an RSS feed with matching papers. It works with any standard RSS reader, delivering updates as new relevant papers are published.

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


