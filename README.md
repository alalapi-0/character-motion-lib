# Character Motion Lib

本项目用于将 RPG Maker 系列角色动作素材图切分为按方向分类的单帧 PNG 图片，方便在游戏或动画中直接调用。脚本现已支持批量处理 `assets/` 目录中的所有素材图。

## 素材说明

- 将待处理的角色素材图（.png 格式）放置于 `assets/` 目录下，可一次放入多张文件，例如：
  - `assets/Actor1.png`
  - `assets/Actor2.png`
- 每张素材图包含 8 组角色（2 行 × 4 列）。
- 每组角色由 `3 列 × 4 行` 共 12 帧组成：
  - 第 1 行：向下行走 (`walk_down`)
  - 第 2 行：向左行走 (`walk_left`)
  - 第 3 行：向右行走 (`walk_right`)
  - 第 4 行：向上行走 (`walk_up`)
- 每个角色组的宽度为整张图的 `1/4`，高度为整张图的 `1/2`；每帧宽度为组宽 `1/3`，每帧高度为组高 `1/4`。

## 使用方法

1. 确保已安装 [Pillow](https://python-pillow.org/) 图像库：

   ```bash
   pip install pillow
   ```

2. 在项目根目录执行脚本：

   ```bash
   python scripts/extract_motion.py
   ```

3. 脚本会自动遍历 `assets/` 目录下的所有 `.png` 文件，并按素材名输出至 `extracted_frames/` 目录。每个角色目录包含：
   - 四个方向的单帧 PNG 图像；
   - `preview.gif`：按向下、向左、向右、向上的顺序展示三帧行走循环，可用于快速预览；
   - `info.json`：记录角色 ID、方向顺序以及帧文件名，便于引擎或外部工具解析。

   示例结构：

   ```
   extracted_frames/
   ├── Actor1_character_01/
   │   ├── walk_down_0.png
   │   ├── walk_down_1.png
   │   ├── walk_down_2.png
   │   ├── walk_left_0.png
   │   ├── ...
   │   ├── preview.gif
   │   └── info.json
   ├── Actor1_character_02/
   │   └── ...
   └── Actor2_character_01/
       └── ...
   ```

   其中 `info.json` 的内容示例：

   ```json
   {
     "character_id": "Actor1_character_01",
     "directions": ["walk_down", "walk_left", "walk_right", "walk_up"],
     "frames_per_direction": 3,
     "frames": {
       "walk_down": ["walk_down_0.png", "walk_down_1.png", "walk_down_2.png"],
       "walk_left": ["walk_left_0.png", "walk_left_1.png", "walk_left_2.png"],
       "walk_right": ["walk_right_0.png", "walk_right_1.png", "walk_right_2.png"],
       "walk_up": ["walk_up_0.png", "walk_up_1.png", "walk_up_2.png"]
     }
   }
   ```

## 注意事项

- 输出图像保持原素材分辨率，未进行缩放或插值。
- 如果输出文件已存在会被覆盖，如需保留旧数据请提前备份。
