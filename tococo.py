"""
@file: tococo.py
@author: Jw
@time: 2023/12/22 11:10
@env: Python,Numpy,Pandas，Pyecharts
@desc: json文件转coco格式的脚本
@ref:
"""
# import json
# import os
# import glob
#
# # 假设所有 JSON 文件都在一个文件夹中
# json_files = glob.glob('H:/test_png/*.json')  # 替换为您的文件夹路径
# # print(json_files)
#
# # COCO 格式的基本结构
# coco_format = {
#     "images": [],
#     "annotations": [],
#     "categories": [{"id": 1, "name": "person"}]  # 示例中只有 "person" 类别
# }
#
# # 用于跟踪 ID
# next_image_id = 1
# next_annotation_id = 1
#
# for json_file in json_files:
#     with open(json_file,encoding='utf-8') as f:
#         data = json.load(f)
#
#     # 图像信息
#     image_info = {
#         "id": next_image_id,
#         "file_name": data["imagePath"],
#         "height": data["imageHeight"],
#         "width": data["imageWidth"]
#     }
#     coco_format["images"].append(image_info)
#
#     # 标注信息
#     for shape in data["shapes"]:
#         if shape["shape_type"] != "rectangle":
#             continue  # 只处理矩形标注
#         x1, y1 = shape["points"][0]
#         x2, y2 = shape["points"][1]
#         width, height = x2 - x1, y2 - y1
#         annotation_info = {
#             "id": next_annotation_id,
#             "image_id": next_image_id,
#             "category_id": 1,  # 假设 "person" 对应类别 ID 为 1
#             "bbox": [x1, y1, width, height],
#             "area": width * height,
#             "iscrowd": 0
#         }
#         coco_format["annotations"].append(annotation_info)
#         next_annotation_id += 1
#         # print(next_image_id)
#     next_image_id += 1
#
# # 保存为 COCO 格式的 JSON 文件
# with open('my_format.json', 'w') as f:
#     json.dump(coco_format, f)
import json
import os
import glob
import numpy as np

# 假设所有 JSON 文件都在一个文件夹中
json_files = glob.glob('H:/test_png/*.json')  # 替换为您的文件夹路径

# COCO 格式的基本结构
coco_format = {
    "images": [],
    "annotations": [],
    "categories": [{"id": 1, "name": "person"}]  # 示例中只有 "person" 类别
}

# 用于跟踪 ID
next_image_id = 1
next_annotation_id = 1

for json_file in json_files:
    with open(json_file, encoding='utf-8') as f:
        data = json.load(f)

    # 图像信息
    image_info = {
        "id": next_image_id,
        "file_name": data["imagePath"],
        "height": data["imageHeight"],
        "width": data["imageWidth"]
    }
    coco_format["images"].append(image_info)

    # 检查是否存在 "shapes" 字段
    if "shapes" in data and data["shapes"]:
        # 标注信息
        for shape in data["shapes"]:
            if shape["shape_type"] != "rectangle":
                continue  # 只处理矩形标注
            x1, y1 = shape["points"][0]
            x2, y2 = shape["points"][1]
            width, height = x2 - x1, y2 - y1
            annotation_info = {
                "id": next_annotation_id,
                "image_id": next_image_id,
                "category_id": 1,  # 假设 "person" 对应类别 ID 为 1
                "bbox": [x1, y1, width, height],
                "area": width * height,
                "iscrowd": 0
            }
            coco_format["annotations"].append(annotation_info)
            next_annotation_id += 1
    else:
        # 如果没有 shapes，则添加一个空的标注
        annotation_info = {
            "id": next_annotation_id,
            "image_id": next_image_id,
            "category_id": 1,  # 这里仍然需要一个类别ID，即使它是空的
            "bbox": [],  # 空的边界框列表
            "area": 0,  # 面积为0
            "iscrowd": 0
        }
        coco_format["annotations"].append(annotation_info)
        next_annotation_id += 1

    next_image_id += 1

# 保存为 COCO 格式的 JSON 文件
with open('my_format1.json', 'w') as f:
    json.dump(coco_format, f)
