---
layout: project
custom_css: project
title: "Fixation Target"
# permalink: /projects/#
date: 2025-11-23
thumbnail: /assets/projects-images/fixation-target/targets.png
description: A Python package for generating customizable fixation targets sized in degrees of visual angle.
---

<div style="display: flex; flex-wrap: wrap; gap: 6px 8px; align-items: center; justify-content: center; margin: 0 0 1.5rem;">
<a href="https://pypi.org/project/fixation-target/"><img src="https://img.shields.io/pypi/v/fixation-target" alt="PyPI version" style="height: 22px; vertical-align: middle;"></a>
<a href="https://pepy.tech/project/fixation-target"><img src="https://static.pepy.tech/badge/fixation-target" alt="Downloads" style="height: 22px; vertical-align: middle;"></a>
<a href="https://pypi.org/project/fixation-target/"><img src="https://img.shields.io/pypi/l/fixation-target" alt="License" style="height: 22px; vertical-align: middle;"></a>
<a href="https://github.com/mh-salari/fixation-target"><img src="https://img.shields.io/badge/code-GitHub-181717?logo=github" alt="Code on GitHub" style="height: 22px; vertical-align: middle;"></a>
</div>

Every time I needed to put a fixation target on a screen, it was a 30-minute side quest — measure the current screen's pixel pitch, work out the viewing distance, convert degrees of visual angle to pixels, and generate an image at the right size. I finally got tired of redoing this and packaged it up. Since then *پوستم ۱۰ پله شفاف‌تر شده* — a Farsi saying that literally translates to "my skin has gotten ten steps clearer", and figuratively that my quality of life has improved.

The package generates the seven fixation target types from Thaler et al. (2013) — combinations of a center dot, an outer circle, and a cross. You specify all sizes in degrees of visual angle plus your screen parameters (width, height, resolution, viewing distance), and it produces a PNG (with optional 2× supersampling) and an SVG for the requested target.

<img src="/assets/projects-images/fixation-target/targets.png" alt="The seven fixation target types" style="max-width: 700px; width: 100%; display: block; margin: 1.5rem auto;">

There's a CLI for one-shot generation from a JSON config and a Python API for programmatic use — colors, background circle, dimensions are all configurable.

Code: [github.com/mh-salari/fixation-target](https://github.com/mh-salari/fixation-target)
