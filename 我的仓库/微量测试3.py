import os
import shutil

# 获取原始文件夹路径
source_folder = r"E:\python\文件重命名\文件命名"

# 获取目标文件夹路径
target_folder = r"E:\python\文件重命名\文件重命名-输出"


# 获取文件夹中的所有文件
file_list = os.listdir(source_folder)
print(file_list)


def get_file_mtime(filename):
    file_path = os.path.join(source_folder, filename)
    return os.path.getmtime(file_path)

file_list.sort(key=get_file_mtime)
print(file_list)