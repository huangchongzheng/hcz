import xml.etree.ElementTree as ET
import os

xml_path = "C:\\Users\\admin\\Downloads\\SDK_2_13_0_EVKB-IMXRT1050\\EVKB-IMXRT1050_manifest_v3_10.xml"

root = ET.parse(xml_path).getroot()
print(root.tag)
print(root.attrib["id"])
sdk_name = root.attrib["id"]
boards = root.findall("boards/board")
board_id = None
hell_world_project = None
for board in boards:
    print(board.attrib["id"])
    if board.attrib["id"] == "evkbimxrt1050":
        board_id = board.attrib["id"]
        h_prjs = board.findall("examples/example")
        for prj in h_prjs:
            if prj.attrib["name"] == "hello_world":
                print(prj.attrib)
                re_prj_path = prj.attrib["path"]
                prj_filenode = prj.find("external/files").attrib.get("mask")

                abs_path = os.path.join(os.path.dirname(xml_path), re_prj_path, prj_filenode)
                print(abs_path)
                print(os.path.exists(abs_path))
                hell_world_project = abs_path

updated_content = []
with open("build.properties", "r") as bf:
    contents = bf.readlines()

    for line in contents:
        print(line)
        if "board.id" in line:
            line = f"board.id             {board_id}\n"
        elif "example.xml" in line:
            line = f"example.xml          {hell_world_project}\n"
        elif "sdk.name" in line:
            line = f"sdk.name             {sdk_name}\n"
        elif "sdk.location" in line:
            line = f"sdk.location          {os.path.dirname(xml_path)}\n"

        updated_content.append(line)

with open("biuld1.properties", "w+") as f:
    f.writelines(updated_content)
