import bm25, os
easyWay = os.path.dirname(os.path.realpath(__file__))

"""
5 local documents, query = One document ranking
"""
tempPathDoc = tuple(easyWay + '/doc' + str(i) + '.txt' for i in range(1, 6))
docTest = bm25.BM25(paths = tempPathDoc)
docResult = docTest.bm25_algorithm("One document ranking")
print(docResult)

"""
3 urls, query = mathematics
"""
"""urlsPath = ["https://en.wikipedia.org/wiki/Isaac_Newton", "https://en.wikipedia.org/wiki/Gottfried_Wilhelm_Leibniz", 
"https://en.wikipedia.org/wiki/Johann_Sebastian_Bach"]
urlTest = bm25.BM25(urls = urlsPath)
urlResult = urlTest.bm25_algorithm("mathematics")
print(urlResult)"""