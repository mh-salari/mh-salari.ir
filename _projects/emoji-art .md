---
layout: project
custom_css: project
title: "Emoji-Art"
# permalink: /projects/#
date:  2021-02-21 12:00:04 +0000
thumbnail: /assets/projects-images/emoji-art/1.png
description: "Rendering Images as Emojis with PyTorch."
---

Inspired by [@bwasti's](https://sigmoid.social/@bwasti/109592598903441446) awesome image-to-emoji project, I built a PyTorch model that renders images as a series of 10-pixel by 10-pixel emojis. 

I created the dataset by downloading the 14-pixel by 14-pixel png images of emojis from https://unicode.org/emoji/charts/full-emoji-list.html.

![dataset](/assets/projects-images/emoji-art/dataset.png)

For transformation, I just did `transforms.GaussianBlur(kernel_size=(3, 3), sigma=(0.1, 0.9))` and `transforms.RandomRotation(degrees=5)`.

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

I need to work on improving its speed (I have a problem making predictions on a batch of inputs), but I'm super happy with the results. I'll clean the code and release it in the coming weeks and update this page.

