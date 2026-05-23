---
layout: project
custom_css: project
title: "EyE Annotation Tool"
# permalink: /projects/#
date: 2024-08-22
thumbnail: /assets/projects-images/eye_annotation_tool/eye_annotation_tool-thumbnail.png
hero: /assets/projects-images/eye_annotation_tool/eye_annotation_tool.png
description: A Qt-based desktop tool for annotating pupil, iris, eyelid, and glints in eye images, with built-in auto-detectors.
---

<div style="display: flex; flex-wrap: wrap; gap: 6px 8px; align-items: center; justify-content: center; margin: 0 0 1.5rem;">
<a href="https://pypi.org/project/eye-annotation-tool/"><img src="https://img.shields.io/pypi/v/eye_annotation_tool" alt="PyPI version" style="height: 22px; vertical-align: middle;"></a>
<a href="https://pepy.tech/project/eye-annotation-tool"><img src="https://static.pepy.tech/badge/eye_annotation_tool" alt="Downloads" style="height: 22px; vertical-align: middle;"></a>
<a href="https://pypi.org/project/eye-annotation-tool/"><img src="https://img.shields.io/pypi/l/eye_annotation_tool" alt="License" style="height: 22px; vertical-align: middle;"></a>
<a href="https://doi.org/10.5281/zenodo.18723470"><img src="https://zenodo.org/badge/DOI/10.5281/zenodo.18723470.svg" alt="Zenodo DOI" style="height: 22px; vertical-align: middle;"></a>
<a href="https://github.com/mh-salari/eye_annotation_tool"><img src="https://img.shields.io/badge/code-GitHub-181717?logo=github" alt="Code on GitHub" style="height: 22px; vertical-align: middle;"></a>
</div>

Throughout my PhD I kept needing accurate, pixel-level annotations of eye features — pupil, limbus (iris), eyelid, and corneal-reflection glints. So over the last few years I've been working on this tool every now and then, growing it from a quick-and-dirty annotation script into a proper Qt desktop app.

It supports monocular and binocular projects with per-eye overrides for ROI, defaults, and carry behavior. The built-in auto-detectors — 8+ pupil detectors so far, a glint detector, and several limbus detectors — all come from [Cheshm]({{ site.baseurl }}/projects/cheshm), my detection library. Project sessions remember your defaults, with undo, a review mode, and a CLI for batch jobs.

Here's the main annotation view:

<img src="/assets/projects-images/eye_annotation_tool/main_page.png" alt="EyE Annotation Tool main interface" style="width: 100%; display: block; margin: 1.5rem auto;">

You can also add your own detectors. Drop a `.py` file into `~/.config/eye_annotation_tool/plugins/` (or any directory listed in the `EYE_ANNOTATION_PLUGINS` env var) that exports a `PLUGINS = [DetectorPlugin(...)]` list, and your detector shows up alongside the built-in ones.

Code: [github.com/mh-salari/eye_annotation_tool](https://github.com/mh-salari/eye_annotation_tool)