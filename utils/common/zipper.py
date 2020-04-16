# -*- coding: utf-8 -*-
# @ Time   :  2020/2/25 15:37
# @ Author : Redtree
# @ File :  zipper 
# @ Desc :  基于python-zipfile 模块的文件管理工具


import zipfile  # 引入zip管理模块
import os


def package_zip(dir_path,zip_path):
    """
    压缩指定文件夹
    :param dir_path: 目标文件夹路径
    :param zip_path: 压缩文件保存路径+xxxx.zip
    :return: 无
    """

    try:
        zip = zipfile.ZipFile(zip_path, "w", zipfile.ZIP_DEFLATED)
        for path, dirnames, filenames in os.walk(dir_path):
            # 去掉目标跟路径，只对目标文件夹下边的文件及文件夹进行压缩
            fpath = path.replace(dir_path, '')

            for filename in filenames:
                zip.write(os.path.join(path, filename), os.path.join(fpath, filename))
        zip.close()
        return True
    except:
        return False


def unzip(zip_path,dir_path,password):
    if password:
        password = password.encode()
    zf = zipfile.ZipFile(zip_path)
    try:
        zf.extractall(path=dir_path,pwd=password)
    except Exception as err:
        print(err)
    zf.close()

# dirpath = "../upload/dicom_ae/ID-1"
# outFullName = "ID-1.zip"

#unzip('../../upload/dcmzip/14070904.zip','../../upload/dicom_ae',None)