<!--
 * @Author: Conghao Wong
 * @Date: 2023-03-28 09:14:00
 * @LastEditors: Conghao Wong
 * @LastEditTime: 2024-12-04 15:00:52
 * @Description: file content
 * @Github: https://cocoon2wong.github.io
 * Copyright 2023 Conghao Wong, All Rights Reserved.
-->

# Resonance Weights

This branch (https://github.com/cocoon2wong/Project-Monandaeg/tree/Re) includes our pre-trained `Re` models' weights.
For more model weights of ablation variations, please refer to [this branch](https://github.com/cocoon2wong/Project-Monandaeg/tree/Re_appendix).
You can download all these weights by clicking the green button `<> Code` above, and choose [`Download Zip`](https://github.com/cocoon2wong/Project-Monandaeg/archive/refs/heads/Re.zip).

## Usage

Clone the `Re` ([https://github.com/cocoon2wong/Re](https://github.com/cocoon2wong/Re)) repo and initialize it, then unzip downloaded weights files into any positions.
You can test one model (`resdd` as an example) like

```bash
python main.py -l ${PATH_TO_WEIGHTS}/Project-Monandaeg-Re/resdd
```

## Note

This is a pretty large repository, so please use `git clone` or `git pull` with caution.
