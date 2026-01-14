<!--
 * @Author: Conghao Wong
 * @Date: 2023-03-28 09:14:00
 * @LastEditors: Conghao Wong
 * @LastEditTime: 2026-01-14 14:36:54
 * @Description: file content
 * @Github: https://cocoon2wong.github.io
 * Copyright 2023 Conghao Wong, All Rights Reserved.
-->

# Encore Weights

This branch (https://github.com/cocoon2wong/Project-Monandaeg/tree/Enc) includes our pre-trained `Enc` models' weights.
You can download all these weights by clicking the green button `<> Code` above, and choose [`Download Zip`](https://github.com/cocoon2wong/Project-Monandaeg/archive/refs/heads/Enc.zip).

<!-- > [!NOTE]
> Due to file size limitations, weights of ablation variations are published in the [Rev_ablation](https://github.com/cocoon2wong/Project-Monandaeg/tree/Rev_ablation) branch. -->

## Usage

Clone the `Enc` ([https://github.com/cocoon2wong/Enc](https://github.com/cocoon2wong/Enc)) repo and initialize it, then unzip downloaded weights files into any positions.
You can test one model (`encsdd` as an example) like

```bash
python main.py -l ${PATH_TO_WEIGHTS}/Project-Monandaeg-Enc/encsdd
```

> [!WARNING]
> This is a pretty large repository, so please use `git clone` or `git pull` with caution.

If you DO want to clone this branch, please use

```bash
git clone --branch Enc --depth 1 https://github.com/cocoon2wong/Project-Monandaeg.git
```

