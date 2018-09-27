#!/usr/bin/python
# -*- coding: utf-8 -*-

import os
import sys
import oss2

if 3 != len(sys.argv):
    print('[Usage] %s [dir_set] [filepath]' % os.path.basename(sys.argv[0]))
    sys.exit(0)
else:
    # dir_set 的格式为 image/ ，注意末尾带反斜杠/
    dir_set = sys.argv[1]
    file_path = sys.argv[2]

accessKeyId = ''

accessKeySecret = ''
# 空间名
bucketName = ''
# Endpoint所在地
region = 'http://oss-cn-shenzhen.aliyuncs.com'
# 访问域名
domainName = ''
# 图片样式
styleCode = "?image/auto-orient,1/quality,q_90/watermark,text_WmFja-ivtOeggQ,type_d3F5LW1pY3JvaGVp,size_20,t_60,color_ffffff,g_se,y_10,x_10"

auth = oss2.Auth(accessKeyId,accessKeySecret)

bucket = oss2.Bucket(auth, region, bucketName)

def upload(input_path):
    #upload single file to qiniu
    filename = os.path.basename(input_path)
    key = '%s%s' % (dir_set, filename)


    bucket.put_object_from_file(key, input_path)

    print('%s done' % (domainName + dir_set + filename + styleCode))

def upload_all_files(input_path):
    if os.path.isfile(input_path):
        upload(input_path)
    elif os.path.isdir(input_path):
        dirlist = os.walk(input_path)
        for root, dirs, files in dirlist:
            for filename in files:
                upload(os.path.join(root, filename))
    else:
        print('Please input the exists file path!')

if __name__ == "__main__":
    upload_all_files(file_path)
