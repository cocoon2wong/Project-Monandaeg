<!--
 * @Author: Conghao Wong
 * @Date: 2024-12-30 10:04:35
 * @LastEditors: Conghao Wong
 * @LastEditTime: 2025-05-08 09:33:58
 * @Github: https://cocoon2wong.github.io
 * Copyright 2025 Conghao Wong, All Rights Reserved.
-->

# Reverberation Weights

This branch (https://github.com/cocoon2wong/Project-Monandaeg/tree/Rev) includes our pre-trained `Rev` models' weights.
You can download all these weights by clicking the green button `<> Code` above, and choose [`Download Zip`](https://github.com/cocoon2wong/Project-Monandaeg/archive/refs/heads/Rev.zip).

> [!NOTE]
> Due to file size limitations, weights of ablation variations are published in the [Rev_ablation](https://github.com/cocoon2wong/Project-Monandaeg/tree/Rev_ablation) branch.

## Usage

Clone the `Rev` ([https://github.com/cocoon2wong/Rev](https://github.com/cocoon2wong/Rev)) repo and initialize it, then unzip downloaded weights files into any positions.
You can test one model (`revsdd` as an example) like

```bash
python main.py -l ${PATH_TO_WEIGHTS}/Project-Monandaeg-Re/revsdd
```

> [!WARNING]
> This is a pretty large repository, so please use `git clone` or `git pull` with caution.

If you DO want to clone this branch, please use

```bash
git clone --branch Rev --depth 1 https://github.com/cocoon2wong/Project-Monandaeg.git
```
