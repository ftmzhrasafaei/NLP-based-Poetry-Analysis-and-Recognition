import copy

def SingleWordDictionary(url ,lim = 0):
    f = open(url, 'r',encoding='utf-8')
    lines = f.readlines()
    f.close()
    wordfreq = {}
    for line in lines:
        s = line.split()
        for w in s:
            if w not in wordfreq.keys():
                wordfreq[w] = 1
            else:
                wordfreq[w] += 1
    if lim > 0:
        another = copy.deepcopy(wordfreq)
        for k in another:
            if wordfreq[k] < lim :
                wordfreq.pop(k)

    return wordfreq


def TwoWordDictionary(url):
    f = open(url, 'r',encoding='utf-8')
    lines = f.readlines()
    f.close()
    wordtwo = {}
    for line in lines:
        s = line.split()
        for i in range(len(s)-1):
            if (s[i] + ' ' + s[i+1]) not in wordtwo.keys():
                wordtwo[s[i] + ' ' + s[i+1]] = 1
            else:
                wordtwo[s[i] + ' ' + s[i+1]] += 1
    return wordtwo

def Unigram(onedict):
    udict = copy.deepcopy(onedict)
    for k in onedict:
        udict[k] = onedict[k]/len(onedict)
    return udict

def Bigram(onedict , twodict):
    Bdict = copy.deepcopy(twodict)
    for k in twodict:
        w = k.split()
        Bdict[k] = twodict[k] / onedict[w[0]]
    return Bdict

def Hemistich(sent):
    h = []
    s = sent.split()
    for i in range(len(s)-1):
        h.append(s[i] + ' ' + s[i+1])
    return h

def ListMultiply(L):
    m = L[0]
    for i in range(len(L)-1):
        m = L[i + 1] * m
    return m


class Poet:
    def __init__(self ,EnglishName ,PersianName , url, diclim = 0):
        self.Ename = EnglishName
        self.Pname = PersianName
        self.url = url
        self.diclim = diclim
        self.sdict = SingleWordDictionary(url , diclim)
        self.bdict = TwoWordDictionary(url)
        self.unigram = Unigram(self.sdict)
        self.bigram = Bigram(self.sdict , self.bdict)
    def EnglishName(self):
        return self.Ename
    def PersianName(self):
        return self.Pname

    def Model(self , lambda1 , lambda2 , epsilone , sentence):
        sent = Hemistich(sentence)
        p1 = self.unigram
        p2 = self.bigram
        phat = [0 for i in range(len(sent))]
        u = 0
        b = 0
        ind = 0
        for k in sent:
            w = k.split()
            if w[0] in p1 :
                u  = p1[w[0]]
            if k in p2:
                b = p2[k]
            phat[ind] =  lambda1 * b + lambda2 * u + (1 - lambda1 - lambda2) * epsilone
            ind = ind + 1

        return ListMultiply(phat)


def WhichPoet(poets , sent, lam1 , lam2 , eps):
    prob = [0 for i in range(len(poets))]
    for i in range(len(poets)):
        prob[i] = poets[i].Model(lam1 , lam2 , eps ,sent)
    return poets[prob.index(max(prob))]
def PrintResualt(s , p):
    taaloq = 'متعلق به'
    ast = 'حدس زده شده است'
    print(s , '  ' , taaloq , p.PersianName() , ast)



def Test(poets ,lam1 , lam2 , eps , url , realpoet ,wprint = 0):
    f = open(url, 'r',encoding='utf-8')
    lines = f.readlines()
    f.close()

    correct = 0
    r  = 'این مصراع در واقع متعلق به'
    ast = 'است'
    for line in lines:
        p = WhichPoet(poets , line[2:len(line)-1], lam1 , lam2 , eps)
        if wprint == 0 :
            PrintResualt(line[2:len(line)-1] , p)
            print(r , realpoet[line[0]] , ast)
            print('=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=')

        if p.PersianName() == realpoet[line[0]] :
            correct = correct + 1

    return correct/len(lines)


p1 = Poet('ferdowsi' , 'فردوسی' , 'train_set/ferdowsi_train.txt')
p2 = Poet('Hafez' , 'حافظ' , 'train_set/hafez_train.txt')
p3 = Poet('Molavi' , 'مولوی' , 'train_set/molavi_train.txt')

realpoet = {
    '1': 'فردوسی',
    '2':'حافظ',
    '3':'مولوی'
}
url = 'test_set/test_file.txt'
#print('If you want to see result of test , Enter 1 Please , Otherwise Enter 0 Please  ')
#pr = int(input())


print(' Result of Test1 : lambda3 = 0.6 , lambda2 = 0.2 , Epsilon = 0.1 ')
print('If you want to see result of test , Enter 1 Please , Otherwise Enter 0 Please  ')
pr = 1 - int(input())
t1 = Test([p1 , p2 , p3] , 0.6 , 0.2 , 0.1 , url , realpoet , pr)
print('Precsion : ' , t1)
print('\n')

print(' Result of Test2: lambda3 = 0.6 , lambda2 = 0.2 , Epsilon = 0.7 ')
print('If you want to see result of test , Enter 1 Please , Otherwise Enter 0 Please  ')
pr = 1- int(input())
t2 = Test([p1 , p2 , p3] , 0.6 , 0.2 , 0.5 , url , realpoet , pr)
print('Precsion : ' , t2)
print('\n')

print(' Result of Test3: lambda3 = 0.95 , lambda2 = 0.005 , Epsilon = 0.1 ')
print('If you want to see result of test , Enter 1 Please , Otherwise Enter 0 Please  ')
pr = 1 -int(input())
t3 = Test([p1 , p2 , p3] , 0.95 , 0.005 , 0.1 , url , realpoet , pr)
print('Precsion : ' , t3)
print('\n')

print(' Result of Test4: lambda3 = 0.95 , lambda2 = 0.005 , Epsilon = 0.7 ')
print('If you want to see result of test , Enter 1 Please , Otherwise Enter 0 Please  ')
pr = 1- int(input())
t4 = Test([p1 , p2 , p3] , 0.95 , 0.005, 0.7 , url , realpoet , pr)
print('Precsion : ' , t4)
print('\n')
