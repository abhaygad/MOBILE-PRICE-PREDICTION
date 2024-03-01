from sklearn.neighbors import NearestNeighbors
import numpy as np


def recommend(n_neighbor,x,a):
    nd = NearestNeighbors(n_neighbors=n_neighbor)
    nd.fit(x)
    distances, indices = nd.kneighbors(a)

    return indices
def recommend_output(data,indices_new,end) :
    output_list = np.empty((end, 0), str)
    for i in range(len(indices_new[0])):
        output_list=np.append(output_list, data[0][int(indices_new[0][i])], axis=None)


    return output_list








