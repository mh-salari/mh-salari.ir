---
layout: project
custom_css: project
title: "UR3"
# permalink: /projects/#
date: 2025-08-20
thumbnail: /assets/projects-images/ur3/ur3.gif
hero: /assets/projects-images/ur3/ur3.mp4
description: A ROS 2 + MoveIt 2 Python control layer for the Universal Robots UR3e, with face- and color-tracking demos.
---

The UR3e robot arm is part of our lab inventory — we're the Interactive Technologies group, after all. Therefore one summer I took a course to learn how to actually use it, since we were discussing pulling the robot into one of my experiments.

The TL;DR: I updated the robot's firmware, wrote a Python control layer on top of ROS 2 + MoveIt 2 with safe joint control and collision avoidance, and shipped three demos — basic movement, color-based object tracking, and real-time face tracking.

Then I decided I never want to touch a robot I didn't build myself ever again. Way too many layers of software to keep straight: ROS 2, MoveIt 2, the UR driver, the controller's own firmware. It works, and I'm proud of it. But it's not where I want to spend my time.

I've since been told that a few master's students in the lab picked up the codebase and built their own work on top of it, which makes me happy.

Code: [github.com/mh-salari/ur3](https://github.com/mh-salari/ur3)
