---
layout: project
custom_css: project
title: "Cheshm"
# permalink: /projects/#
date: 2026-05-14
thumbnail: /assets/projects-images/cheshm/cheshm-thumbnail.png
hero: /assets/projects-images/cheshm/cheshm.png
description: A cross-platform C++ library with Python bindings packaging pupil, glint, and limbus detectors for grayscale eye images.
---

<div style="display: flex; flex-wrap: wrap; gap: 6px 8px; align-items: center; justify-content: center; margin: 0 0 1.5rem;">
<a href="https://pypi.org/project/cheshm/"><img src="https://img.shields.io/pypi/v/cheshm" alt="PyPI version" style="height: 22px; vertical-align: middle;"></a>
<a href="https://pepy.tech/project/cheshm"><img src="https://static.pepy.tech/badge/cheshm" alt="Downloads" style="height: 22px; vertical-align: middle;"></a>
<a href="https://pypi.org/project/cheshm/"><img src="https://img.shields.io/pypi/l/cheshm" alt="License" style="height: 22px; vertical-align: middle;"></a>
<a href="https://github.com/mh-salari/cheshm"><img src="https://img.shields.io/badge/code-GitHub-181717?logo=github" alt="Code on GitHub" style="height: 22px; vertical-align: middle;"></a>
</div>

I needed to test and use several pupil detectors for my work, and I couldn't find a single pip-installable tool that bundled them all together. So I wrote Cheshm — a cross-platform (Linux, macOS, Windows) C++ library with Python bindings that packages the most common pupil, glint, and limbus detectors in one place.

The pupil detectors implemented so far: Simple, Starburst, Swirski2D, ExCuSe, ElSe, PuRe, PuReST, and PupilLabs2D. There's also a Simple glint detector and three limbus detectors based on Daugman algorithms (integro-differential, active contour, and pupil-guided variants). On top of that, it does rigid alignment of two eye images using glint, pupil, or iris-texture features.

Both the C++ library and the Python bindings can be used headlessly inside any pupil-detection pipeline — that's the main use case.

Cheshm also ships with a small GUI for a quick visual check of what each detector finds on a single image:

<img src="/assets/projects-images/cheshm/cheshm-gui.png" alt="Cheshm GUI" style="width: 100%; display: block; margin: 1.5rem auto;">

If you want to *annotate* eye features at scale instead, the [EyE Annotation Tool]({{ site.baseurl }}/projects/eye-annotation-tool) is the better front-end — it uses Cheshm under the hood for its auto-detectors.

Code: [github.com/mh-salari/cheshm](https://github.com/mh-salari/cheshm)
