---
layout: project
custom_css: project
title: "Automatically extracting the optic disc area in fundus images"
# permalink: /projects/#
date: 2021-12-09
thumbnail: /assets/projects-images/OptDisc-Extractor/t0.png
description: "A project that automates the detection of optic discs in fundus images to assist with glaucoma screening."
---

My master's supervisor, [Mohammad Amin Shayegan](https://scholar.google.com/citations?user=M7q-hukAAAAJ&hl=en), once asked me to help two of his master's students with a data annotation tool. They were working with fundus images and needed bounding boxes around the optic disc.

Rather than manually labeling hundreds of images, I tried a more automated approach. From the literature, threshold methods could work, but picking the right threshold was the hard part. Using two known properties of the optic disc — it's roughly circular, and its size relative to the eye is fairly consistent — I wrote an OpenCV pipeline that sweeps threshold values until the detected region matches those expectations.

<div style="text-align: center; margin: 1.5rem 0;">
<div style="position: relative; width: 100%; max-width: 600px; padding-bottom: 33.75%; margin: 0 auto; display: inline-block;">
<iframe style="position: absolute; top: 0; left: 0; width: 100%; height: 100%;" src="https://www.youtube.com/embed/D-Nlaal8U8w" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" allowfullscreen></iframe>
</div>
</div>

Once that worked, I used the algorithm to auto-label the dataset and trained a ResNet34 with SmoothL1Loss to predict the top-left and bottom-right corners of the optic disc. Normalizing every image to a fixed size made the regression tractable.

Results of the deep learning model:

<img src="/assets/projects-images/OptDisc-Extractor/t2.jpeg" alt="Deep learning model results" style="max-width: 600px; width: 100%; display: block; margin: 1.5rem auto;">

I handed the labeled data over to the students and never followed up on what they ended up doing with it. On my end, this was one of my first attempts at auto-labeling images — and I'd like to do more of it in the future, since I still have a soft spot for classic computer vision and hand-crafted feature extractors!

Code: [github.com/mh-salari/self_training_optic_disc_localization](https://github.com/mh-salari/self_training_optic_disc_localization/blob/main/threshold_localization.ipynb)