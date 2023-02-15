#--*-- coding:utf-8 --*--
import re


def getbanwords():
    f = open('banwords.txt', mode='r',encoding='utf-8')
    lines = f.readlines()
    txtdata = []
    for line in lines:
        line = line.strip('\n')
        txtdata.append(line)
    return txtdata


def has_banwords(text):#判断是否存在禁词
    banwords = getbanwords()
    words = []
    for word in banwords:
        if word in text:
            words.append(word)
    return words


    # def replace_banword(banwords, text):
    #     for word in banwords:
    #         if word in text:
    #             text = text.replace(word, '*' * len(word.decode('utf-8')))
    #     return text
    #
    # def nobantext(text):
    #     return replace_banword(has_banwords(text), text)

if __name__ == "__main__":
    print(has_banwords(text="嫖娼成人联盟被抓"))
