import numpy as np 
from multiprocessing import Pool

def unpickle(file):
    import cPickle
    fo = open(file, 'rb')
    dict = cPickle.load(fo)
    fo.close()
    return dict

dic=unpickle('data_batch_1')

def load_CIFAR10():
	pic=[0]*6
	label=[0]*6
	for i in range(1,6):
		filename='data_batch_%d' %i
		dic=unpickle(filename)
		pic[i]=dic['data']
		label[i]=dic['labels']

	Xtr=np.vstack((pic[1],pic[2],pic[3],pic[4],pic[5]))
	Ytr=np.hstack((label[1],label[2],label[3],label[4],label[5]))

	filename='test_batch'
	test=unpickle(filename)
	Xte=test['data']
	Yte=test['labels']
	return Xtr,Ytr,Xte,np.array(Yte)
Xtr, Ytr, Xte, Yte = load_CIFAR10()
# print Xtr.shape,Ytr.shape,Xte.shape,Yte.shape

def long_time_task(train_X,train_y,X,i,Ypred):#没用了
	print 'he'
	distances=np.sum(np.abs(train_X-X[i,:]),axis=1)
	min_index=np.argmin(distances)
	Ypred[i]=train_y[min_index]
	print Ypred[i]

class NearestNeighbor(object):
	def __init__(self):
		pass

	def train(self,X,y):
		self.Xtr=X
		self.ytr=y

	# 基本方法
	def predict(self,X):
		num_test=X.shape[0]
		Ypred=np.zeros(num_test)

		for i in xrange(num_test):
			distances=np.sum(np.abs(self.Xtr-X[i,:]),axis=1)
			min_index=np.argmin(distances)
			Ypred[i]=self.ytr[min_index]

		return Ypred

	# def predict(self,X):
	# 	num_test=X.shape[0]
	# 	# Ypred=np.zeros(num_test)
	# 	Ypred=map(self.getDistance,[[i,X] for i in range(num_test)])
	# 	return Ypred

	# def getDistance(self,args):
	# 	distances=np.sum(np.abs(self.Xtr-args[1][args[0],:]),axis=1)
	# 	min_index=np.argmin(distances)
	# 	Ypred=self.ytr[min_index]
	# 	return Ypred


    #####################试试多进程####### 尼玛！！！进程间数据传递好特么复杂~~TAT
	# def predict(self,X):
	# 	num_test=X.shape[0]
	# 	Ypred=np.zeros(num_test)
	# 	p=Pool()
	# 	for i in range(num_test):
	# 		p.apply_async(long_time_task,(self.Xtr,self.ytr,X,i,Ypred,))
	# 	p.close()
	# 	p.join()
	# 	return Ypred

nn=NearestNeighbor()
nn.train(Xtr[0:100,:],Ytr[0:100])
Yte_predict=nn.predict(Xte[0:100,:])
print 'accuracy: %f' % (np.mean(Yte[0:100]==Yte_predict))
# nn=NearestNeighbor()
# nn.train(Xtr,Ytr)
# Yte_predict=nn.predict(Xte)
# print 'accuracy: %f' % (np.mean(Yte==Yte_predict))


