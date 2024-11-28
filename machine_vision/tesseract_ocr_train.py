# -*- coding: utf-8 -*-

import os

'''

tesseract_ocr_train 训练
'''


def invocation_command(cmd: str):
    print("执行命令 ", cmd)
    os.system(cmd)


if __name__ == '__main__':
    print("请先确认配置好执行Tesseract-OCR命令环境变量和TESSDATA_PREFIX环境变量，默认会读取addr.test.exp0.tif")
    # tif文面命名格式[lang].[fontname].exp[num].tif
    lang = "addr"
    font_name = "test"
    num = "0"

    lang_tmp = input("请输入lang,默认addr ")
    if lang_tmp:
        lang = lang_tmp

    font_name_tmp = input("请输入fontname 默认test")
    if font_name_tmp:
        font_name = font_name_tmp

    num_tmp = input("请输入num，默认0 ")
    if num_tmp:
        num = num_tmp


    tif_name = lang + "." + font_name + ".exp" + num + ".tif"
    name = lang + "." + font_name + ".exp" + num

    print("tif_name ",tif_name)
    input("1、按任意键继续，会生成.box文件")
    cmd = "tesseract " + tif_name + " " + name + " -l chi_sim --psm 6 batch.nochop makebox"
    invocation_command(cmd)
    input("请用jTessBoxEditor打开文件，矫正并保存后按任意键继续")

    print("2、生成font_properties文件")
    invocation_command("echo " + font_name + " 0 0 0 0 0 >font_properties")

    print("3、生成.tr训练文件")
    invocation_command("tesseract " + tif_name + " " + name + " nobatch box.train")

    print("4、生成字符集文件")
    invocation_command("unicharset_extractor " + name + ".box")

    print("5、生成shape文件 ")
    invocation_command("shapeclustering -F font_properties -U unicharset -O " + lang + ".unicharset " + name + ".tr")

    print("6、生成聚字符特征文件")
    invocation_command("mftraining -F font_properties -U unicharset -O " + lang + ".unicharset " + name + ".tr")

    print("7、生成字符正常化特征文件")
    invocation_command("cntraining " + name + ".tr")

    print("8、文件重命名")
    file_list = ["inttemp","pffmtable","shapetable","normproto"]
    for file in file_list:
        if os.path.exists(file):
            rename_file = lang+"."+file
            if os.path.exists(rename_file):
                os.remove(rename_file)
            print("rename ",file +" " + rename_file)
            os.rename(file,rename_file)


    print("9、合并训练文件")
    invocation_command("combine_tessdata "+lang+".")