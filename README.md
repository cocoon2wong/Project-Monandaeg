<!--
 * @Author: Conghao Wong
 * @Date: 2023-03-28 09:14:00
 * @LastEditors: Conghao Wong
 * @LastEditTime: 2024-06-05 09:51:17
 * @Description: file content
 * @Github: https://cocoon2wong.github.io
 * Copyright 2023 Conghao Wong, All Rights Reserved.
-->

# SocialCircle+ Weights

This branch (https://github.com/cocoon2wong/Project-Monandaeg/tree/SocialCirclePlus) includes several of our pre-trained SocialCircle+ models' weights.
You can download all these weights by clicking the green button `<> Code` above, and choose [`Download Zip`](https://github.com/cocoon2wong/Project-Monandaeg/archive/refs/heads/SocialCirclePlus.zip).

## Usage

Clone the [SocialCirclePlus Repo](https://github.com/cocoon2wong/SocialCirclePlus), then

```bash
cd SocialCirclePlus
```

Unzip weights files into any positions, then you can test one model (`evspczara1_adaptive` as an example) like

```bash
python main.py -sc ${PATH_TO_WEIGHTS}/Project-Monandaeg-SocialCirclePlus/evspczara1_adaptive
```

## Note

This is a pretty large repository, so please use `git clone` or `git pull` with caution.
