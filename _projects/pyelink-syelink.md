---
layout: project
custom_css: project
title: "PyeLink and SyeLink"
# permalink: /projects/#
date: 2025-11-29
thumbnail: /assets/projects-images/pyelink-syelink/pyelink-syelink.png
description: "Python tools for running EyeLink 1000 Plus experiments and parsing the resulting data."
---

<div style="display: flex; flex-wrap: wrap; gap: 6px 8px; align-items: center; justify-content: center; margin: 0 0 1rem;">
<strong style="margin-right: 4px;">PyeLink:</strong>
<a href="https://pypi.org/project/pyelink/"><img src="https://img.shields.io/pypi/v/pyelink" alt="PyPI version" style="height: 22px; vertical-align: middle;"></a>
<a href="https://pepy.tech/project/pyelink"><img src="https://static.pepy.tech/badge/pyelink" alt="Downloads" style="height: 22px; vertical-align: middle;"></a>
<a href="https://pypi.org/project/pyelink/"><img src="https://img.shields.io/pypi/l/pyelink" alt="License" style="height: 22px; vertical-align: middle;"></a>
<a href="https://pyelink.readthedocs.io/"><img src="https://readthedocs.org/projects/pyelink/badge/?version=latest" alt="Docs" style="height: 22px; vertical-align: middle;"></a>
<a href="https://github.com/mh-salari/pyelink"><img src="https://img.shields.io/badge/code-GitHub-181717?logo=github" alt="Code on GitHub" style="height: 22px; vertical-align: middle;"></a>
</div>

<div style="display: flex; flex-wrap: wrap; gap: 6px 8px; align-items: center; justify-content: center; margin: 0 0 1.5rem;">
<strong style="margin-right: 4px;">SyeLink:</strong>
<a href="https://pypi.org/project/syelink/"><img src="https://img.shields.io/pypi/v/syelink" alt="PyPI version" style="height: 22px; vertical-align: middle;"></a>
<a href="https://pepy.tech/project/syelink"><img src="https://static.pepy.tech/badge/syelink" alt="Downloads" style="height: 22px; vertical-align: middle;"></a>
<a href="https://pypi.org/project/syelink/"><img src="https://img.shields.io/pypi/l/syelink" alt="License" style="height: 22px; vertical-align: middle;"></a>
<a href="https://syelink.readthedocs.io/"><img src="https://readthedocs.org/projects/syelink/badge/?version=latest" alt="Docs" style="height: 22px; vertical-align: middle;"></a>
<a href="https://github.com/mh-salari/syelink"><img src="https://img.shields.io/badge/code-GitHub-181717?logo=github" alt="Code on GitHub" style="height: 22px; vertical-align: middle;"></a>
</div>

For my work on the pupil-size artifact (PSA), I needed to know the pupil size during calibration and validation on the EyeLink 1000 Plus, and the available tools didn't give me a clean way to get it. Marcus Nyström and Diederick Niehorster shared their own code with me, and after days of refactoring it grew into two packages: PyeLink for controlling the EyeLink 1000 Plus, and SyeLink for parsing the resulting EDF files.

PyeLink exposes the pupil and corneal-reflection positions in the EyeLink 1000 Plus's own camera coordinate system, across the calibration, validation, and recording phases. SyeLink reads the resulting ASC files into structured JSON and CSV, with calibration and validation plots, usable as a Python library or from the command line. For full details, check the [paper]({{ site.baseurl }}/publications/2026-pyelink-syelink).

Since then I've been using both packages for a lot of recordings, fixing bugs as I went. At this point the only item left is the mouse registry, and then I'm done.

Code: [PyeLink](https://github.com/mh-salari/pyelink) · [SyeLink](https://github.com/mh-salari/syelink)
