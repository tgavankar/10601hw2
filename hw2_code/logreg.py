from __future__ import divisionimport csvimport operatorimport mathimport timedef print_timing(func):    def wrapper(*arg):        t1 = time.time()        res = func(*arg)        t2 = time.time()        print '%s took %0.3f ms' % (func.func_name, (t2-t1)*1000.0)        return res    return wrapperdef sigmoid(z):    return 1 / (1 + math.exp(-z))    def dotp(v1, v2):    return sum(map(operator.mul, v1, v2))    class LogisticRegression():    def __init__(self, step=0.001):        self.docs = []        self.v = step        self.text = []        self.sVoc = 0            @print_timing    def train(self, custname=""):        word_indices = [line.strip() for line in open("data/word_indices" + custname + ".txt")]        train_labels = [line.strip() for line in open("data/train_labels.txt")]        training_docs = []        train_pos = 0        with open("data/train" + custname + ".csv") as csvfile:            training = csv.reader(csvfile)            for row in training:                training_docs.append({                'label': int(train_labels[train_pos]),                'data': [int(e) for e in row]})                train_pos += 1        print "finished reading"        self.sVoc = len(word_indices)        minAllStep = float("inf")                while minAllStep > 0.01:            for doc in training_docs:                print "doc"                origTheta = doc['data']                maxStep = 0                for j in xrange(len(doc['data'])):                    step = self.v * (doc['label'] - dotp(origTheta, origTheta) * doc['data'][j])                    doc['data'][j] = doc['data'][j] + step                    if step > maxStep:                        maxStep = step                if maxStep < minAllStep:                    minAllStep = maxStep            print minAllStep        import pdb; pdb.set_trace()        if __name__ == "__main__":                          lr = LogisticRegression()    lr.train()