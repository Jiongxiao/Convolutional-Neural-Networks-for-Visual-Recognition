import copy
for k in k_choices:
    k_to_accuracies[k]=[]
    for i in range(num_folds):
    	X_folds=copy.deepcopy(X_train_folds)
    	y_folds=copy.deepcopy(y_train_folds)
    	X_ith_test=X_folds.pop(i)
    	y_ith_test=y_folds.pop(i)
    	X_ith_train=np.vstack(X_folds)
    	y_ith_train=np.vstack(y_folds)
    	classifier_k=KNearestNeighbor()
    	classifier_k.train(X_ith_train,y_ith_train)
    	distances=classifier_k.compute_distances_no_loops(X_ith_test)
    	y_ith_test_pred=classifier_k.predict_labels(distances,k)
    	num_ith_correct=np.sum(y_ith_test_pred==y_ith_test)
    	accuracy_ith=float(num_ith_correct)/len(y_ith_test)
    	k_to_accuracies[k].append(accuracy_ith)