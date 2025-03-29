---
layout: project
custom_css: project
title: "Automatically extracting the optic disc area in fundus images"
# permalink: /projects/#
date:  2021-02-28 12:00:03 +0000
thumbnail: /assets/projects-images/OptDisc-Extractor/t0.png
description: "A project that automates the detection of optic discs in fundus images to assist with glaucoma screening."
---

The optic disc is an important area for detecting glaucoma, as this condition affects the optic disc and surrounding regions. To help with more efficient screening, I developed a threshold-based algorithm for automatically detecting the optic disc in fundus images.

Rather than manually labeling hundreds of images to train a deep learning model, I decided to find a more automated approach. After reviewing research papers on optic disc detection, I found that while threshold methods could work, determining the right threshold value was challenging. Working with what we know about optic discs (they're circular and have a consistent size ratio relative to the eye), I created a Python solution using OpenCV.

The algorithm intelligently adjusts threshold values until it identifies areas matching the expected optic disc characteristics, effectively automating what would otherwise be manual work.

<iframe width="560" height="315" src="https://www.youtube.com/embed/D-Nlaal8U8w" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" allowfullscreen></iframe>

Then, I used this threshold-based method to label all of the dataset and train a deep neural network for the final optic disc localization. I used ResNet34 with SmoothL1Loss to train a the deep learning model to predict the top-left and bottom-right corner of optic discs. This approach was possible because I normalized all of the images to a fixed size.


Results of the deep learning model:![deep learning results](/assets/projects-images/OptDisc-Extractor/t2.jpeg)

GitHub link: [https://github.com/mh-salari/self_training_optic_disc_localization/blob/main/threshold_localization.ipynb](https://github.com/mh-salari/self_training_optic_disc_localization/blob/main/threshold_localization.ipynb)