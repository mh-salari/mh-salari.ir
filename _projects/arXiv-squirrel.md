---
layout: project
custom_css: project
title: "arXivSquirrel"
# permalink: /projects/#
date: 2023-01-20
thumbnail: /assets/projects-images/arXivSquirrel/arXivSquirrel-thumbnail.png
hero: /assets/projects-images/arXivSquirrel/arXivSquirrel.png
description: "A Go program that creates personalized RSS feeds from arXiv.org based on your research keywords."
---

arXivSquirrel is a tool I built to keep track of new computer-vision papers. Following arXiv directly is overwhelming, so I wanted something that filters papers by my keywords and drops them into my RSS reader.

The useful trick is that the generated feed embeds thumbnails of the first five pages of each paper, not just the title and abstract. Scanning a paper's figures is much faster than reading abstracts when you're deciding whether to dig in.

<img src="/assets/projects-images/arXivSquirrel/lifera.png" alt="Liferea screenshot" style="max-width: 600px; width: 100%; display: block; margin: 1.5rem auto;">

<img src="/assets/projects-images/arXivSquirrel/feedreader.png" alt="Feedreader screenshot" style="max-width: 600px; width: 100%; display: block; margin: 1.5rem auto;">

I personally use NewsFlash as the reader — open-source, simple, and the UI is nice to look at.

<img src="/assets/projects-images/arXivSquirrel/NewsFlash.png" alt="NewsFlash screenshot" style="max-width: 600px; width: 100%; display: block; margin: 1.5rem auto;">

Under the hood, it's a small Go program that polls arXiv's RSS, downloads each matched paper, extracts the first few pages as images with `go-fitz`, and rebuilds the feed with those previews embedded.

Code: [github.com/mh-salari/arXivSquirrel](https://github.com/mh-salari/arXivSquirrel)


