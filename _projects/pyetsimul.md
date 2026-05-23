---
layout: project
custom_css: project
title: "PyEtSimul"
# permalink: /projects/#
date: 2025-07-23
thumbnail: /assets/projects-images/pyetsimul/pyetsimul.png
description: "A Python framework for simulating video-based eye trackers by geometrically modeling eyes, cameras, and light sources."
---

<div style="display: flex; flex-wrap: wrap; gap: 6px 8px; align-items: center; justify-content: center; margin: 0 0 1.5rem;">
<a href="https://pypi.org/project/pyetsimul/"><img src="https://img.shields.io/pypi/v/pyetsimul" alt="PyPI version" style="height: 22px; vertical-align: middle;"></a>
<a href="https://pepy.tech/project/pyetsimul"><img src="https://static.pepy.tech/badge/pyetsimul" alt="Downloads" style="height: 22px; vertical-align: middle;"></a>
<a href="https://pypi.org/project/pyetsimul/"><img src="https://img.shields.io/pypi/l/pyetsimul" alt="License" style="height: 22px; vertical-align: middle;"></a>
<a href="https://pyetsimul.readthedocs.io/"><img src="https://readthedocs.org/projects/pyetsimul/badge/?version=latest" alt="Docs" style="height: 22px; vertical-align: middle;"></a>
<a href="https://doi.org/10.1145/3806023"><img src="https://img.shields.io/badge/DOI-10.1145%2F3806023-blue" alt="DOI" style="height: 22px; vertical-align: middle;"></a>
<a href="https://github.com/mh-salari/pyetsimul"><img src="https://img.shields.io/badge/code-GitHub-181717?logo=github" alt="Code on GitHub" style="height: 22px; vertical-align: middle;"></a>
</div>

For my PhD research on the pupil-size artifact (PSA), I needed a simulator where I could change pupil size while independently controlling pupil decentration. I found [et_simul](https://github.com/mh-salari/et_simul-1.01) (Böhme et al., 2008) and started using it, but I needed so many modifications that I decided to port the framework to Python and add the features I wanted along the way. That became PyEtSimul.

The simulator works geometrically, modeling reflection and refraction at the eye's surfaces: place eyes, cameras, and light sources anywhere in 3D, and it produces the synthetic eye-image features a video-based tracker would see. Pupil decentration was the feature I built it for, but the model has grown to cover non-circular pupils, conic corneas, eyelid occlusion, and camera distortion, among many other things. For full details, check the [paper]({{ site.baseurl }}/publications/2026-pyetsimul).

Code: [github.com/mh-salari/pyetsimul](https://github.com/mh-salari/pyetsimul)
