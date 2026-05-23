---
layout: project
custom_css: project
title: "Zarafe"
# permalink: /projects/#
date: 2025-03-11
thumbnail: /assets/projects-images/zarafe/zarafe-thumbnail.png
hero: /assets/projects-images/zarafe/zarafe.png
description: A unified video annotation tool for time-marking events across different head-mounted eye trackers.
---

<div style="display: flex; flex-wrap: wrap; gap: 6px 8px; align-items: center; justify-content: center; margin: 0 0 1.5rem;">
<a href="https://pypi.org/project/zarafe/"><img src="https://img.shields.io/pypi/v/zarafe" alt="PyPI version" style="height: 22px; vertical-align: middle;"></a>
<a href="https://pepy.tech/project/zarafe"><img src="https://static.pepy.tech/badge/zarafe" alt="Downloads" style="height: 22px; vertical-align: middle;"></a>
<a href="https://pypi.org/project/zarafe/"><img src="https://img.shields.io/pypi/l/zarafe" alt="License" style="height: 22px; vertical-align: middle;"></a>
<a href="https://github.com/mh-salari/zarafe"><img src="https://img.shields.io/badge/code-GitHub-181717?logo=github" alt="Code on GitHub" style="height: 22px; vertical-align: middle;"></a>
</div>

For my [pupil-size artifact paper]({{ site.baseurl }}/publications/2025-psa-head-mounted), I needed to annotate eye-tracking data from four different head-mounted eye trackers — the Pupil Core, Pupil Neon, SMI ETG 2w, and Tobii Pro Glasses 2 — each with its own data format and its own proprietary annotation software. Learning four different tools just to mark the same kind of event timestamps felt absurd, so I wrote my own.

Zarafe works on the `worldCamera.mp4` + `gazeData.tsv` pair produced by [glassesValidator](https://github.com/dcnieho/glassesValidator) once each manufacturer's native recording is converted to that common format. Inside Zarafe you get the video with gaze position overlaid frame by frame, controls to create and manage time-based event annotations, and CSV export for downstream analysis.

Here's what the interface looks like in use:

<img src="/assets/projects-images/zarafe/app.png" alt="Zarafe application screenshot" style="width: 100%; display: block; margin: 1.5rem auto;">

Code: [github.com/mh-salari/zarafe](https://github.com/mh-salari/zarafe)