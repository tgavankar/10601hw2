# Tanay Gavankar# tgavanka# HW2 Question 4# Naive Bayesfrom __future__ import divisionimport csvimport mathimport randomimport timedef print_timing(func):    def wrapper(*arg):        t1 = time.time()        res = func(*arg)        t2 = time.time()        print '%s took %0.3f ms' % (func.func_name, (t2-t1)*1000.0)        return res    return wrapperclass NaiveBayes():    def __init__(self):        self.docs = []        self.P = []        self.text = []        self.sVoc = 0    @print_timing    def train(self, custname="", subset=None):        word_indices = [line.strip() for line in open("data/word_indices" + custname + ".txt")]        train_labels = [line.strip() for line in open("data/train_labels.txt")]        training_docs = []        train_pos = 0        with open("data/train" + custname + ".csv") as csvfile:            training = csv.reader(csvfile)            for row in training:                training_docs.append({                'label': int(train_labels[train_pos]),                'data': [int(e) for e in row]})                train_pos += 1                    self.sVoc = len(word_indices)        sVoc = self.sVoc        if subset is not None:            training_docs = random.sample(training_docs, subset)                for j in xrange(2):            self.docs.append([item for item in training_docs if item['label'] == j])            self.text.append(reduce(lambda x,y: {'data': [int(x['data'][i]) + int(y['data'][i]) for i in xrange(sVoc)]}, self.docs[j], {'data': [0]*sVoc}))            n = sum(self.text[j]['data'])                        self.P.append({'v': len(self.docs[j]) / len(training_docs),                            'wgv': [(self.text[j]['data'][k] + 1) / (n + sVoc) for k in xrange(sVoc)]})    @print_timing    def classify(self, name="test"):        test_labels = [line.strip() for line in open("data/" + name + "_labels.txt")]                test_docs = []        test_pos = 0                with open("data/" + name + ".csv") as csvfile:            test = csv.reader(csvfile)            for row in test:                test_docs.append({                    'label': int(test_labels[test_pos]),                    'data': [int(e) for e in row]})                test_pos += 1        for doc in test_docs:            vnbl = []            for j in xrange(2):                vnbl.append(math.log(self.P[j]['v']) + sum([math.log(self.P[j]['wgv'][i]) * (int(doc['data'][i])) for i in xrange(self.sVoc)]))            doc['vnbl'] = vnbl            doc['pred_label'] = vnbl.index(max(vnbl))                           actual = [x['label'] for x in test_docs]        pred = [x['pred_label'] for x in test_docs]                res = [(0, 1)[a[0] == a[1]] for a in zip(actual, pred)]        print sum(res) / len(res)if __name__ == "__main__":    for i in xrange(90):        nb = NaiveBayes()        nb.train("_feat100", i*50+20)        nb.classify("train_feat100")        nb.classify("test_feat100")