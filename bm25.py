import os, re, math
import getUrlText

class BM25:
	def __init__(self, *a, docs = [], paths = [], urls = []):
		"""
		Initialize class in three ways:
		1) docs - a list of str documents
		2) paths - a list of documents paths
		3) urls - a list of urls
		"""
		if docs:
			self.docs = docs
		elif paths:
			docs = []
			for docPath in paths:
				curDoc = open(docPath, "r")
				docs.append(curDoc.read())
				curDoc.close()
			self.docs = docs
		elif urls:
			docs = []
			for oneUrl in urls:
				docs.append(getUrlText.get_url_text(oneUrl))
			self.docs = docs
		else:
			raise Exception("Can't get data!")
	
	def get_needed_inf(self, query):
		"""
		Returns needed information about "docs and queries"
		"""
		docsInfo = []
		queryFin = [x for x in re.split('\W+', query.lower()) if x]
		for document in self.docs:
			curDocText = re.split('\W+', document.lower())
			docsInfo.append({'len': len(curDocText), 'meetCnt': []})
			for queryWord in queryFin:
				docsInfo[-1]['meetCnt'].append(curDocText.count(queryWord))
		# print(docsInfo)
		return docsInfo
	
	def count_IDF(self, N, n):
		return max(math.log((N - n + 0.5) / (n + 0.5)), 0.0000001)

	def count_main_fraction(self, TF, k1, b, avgdl, docLen):
		return TF * (k1 + 1) / (TF + k1 * (1 - b + b * docLen / float(avgdl)))

	def count_score(self, docsInfo, avgdl, k1, b):
		"""
		Counting bm25 score of the document
		"""
		docScore = []
		for doc in docsInfo:
			curDocScore = 0
			for queryWord in range(len(doc['meetCnt'])):
				TF = float(doc['meetCnt'][queryWord])
				freaq = sum(1 for x in docsInfo if x['meetCnt'][queryWord])
				curDocScore += self.count_IDF(len(docsInfo), freaq) * self.count_main_fraction(TF, k1, b, avgdl, doc['len'])
			docScore.append(curDocScore)
		return docScore

	def bm25_algorithm(self, query, k1 = 2.0, b = 0.75):
		"""
		Counting scores by bm25 algorithm for string query, returns list of scores
		"""
		docsInfo = self.get_needed_inf(query)
		avgdl = sum(x['len'] for x in docsInfo) / float(len(docsInfo))
		# print(docsInfo)
		docScore = self.count_score(docsInfo, avgdl, k1, b)
		return docScore

if __name__ == "__main__":
	easyWay = os.path.dirname(os.path.realpath(__file__))
	tempPathDoc = (easyWay + "/doc1.txt", easyWay + "/doc2.txt", easyWay + "/doc3.txt", easyWay + "/doc4.txt", easyWay + "/doc5.txt")
	docTest = BM25(paths = tempPathDoc)
	docTest.bm25_algorithm("One document ranking")
	# print(os.getcwd())
