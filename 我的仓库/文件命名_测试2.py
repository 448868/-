import os
import shutil

# 获取原始文件夹路径
source_folder = r"E:\python\文件重命名\文件命名"

# 获取目标文件夹路径
target_folder = r"E:\python\文件重命名\文件重命名-输出"


# 获取文件夹中的所有文件
file_list = os.listdir(source_folder)
#print(file_list)

#getmtime()函数返回的是文件的修改时间，而getctime()函数返回的是文件的创建时间
def get_file_mtime(filename):
    file_path = os.path.join(source_folder, filename)
    return os.path.getmtime(file_path)

file_list.sort(key=get_file_mtime)
#print(file_list)

# 询问用户是进行移动操作还是粘贴操作
operation = input("请选择操作（移动/粘贴）移动请输入0粘贴请输入1：")

# 创建目标文件夹（如果不存在）
#os.makedirs()是一个函数，用于创建目录
#如果目录已经存在，那么这段代码不会抛出异常，也不会对目录做任何操作
#如果目录不存在，那么这段代码会创建该目录及其所有父级目录。
#exist_ok=True是一个关键字参数，表示如果目标目录已经存在，是否抛出异常
#如果exist_ok为True，则不会抛出异常，如果目标目录已经存在，则什么都不做；如果exist_ok为False，则会抛出FileExistsError异常。
os.makedirs(target_folder, exist_ok=True)

for idx, file_name in enumerate(file_list):
    #print(idx, file_name)
    #构建新的文件名
    #splitext()函数用于分割文件的扩展名
    new_file_name = str(idx + 1) + os.path.splitext(file_name)[1]
    #print(new_file_name)
    # 构建文件的完整路径
    source_file_path = os.path.join(source_folder, file_name)
    new_file_path = os.path.join(target_folder, new_file_name)
    #print(file_path)
    #print(new_file_path)
    # 根据用户选择进行移动或粘贴操作
    if operation == "0" :
        shutil.move(source_file_path, new_file_path)
        print(f"原文件{file_name}已重命名为{new_file_name}并移动到{new_file_path}")
    elif operation == "1" :
        shutil.copy(source_file_path, new_file_path)
        print(f"原文件{file_name}已重命名为{new_file_name}并粘贴到{new_file_path}")
    else:
        print("无效的操作选择！请重新运行代码并选择正确的操作（移动/粘贴）")

    #print(f"原文件{file_name}已重命名为{new_file_name}")
