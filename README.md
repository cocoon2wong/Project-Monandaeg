<!--
 * @Author: Conghao Wong
 * @Date: 2023-03-28 09:14:00
 * @LastEditors: Conghao Wong
 * @LastEditTime: 2026-02-06 09:35:14
 * @Description: file content
 * @Github: https://cocoon2wong.github.io
 * Copyright 2023 Conghao Wong, All Rights Reserved.
-->

# Encore Weights

This weights branch (https://github.com/cocoon2wong/Project-Monandaeg/tree/Enc) includes our pre-trained `Encore` models' weights.
You can download all these weights by clicking the green button `<> Code` above in the [repo page](https://github.com/cocoon2wong/Project-Monandaeg/tree/Enc), and choose [`Download Zip`](https://github.com/cocoon2wong/Project-Monandaeg/archive/refs/heads/Enc.zip), or just clicking the following button:

<div class="btn-normal-group" style="text-align: center;">
    <a class="btn btn-lg btn-normal" href="https://github.com/cocoon2wong/Project-Monandaeg/archive/refs/heads/Enc.zip">⬇️ Download Weights</a>
</div>

<!-- > [!NOTE]
> Due to file size limitations, weights of ablation variations are published in the [Rev_ablation](https://github.com/cocoon2wong/Project-Monandaeg/tree/Rev_ablation) branch. -->

## Usages

Clone the `Encore` ([https://github.com/cocoon2wong/Enc](https://github.com/cocoon2wong/Enc)) repo and initialize it, then unzip downloaded weights files into any positions.
You can test one model (`enczara1` as an example) like

```bash
python main.py -l ${PATH_TO_WEIGHTS}/enczara1
```

> [!WARNING]
> This is a pretty large repository, so please use `git clone` or `git pull` with caution.

If you DO want to clone this branch, please use

```bash
git clone --branch Enc --depth 1 https://github.com/cocoon2wong/Project-Monandaeg.git
```

## Results

These results could be obtained if all other codes were properly set.
(Might be with small differences due to the randomly sampled noise vector. Run a single model for multiple times to check model's generation capability is recommended.)

| Dataset | ADE | FDE |
| --- | --- | --- |
| eth       |
| hotel     | 0.1144149973988533 (meter)    | 0.1496908813714981 (meter) |
| univ      | 0.2308891266584396 (meter)    | 0.4013743400573733 (meter) |
| zara1     | 0.1692499667406082 (meter)    | 0.2857049405574795 (meter) |
| zara2     | 0.1260605007410049 (meter)    | 0.2178858816623687 (meter) |
| SDD       | 6.1143870353698731 (pixel)    | 9.8406696319580081 (pixel) |
| NBA@2.0s  | 2.0089097023010254 (foot)     | 2.4949486255645752 (foot) |
|           | 0.6123156772613526 (meter)    | 0.7604603410720825 (meter) |
| NBA@4.0s  | 3.6619672775268555 (foot)     | 4.4283628463745126 (foot) |
|           | 1.1161676261901856 (meter)    | 1.3497649955749517 (meter) |
| nuScenes (K=5) | 1.2448897361755371 (meter) | 2.7193241119384766 (meter) |
| nuScenes (K=10)| 0.9933908581733704 (meter) | 2.0258171558380127 (meter) |

## Visualization

Our main repo has provided a set of visualization code to help you faster learn how the proposed `Encore` model works.
You can use the following command to open a playground window (`pyqt6` is needed):

```bash
python playground/main.py -l ${PATH_TO_WEIGHTS}/enczara1
```

Then click the `Run` button to visualize your specific model's outputs (for the specific ego agent, which can be changed by clicking the `Random` button).
