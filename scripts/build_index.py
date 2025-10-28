"""聚合所有角色 info.json 的辅助脚本。"""

import json
from pathlib import Path
from typing import Dict


def build_index(extracted_dir: Path) -> Dict[str, dict]:
    """遍历角色目录并收集 info.json 信息。

    :param extracted_dir: 存放角色帧图像的根目录
    :return: 以角色 ID 为键的完整信息字典
    """

    characters: Dict[str, dict] = {}

    if not extracted_dir.exists():
        return characters

    for character_dir in sorted(extracted_dir.iterdir()):
        if not character_dir.is_dir():
            continue

        info_path: Path = character_dir / "info.json"
        if not info_path.exists():
            continue

        try:
            info_data = json.loads(info_path.read_text(encoding="utf-8"))
        except json.JSONDecodeError:
            # 遇到无效 JSON 时跳过，避免脚本中断
            continue

        character_id = info_data.get("character_id") or character_dir.name
        characters[character_id] = info_data

    return characters


def main() -> None:
    """脚本入口：收集并输出聚合后的角色索引。"""

    project_root: Path = Path(__file__).resolve().parent.parent
    extracted_dir: Path = project_root / "extracted_frames"
    output_path: Path = extracted_dir / "characters_index.json"

    characters_index = build_index(extracted_dir)

    extracted_dir.mkdir(parents=True, exist_ok=True)
    output_path.write_text(
        json.dumps(characters_index, ensure_ascii=False, indent=2),
        encoding="utf-8",
    )

    print(f"已生成索引文件：{output_path}")


if __name__ == "__main__":
    main()
