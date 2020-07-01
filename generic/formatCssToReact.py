# -*-coding: UTF-8 -*-

'''
zzq
格式css 转成react认的css
'''

if __name__ == '__main__':
    #data = "width: 100%;display: block;margin-top: 18px;"
    #data = input("请输入css...")
    data = ''
    file = open("css.txt", 'r', encoding='utf-8')
    data = file.read().strip();
    file.close()
    data_arr = data.split(";")
    for item in data_arr:
        if item:
            item_arr = item.split(":")
            if item_arr and len(item_arr) > 1:
                key = item_arr[0];
                key_index = key.find("-");
                if key_index > 0:
                    key_arr = key.split("-")
                    key = key_arr[0] + key_arr[1].capitalize()
                elif item_arr and key_index == 0:
                    key = key[1:len(key)]
                print(key.strip() + ": " + "'" + item_arr[1].strip() + "',")
