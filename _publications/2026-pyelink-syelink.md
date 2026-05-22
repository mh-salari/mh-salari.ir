---
layout: publication
title: "PyeLink and SyeLink: Open-source Python tools for low-level EyeLink experiment control and data parsing"
authors: "Mohammadhossein Salari, Marcus Nyström, Diederick C. Niehorster, Roman Bednarik"
venue: "ACM Symposium on Eye Tracking Research and Applications (ETRA '26 Late-Breaking Work)"
year: 2026
date: 2026-06-01
doi: "10.1145/3797246.3805844"
---

PyeLink and SyeLink are two complementary open-source Python tools for running eye-tracking experiments and parsing data from SR Research Ltd. EyeLink hardware. PyeLink simplifies experiment creation with plug-and-play support for multiple display backends (Pygame, PsychoPy, Pyglet) and enables two features not available in existing tools: recording data during calibration and validation phases, and simultaneously recording raw pupil/corneal-reflection data alongside calibrated gaze data. SyeLink processes the resulting enriched ASC files into structured JSON and CSV formats through both a Python API and a command-line interface, with built-in visualization of calibration and validation results.

Tools: [PyeLink](https://github.com/mh-salari/pyelink) · [SyeLink](https://github.com/mh-salari/syelink) · [Demo](https://github.com/mh-salari/pyelink_and_syelink_etra_lbw_demo)
