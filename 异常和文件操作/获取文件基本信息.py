# 用os模块输出文件的基本信息
import os
def foarmatTime(longtime):
    import time
    return time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(longtime))

def formatByte(number):
    for (scale,label) in [(1024*1024*1024,'GB'),(1024*1024,'MB'),(1024,'KB')]:
        if number >= scale: # 文件大于大于小于或等于1KB
            return "%.2f %s" %(number*1.0/scale,label)
        elif number == 1: # 如果文件大小为1字节
            return "1字节"
        else: # 处理小于1kb的情况
            byte = "%.2f" %(number or 0)

    return (byte[:-3] if byte.endswith('.00') else byte)+"字节"

if __name__== "__main__":
    fileinfo = os.stat('mr.png')  # 获取文件的基本信息
    print('完整路径:',os.path.abspath('mr1.png'))
    print('索引号：',fileinfo.st_ino)
    print('设备号：', fileinfo.st_dev)
    print('文件大小：', formatByte(fileinfo.st_size))
    print('最后一次访问时间：', formatByte(fileinfo.st_atime))
    print('最后一次修改时间：',formatByte(fileinfo.st_mtime))
    print('最后一次状态修改变化时间：', formatByte(fileinfo.st_ctime))