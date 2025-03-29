---
layout: project
custom_css: project
title: "Emoji-Art"
# permalink: /projects/#
date:  2021-02-27 12:00:04 +0000
thumbnail: /assets/projects-images/emoji-art/1.png
description: "Converting images into emoji mosaics using PyTorch."
---

After seeing [@bwasti's](https://sigmoid.social/@bwasti/109592598903441446) creative image-to-emoji project, I created my own PyTorch implementation that transforms photos into mosaics made of 10x10 pixel emoji tiles.

The project started by building a dataset from standard emoji images found at [unicode.org](https://unicode.org/emoji/charts/full-emoji-list.html), using their 14x14 pixel PNG versions.

![dataset](/assets/projects-images/emoji-art/dataset.png)

To improve model training, I applied basic image augmentation with Gaussian blur and slight rotation to create more variation in the training data.

For the model, first, I overfitted `torchvision.models.resnet18()` and then this small model. Both worked fine, but I like the output of the resnet18 more. 

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

Resnet18 output: ![Resnet18 output](/assets/projects-images/emoji-art/mh.png)

EmojiNet output: ![EmojiNet output](/assets/projects-images/emoji-art/mh_mini.png)

I need to work on improving its speed (I have a problem making predictions on a batch of inputs), but I'm super happy with the results. I'll clean the code and release it sometime in the future and update this page :)

