# -*- coding: utf-8 -*-
# @File  : text_similarity.py
# @Author: redtree
# @Date  : 18-6-27
# @Desc  : 字符串相似度匹配算法工具包

import difflib
from nltk.util import ngrams
from urllib.parse import unquote


#difflib的算法，类余弦相似度匹配算法
def difflib_rank(strA,strB):
    strB = unquote(strB, 'utf-8')
    for rsp in ['\n', ' ', '。','+']:
        strA=  str(strA).replace(rsp,'')
        strB=  str(strB).replace(rsp,'')
    seq = difflib.SequenceMatcher(None, str(strA), str(strB))
    ratio = seq.ratio()
    return float(ratio)

#基于nGram算法匹配字符串相似度
def nGram_rank(strA,strB,N_value=2):
    nGram_A = list(ngrams(strA,N_value))
    nGram_B = list(ngrams(strB,N_value))
    LEN_A = len(nGram_A)
    LEN_B = len(nGram_B)
    MATCHS = 0
    for n_A in nGram_A:
        if n_A in nGram_B:
            nGram_B.remove(n_A)
            MATCHS=MATCHS+1

    rank = LEN_A+LEN_B-2*MATCHS
    return rank
