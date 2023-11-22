import os

# 获取文件夹路径
folder_path = "your_folder_path"

# 获取文件夹中的所有文件
file_list = os.listdir(folder_path)

# 定义排序的关键函数
def get_file_mtime(filename):
    file_path = os.path.join(folder_path, filename)
    return os.path.getmtime(file_path)

# 根据文件的修改时间进行排序
file_list.sort(key=get_file_mtime)

# 逐个对文件进行重命名
for idx, file_name in enumerate(file_list):
    # 构建新的文件名
    new_file_name = str(idx + 1) + os.path.splitext(file_name)[1]
    # 构建文件的完整路径
    file_path = os.path.join(folder_path, file_name)
    new_file_path = os.path.join(folder_path, new_file_name)
    # 重命名文件
    os.rename(file_path, new_file_path)
