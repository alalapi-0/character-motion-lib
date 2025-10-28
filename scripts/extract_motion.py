"""角色动作图切分脚本。"""

from pathlib import Path
from typing import List

from PIL import Image

# 定义常量：角色数量与每组帧信息
GROUP_COLUMNS: int = 4  # 每行角色组数量
GROUP_ROWS: int = 2  # 每列角色组数量
CHARACTER_COUNT: int = GROUP_COLUMNS * GROUP_ROWS
COLUMNS_PER_GROUP: int = 3
ROWS_PER_GROUP: int = 4
DIRECTIONS: List[str] = [
    "walk_down",
    "walk_left",
    "walk_right",
    "walk_up",
]


def extract_frames(sheet_path: Path, output_root: Path) -> None:
    """从角色素材图中切分出所有角色动作帧并保存。

    :param sheet_path: 角色素材图路径
    :param output_root: 输出根目录
    """
    if not sheet_path.exists():
        raise FileNotFoundError(f"素材图不存在：{sheet_path}")

    # 打开素材图，并转换为支持透明度的 RGBA 模式
    sheet_image: Image.Image = Image.open(sheet_path).convert("RGBA")
    sheet_width, sheet_height = sheet_image.size

    # 计算每组角色的宽高（使用相对比例，不写死具体像素）
    group_width: float = sheet_width / GROUP_COLUMNS
    group_height: float = sheet_height / GROUP_ROWS

    # 每帧的宽度和高度（同样使用相对比例）
    frame_width: float = group_width / COLUMNS_PER_GROUP
    frame_height: float = group_height / ROWS_PER_GROUP

    # 获取素材名，用于输出目录前缀
    material_name: str = sheet_path.stem

    # 确保输出根目录存在
    output_root.mkdir(parents=True, exist_ok=True)

    for character_index in range(CHARACTER_COUNT):
        character_name: str = f"character_{character_index + 1:02d}"
        character_dir: Path = output_root / f"{material_name}_{character_name}"
        character_dir.mkdir(parents=True, exist_ok=True)

        # 计算当前角色组在整张图中的左上角坐标
        group_row: int = character_index // GROUP_COLUMNS
        group_column: int = character_index % GROUP_COLUMNS
        group_left: float = group_column * group_width
        group_top: float = group_row * group_height

        for row_index, direction in enumerate(DIRECTIONS):
            for column_index in range(COLUMNS_PER_GROUP):
                # 计算当前帧在整张图中的边界坐标
                left: int = round(group_left + column_index * frame_width)
                upper: int = round(group_top + row_index * frame_height)
                right: int = round(group_left + (column_index + 1) * frame_width)
                lower: int = round(group_top + (row_index + 1) * frame_height)

                frame_image: Image.Image = sheet_image.crop((left, upper, right, lower))

                output_path: Path = character_dir / f"{direction}_{column_index}.png"
                frame_image.save(output_path, "PNG")


if __name__ == "__main__":
    # 获取当前脚本所在项目根目录
    project_root: Path = Path(__file__).resolve().parent.parent
    assets_dir: Path = project_root / "assets"
    output_dir: Path = project_root / "output"

    # 素材图路径
    sheet_path: Path = assets_dir / "Actor1.png"

    # 执行切分
    extract_frames(sheet_path, output_dir)
