import base64
#image转base64
def base (filename):
    with open(filename, "rb") as f:  # 转为二进制格式
     base64_data = base64.b64encode(f.read())  # 使用base64进行加密
     print(base64_data)
     file_handle = open('tot.txt', mode='wb+')  # 写成文本格式
     file_handle.write(base64_data)
     file_handle.close()



#base64转image
def basetwo(filename):
    with open(filename,"r") as f:
     imgdata = base64.b64decode(f.read())
     file_handle = open('top.jpg', 'wb')
     file_handle.write(imgdata)
     file_handle.close()

if __name__ == '__main__':
    base('a.jpg')
    basetwo('tot.txt')


