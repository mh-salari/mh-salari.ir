---
layout: project
custom_css: project
title: "Automatically extracting the optic disc area in fundus images"
# permalink: /projects/#
date:  2021-02-21 12:00:03 +0000
thumbnail: /assets/projects-images/OptDisc-Extractor/t0.png
description: "This project aimed to automate the detection and localization of the optic disc in fundus images for efficient glaucoma detection."
---

The optic disc is a critical area for detecting glaucoma, as this condition primarily affects the optic disc and its surrounding areas. To improve the efficiency of glaucoma detection, I developed a simple yet effective threshold-based algorithm for automatically detecting the optic disc in fundus images.

I hate manually labeling images to train a deep learning model, and I'm the kind of developer who happily spends a couple of days automating a task that takes a couple of hours! So, I spent around a week on this project reading state-of-the-art papers regarding optic disc detection. I realized that a threshold method can be used to extract the optic-disc areas, but it's almost impossible to find the right threshold. However, we know a couple of facts about the optic disc: it's circular and has a fixed aspect ratio to the entire eye area.

So, I wrote a code that starts to extract optic disc areas from images and changes the threshold values until it finds an area that checks all of the criteria (check the code if you are interested in this part!).

<iframe width="560" height="315" src="https://www.youtube.com/embed/D-Nlaal8U8w" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" allowfullscreen></iframe>

Then, I used this threshold-based method to label my data and train a deep neural network for the final optic disc localization. I was able to achieve good results. The extracted regions can also be used to create an even more robust cropping system. I used OpenCV for the threshold-based method and ResNet34 with SmoothL1Loss for the deep learning part of it.
![deep learning results](/assets/projects-images/OptDisc-Extractor/t2.jpeg)

GitHub link: [https://github.com/mh-salari/self_training_optic_disc_localization/blob/main/threshold_localization.ipynb](https://github.com/mh-salari/self_training_optic_disc_localization/blob/main/threshold_localization.ipynb)