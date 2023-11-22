import os

# 获取文件夹路径
folder_path = "E:\python\文件命名\文件命名"

# 获取文件夹中的所有文件
file_list = os.listdir(folder_path)
#print(file_list)
def get_file_mtime(filename):
    file_path = os.path.join(folder_path, filename)
    return os.path.getmtime(file_path)

file_list.sort(key=get_file_mtime)
#print(file_list)
for idx, file_name in enumerate(file_list):
    # 构建新的文件名str(idx + 1) 
    new_file_name = str(idx + 1) + os.path.splitext(file_name)[1]
    #print(new_file_name)
    # 构建文件的完整路径
    file_path = os.path.join(folder_path, file_name)
    new_file_path = os.path.join(folder_path, new_file_name)
    #print(file_path)
    #print(new_file_path)
    # 重命名文件
    os.rename(file_path, new_file_path)
    print(f"原文件{file_name}已重命名为{new_file_name}")
