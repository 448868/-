import os

target_folder = "E:\python\文件命名\未创建的文件夹-如果看见请删掉"

#os.makedirs()是一个函数，用于创建目录
#如果目录已经存在，那么这段代码不会抛出异常，也不会对目录做任何操作
#如果目录不存在，那么这段代码会创建该目录及其所有父级目录。
#exist_ok=True是一个关键字参数，表示如果目标目录已经存在，是否抛出异常
#如果exist_ok为True，则不会抛出异常，如果目标目录已经存在，则什么都不做；如果exist_ok为False，则会抛出FileExistsError异常。
os.makedirs(target_folder, exist_ok=False)
