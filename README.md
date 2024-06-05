<!--
 * @Author: Conghao Wong
 * @Date: 2023-03-28 09:14:00
 * @LastEditors: Conghao Wong
 * @LastEditTime: 2024-06-05 09:56:30
 * @Description: file content
 * @Github: https://cocoon2wong.github.io
 * Copyright 2023 Conghao Wong, All Rights Reserved.
-->

# SocialCircle Weights

This branch (https://github.com/cocoon2wong/Project-Monandaeg/tree/SocialCircle) includes several of our pre-trained SocialCircle models' weights.
You can download all these weights by clicking the green button `<> Code` above, and choose [`Download Zip`](https://github.com/cocoon2wong/Project-Monandaeg/archive/refs/heads/SocialCircle.zip).

## Usage

Clone the [SocialCircle Repo](https://github.com/cocoon2wong/SocialCircle), then

```bash
cd SocialCircle
```

Unzip weights files into any positions, then you can test one model (`evsczara1` as an example) like

```bash
python main.py -sc ${PATH_TO_WEIGHTS}/Project-Monandaeg-SocialCircle/evsczara1
```

## Note

This is a pretty large repository, so please use `git clone` or `git pull` with caution.
