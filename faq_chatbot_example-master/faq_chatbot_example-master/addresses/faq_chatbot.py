from gensim.models import doc2vec, Doc2Vec
from gensim.models.doc2vec import TaggedDocument
import pandas as pd
from nltk.tokenize import word_tokenize
from nltk.stem import WordNetLemmatizer
from nltk.corpus import stopwords
import nltk
#형태소 분석
import jpype
from konlpy.tag import Kkma

# 파일로부터 모델을 읽는다. 없으면 생성한다.
d2v_faqs = Doc2Vec.load('d2v_faqs.model')
faqs = pd.read_csv('faq.csv')

kkma = Kkma()
filter_kkma = ['NNG',  #보통명사
             'NNP',  #고유명사
             'OL' ,  #외국어
            ]

def tokenize_kkma(doc):
    jpype.attachThreadToJVM()
    token_doc = ['/'.join(word) for word in kkma.pos(doc)]
    return token_doc

def tokenize_kkma_noun(doc):
    jpype.attachThreadToJVM()
    token_doc = ['/'.join(word) for word in kkma.pos(doc) if word[1] in filter_kkma]
    return token_doc


# FAQ 답변
def faq_answer(input):
    # 테스트하는 문장도 같은 전처리를 해준다.
    tokened_test_string = tokenize_kkma_noun(input)
    print('인풋!!' + str(tokened_test_string))
    topn = 10
    test_vector = d2v_faqs.infer_vector(tokened_test_string)
    result = d2v_faqs.docvecs.most_similar([test_vector], topn=topn)
    answer_list = []

    # for i in range(topn):
    #     print("{}위. {}, {} {} {}".format(i + 1, result[i][1], result[i][0], faqs['질문'][result[i][0]], faqs['답변'][result[i][0]]))
    #     answer_list.append(dict(acc=result[i][1], question=faqs['질문'][result[i][0]], answer=faqs['답변'][result[i][0]]))
    #
    return dict(acc1=result[0][1], question1=faqs['질문'][result[0][0]],answer1=faqs['답변'][result[0][0]],
                acc2=result[1][1], question2=faqs['질문'][result[1][0]],answer2=faqs['답변'][result[1][0]],
                acc3=result[2][1], question3=faqs['질문'][result[2][0]],answer3=faqs['답변'][result[2][0]],
                acc4=result[3][1], question4=faqs['질문'][result[3][0]],answer4=faqs['답변'][result[3][0]],
                acc5=result[4][1], question5=faqs['질문'][result[4][0]],answer5=faqs['답변'][result[4][0]],
                acc6=result[5][1], question6=faqs['질문'][result[5][0]],answer6=faqs['답변'][result[5][0]],
                acc7=result[6][1], question7=faqs['질문'][result[6][0]],answer7=faqs['답변'][result[6][0]],
                acc8=result[7][1], question8=faqs['질문'][result[7][0]],answer8=faqs['답변'][result[7][0]],
                acc9=result[8][1], question9=faqs['질문'][result[8][0]],answer9=faqs['답변'][result[8][0]],
                acc10=result[9][1], question10=faqs['질문'][result[9][0]],answer10=faqs['답변'][result[9][0]])


def faq_search(inputs):
    keywords = None
    for word in inputs:
        if keywords is None:
            keywords = word
        else:
            keywords = keywords + '|' + word
    faqs[faqs.str.contains(keywords)]
    print(faqs)
    return 0