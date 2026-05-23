---
layout: project
custom_css: project
title: "Emoji-Art"
# permalink: /projects/#
date:  2021-02-27 12:00:04 +0000
thumbnail: /assets/projects-images/emoji-art/futurama.png
description: "Converting images into emoji mosaics using PyTorch."
---

After seeing [@bwasti's](https://sigmoid.social/@bwasti/109592598903441446) creative image-to-emoji project, I created my own PyTorch implementation that transforms photos into mosaics made of 10x10 pixel emoji tiles. 

I started by building a dataset from the standard emoji set on [unicode.org](https://unicode.org/emoji/charts/full-emoji-list.html), using their 14x14 pixel PNG versions. To give the model more to train on, I added light augmentation — Gaussian blur and a small random rotation.

For the model itself, I first overfitted `torchvision.models.resnet18()`, then tried the much smaller homegrown network below. Both worked, but the ResNet18 output looked cleaner to me.

```python
class EmojiNet(nn.Module):
  def __init__(self, num_classes):
    super(EmojiNet, self).__init__()

    self.feature_extractor = nn.Sequential(
        nn.Conv2d(in_channels=3, out_channels=8, kernel_size=3, stride=1),
        nn.ReLU(),
        nn.MaxPool2d(kernel_size=2),
        nn.Conv2d(in_channels=8, out_channels=32, kernel_size=3, stride=1),
        nn.ReLU(),
        nn.MaxPool2d(kernel_size=2)
        )
    
    self.clasifier = nn.Sequential(
        nn.Linear(in_features=32, out_features=256),
        nn.ReLU(),
        nn.Linear(in_features=256, out_features=num_classes),
    )


  def forward(self,x):
    x = self.feature_extractor(x)
    x = torch.flatten(x, 1)
    x = self.clasifier(x)

    return x
```

Resnet18 output:

<img src="/assets/projects-images/emoji-art/resnet-18-output.png" alt="Resnet18 output" style="max-width: 400px; width: 100%; display: block; margin: 1.5rem auto;">

EmojiNet output:

<img src="/assets/projects-images/emoji-art/emojinet-output.png" alt="EmojiNet output" style="max-width: 400px; width: 100%; display: block; margin: 1.5rem auto;">

One day I'll have enough time to re-train a simpler model and port it to C++ with every tip and trick I can find to make it run in real time. Then [I'll be enough](https://www.youtube.com/watch?v=pd6LYZrkEqQ).

<img src="/assets/projects-images/emoji-art/disenchantment.png" alt="Disenchantment scene as emoji mosaic" style="max-width: 600px; width: 100%; display: block; margin: 1.5rem auto;">

