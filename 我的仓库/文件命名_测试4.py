import os
import shutil

# 获取原始文件夹路径
source_folder = r"E:\python\文件重命名\文件命名"

# 获取目标文件夹路径
target_folder = r"E:\python\文件重命名\文件重命名-输出"

# 计数器用于记录连续空文件夹的次数
empty_folder_count = 0

def rename_files():
    # 声明全局变量
    global empty_folder_count  
    # 获取文件夹中的所有文件
    file_list = os.listdir(source_folder)
    if empty_folder_count >= 3:
        print("警告：检测到连续三次原始文件夹为空,请检查原始文件夹地址：", source_folder)
        return
    if len(file_list) == 0:
        empty_folder_count += 1
        print("警告：原始文件夹中没有任何文件。")
        #print(empty_folder_count)
        return
    
    # 询问用户是进行剪切操作还是粘贴操作
    operation = input("请选择操作（剪切/粘贴）剪切请输入0粘贴请输入1：")
    # 输入文件名称已获得该文件的修改时间
    # getmtime()函数返回的是文件的修改时间，而getctime()函数返回的是文件的创建时间
    def get_file_mtime(filename):
        file_path = os.path.join(source_folder, filename)
        return os.path.getmtime(file_path)
    # 根据文件的创建时间进行排序（从大到小）
    file_list.sort(key=get_file_mtime)
    # 创建文件夹
    os.makedirs(target_folder, exist_ok=True)

    for idx, file_name in enumerate(file_list):
        new_file_name = str(idx + 1) + os.path.splitext(file_name)[1]
        source_file_path = os.path.join(source_folder, file_name)
        new_file_path = os.path.join(target_folder, new_file_name)

        if operation == "0" :
            shutil.move(source_file_path, new_file_path)
            print(f"原文件{file_name}已重命名为{new_file_name}并剪切到{new_file_path}")
        elif operation == "1" :
            shutil.copy(source_file_path, new_file_path)
            print(f"原文件{file_name}已重命名为{new_file_name}并粘贴到{new_file_path}")
        else:
            print("无效的操作选择！请重新运行代码并选择正确的操作（移动/粘贴）")
            # 删除已创建的文件夹
            shutil.rmtree(target_folder)
            return
        
        # 重置计数器，因为找到了非空文件夹
        empty_folder_count = 0

rename_files()
print(empty_folder_count)