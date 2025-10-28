# Character Motion Lib

本项目用于将 RPG Maker 系列角色动作素材图（以 `Actor1.png` 为例）切分为按方向分类的单帧 PNG 图片，方便在游戏或动画中直接调用。

## 素材说明

- 素材位于 `assets/Actor1.png`，包含 8 组角色（横向排列）。
- 每组角色由 `3 列 × 4 行` 共 12 帧组成：
  - 第 1 行：向下行走 (`walk_down`)
  - 第 2 行：向左行走 (`walk_left`)
  - 第 3 行：向右行走 (`walk_right`)
  - 第 4 行：向上行走 (`walk_up`)
- 每个角色组的宽度为整张图的 `1/8`，高度等于整张图高度；每帧宽度为组宽 `1/3`，每帧高度为组高 `1/4`。

## 使用方法

1. 将待处理的素材图命名为 `Actor1.png` 并放入 `assets/` 目录。
2. 确保已安装 [Pillow](https://python-pillow.org/) 图像库：

   ```bash
   pip install pillow
   ```

3. 在项目根目录执行脚本：

   ```bash
   python scripts/extract_motion.py
   ```

4. 切分后的帧图将输出到 `output/character_01` 至 `output/character_08` 目录中，并按方向命名，如：

   ```
   output/
   └── character_01/
       ├── walk_down_0.png
       ├── walk_down_1.png
       ├── walk_down_2.png
       ├── walk_left_0.png
       └── ...
   ```

## 注意事项

- 输出图像保持原素材分辨率，未进行缩放或插值。
- 每次运行脚本会覆盖同名输出文件，请注意备份重要数据。

