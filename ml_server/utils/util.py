from typing import List
from keras.preprocessing.text import Tokenizer


def getArray(path: str) -> List[List[str]]:
    articleList = []
    with open(path) as textFile:
        tempList: List[str] = textFile.readlines()
        for article in tempList:
            articleList.append(article.split())

    return articleList


def WordtoInt(arr: List[List[str]],):
    t = Tokenizer(num_words=500)
    t.fit_on_texts(arr)
    sequences = t.texts_to_sequences(arr)
    print('sequences : ', sequences, '\n')
    print('word_index : ', t.word_index)
    tokenizer_json = t.to_json()
    print(tokenizer_json)


if __name__ == "__main__":
    arr = getArray("file.txt")
    print(arr)
    WordtoInt(arr)
