import copy
from random import randint
from statistics import mode
import string
import matplotlib.pyplot as plt
import numpy


LABEL_COL = 1
ROWS = 10000
DATA_COL = 784


def find_centriods_randomly(k, data):
    # has the full centriod vectors
    centriods = []
    # is a list of k lists with all of the vector index in their
    # corresponding cluster. This vector index can be plugged into
    # the data list to get the full vector with all of its components
    centriod_clusters = []
    previous_centriods = []
    # random centriods
    for i in range(k):
        random_val = randint(0, ROWS-1)
        centriods.append(numpy.ndarray.copy(data[random_val]))
        previous_centriods.append(numpy.ndarray.copy(data[random_val]))
    num_iterations = 0
    converges = False
    while(not converges):
        num_iterations += 1
        centriod_clusters.clear()
        for i in range(k):
            centriod_clusters.append([])
        # appoints vectors to closest centriods
        for i in range(ROWS):
            distance = float('inf')
            cluster_index = 0
            for j in range(k):
                euc_dist = numpy.linalg.norm(centriods[j] - data[i])
                if euc_dist < distance:
                    distance = euc_dist
                    cluster_index = j
            centriod_clusters[cluster_index].append(i)
        # for each centriod
        for i in range(k):
            # for each component of a vector
            for j in range(DATA_COL):
                avg = 0.0
                # for each vector in centriod cluster
                for vector_index in centriod_clusters[i]:
                    #  j=component index
                    avg += data[vector_index][j]
                # divides by num elements summed if the number of elements is greater than 0
                if (len(centriod_clusters[i]) > 0):
                    avg /= len(centriod_clusters[i])
                # appoints new centriod component to avg
                centriods[i][j] = avg
        # checks if the previous centriod was the same as this one, if it is, stops the loop
        if num_iterations > 1 and compare_lists(previous_centriods, centriods):
            converges = True
            # copies the current set of centriods to the previous_centriods list if there is not yet convergence
        else:
            for i in range(k):
                for j in range(DATA_COL):
                    previous_centriods[i][j] = centriods[i][j]
    # returns the number of iterations that this took and the clusters generated
    return num_iterations, centriod_clusters


def find_centriods_randomly_with_labels(k, data, labels):
    # has the full centriod vectors
    centriods = []
    # is a list of k lists with all of the vector index in their
    # corresponding cluster. This vector index can be plugged into
    # the data list to get the full vector with all of its components
    centriod_clusters = []
    previous_centriods = []
    # random centriods
    for i in range(k):
        random_val = randint(0, ROWS-1)
        while(labels[random_val] != i):
            random_val = randint(0, ROWS-1)
        centriods.append(numpy.ndarray.copy(data[random_val]))
        previous_centriods.append(numpy.ndarray.copy(data[random_val]))
    num_iterations = 0
    converges = False
    while(not converges):
        num_iterations += 1
        centriod_clusters.clear()
        for i in range(k):
            centriod_clusters.append([])
        # appoints vectors to closest centriods
        for i in range(ROWS):
            distance = float('inf')
            cluster_index = 0
            for j in range(k):
                euc_dist = numpy.linalg.norm(centriods[j] - data[i])
                if euc_dist < distance:
                    distance = euc_dist
                    cluster_index = j
            centriod_clusters[cluster_index].append(i)
        # for each centriod
        for i in range(k):
            # for each component of a vector
            for j in range(DATA_COL):
                avg = 0.0
                # for each vector in centriod cluster
                for vector_index in centriod_clusters[i]:
                    #  j=component index
                    avg += data[vector_index][j]
                # divides by num elements summed if the number of elements is greater than 0
                if (len(centriod_clusters[i]) > 0):
                    avg /= len(centriod_clusters[i])
                # appoints new centriod component to avg
                centriods[i][j] = avg
        # checks if the previous centriod was the same as this one, if it is, stops the loop
        if num_iterations > 1 and compare_lists(previous_centriods, centriods):
            converges = True
            # copies the current set of centriods to the previous_centriods list if there is not yet convergence
        else:
            for i in range(k):
                for j in range(DATA_COL):
                    previous_centriods[i][j] = centriods[i][j]
    # returns the number of iterations that this took and the clusters generated
    return num_iterations, centriod_clusters


def find_and_print_centriods(k, data):
    # shows the images of all of the centriods for one run
    # has the full centriod vectors
    centriods = []
    # is a list of k lists with all of the vector index in their
    # corresponding cluster. This vector index can be plugged into
    # the data list to get the full vector with all of its components
    centriod_clusters = []
    previous_centriods = []
    # random centriods
    for i in range(k):
        random_val = randint(0, ROWS-1)
        centriods.append(numpy.ndarray.copy(data[random_val]))
        previous_centriods.append(numpy.ndarray.copy(data[random_val]))
    num_iterations = 0
    converges = False
    while(not converges):
        num_iterations += 1
        centriod_clusters.clear()
        for i in range(k):
            centriod_clusters.append([])
        # appoints vectors to closest centriods
        for i in range(ROWS):
            distance = float('inf')
            cluster_index = 0
            for j in range(k):
                euc_dist = numpy.linalg.norm(centriods[j] - data[i])
                if euc_dist < distance:
                    distance = euc_dist
                    cluster_index = j
            centriod_clusters[cluster_index].append(i)
        # for each centriod
        for i in range(k):
            # for each component of a vector
            for j in range(DATA_COL):
                avg = 0.0
                # for each vector in centriod cluster
                for vector_index in centriod_clusters[i]:
                    #  j=component index
                    avg += data[vector_index][j]
                # divides by num elements summed if the number of elements is greater than 0
                if (len(centriod_clusters[i]) > 0):
                    avg /= len(centriod_clusters[i])
                # appoints new centriod component to avg
                centriods[i][j] = avg
        # checks if the previous centriod was the same as this one, if it is, stops the loop
        if num_iterations > 1 and compare_lists(previous_centriods, centriods):
            converges = True
            # copies the current set of centriods to the previous_centriods list if there is not yet convergence
        else:
            for i in range(k):
                for j in range(DATA_COL):
                    previous_centriods[i][j] = centriods[i][j]
    # returns the number of iterations that this took and the clusters generated
    for i in range(k):
        img = (numpy.reshape(centriods[i], (28, 28))).astype(numpy.uint8)
        plt.imshow(img, interpolation='nearest')
        plt.show()


def most_common_digit(cluster, labels):
    # finds the most common digit in a cluster
    digit = []
    for i in cluster:
        digit.append(labels[i])
    return mode(digit)


def different_from_digit(digit, cluster, labels):
    # count the number of instances in the cluster that are
    # different from the most common one
    total = 0
    for i in cluster:
        if labels[i] != digit:
            total += 1
    return total


def compare_lists(list1, list2):
    # compares two lists and returns true it they have the same values, false otherwise
    if len(list1) != len(list2):
        return False
    for i in range(len(list1)):
        if not numpy.array_equal(list1[i], list2[i]):
            return False
    return True


def load_data_file(name):
    # loads the data file
    data = open(name, 'r')
    final_list = []
    for i in range(ROWS):
        line = data.readline()
        string_rep = line.strip().split()
        int_rep = [int(x) for x in string_rep]
        final_list.append(numpy.asarray(int_rep))
    data.close()
    return final_list


def load_label_file(name):
    # loads the label file
    data = open(name, 'r')
    final_list = []
    for i in range(ROWS):
        line = data.readline()
        string_rep = line.strip()
        final_list.append(int(string_rep))
    data.close()
    return final_list


if __name__ == "__main__":
    data = load_data_file("mnist_data.txt")
    labels = load_label_file("mnist_labels.txt")
    avg_iterations = 0.0
    avg_differences = 0.0
    avg_iterations2 = 0.0
    avg_differences2 = 0.0
    total_runs = 10
    k = 10
    # runs for as many times as total_runs, randomly chooses initial centriods
    for a in range(total_runs):
        iterations, centrioid_clusters = find_centriods_randomly(
            k, data)
        avg_iterations += iterations
        sum_differences = 0.0
        # runs for all of the clusters
        for b in range(k):
            # if the cluster is not empty
            if len(centrioid_clusters[b]) > 0:
                # get the sum of differences from the most common digit in this
                # cluster and add that to the sum
                sum_differences += different_from_digit(most_common_digit(
                    centrioid_clusters[b], labels), centrioid_clusters[b], labels)
        # add the sum to the avg of differences
        avg_differences += sum_differences
    # runs for as many times as total_runs,
    # randomly chooses an instance that represents each of the digits and uses them as the centroids
    for a in range(total_runs):
        iterations, centrioid_clusters = find_centriods_randomly_with_labels(
            k, data, labels)
        avg_iterations2 += iterations
        sum_differences = 0.0
        # runs for all of the clusters
        for b in range(k):
            # if the cluster is not empty
            if len(centrioid_clusters[b]) > 0:
                # get the sum of differences from the most common digit in this
                # cluster and add that to the sum
                sum_differences += different_from_digit(most_common_digit(
                    centrioid_clusters[b], labels), centrioid_clusters[b], labels)
        # add the sum to the avg of differences
        avg_differences2 += sum_differences
    # divide the averages by the total runs
    avg_differences /= total_runs
    avg_iterations /= total_runs
    avg_differences2 /= total_runs
    avg_iterations2 /= total_runs
    # print out the results
    print("k=10")
    print(
        F"Over {total_runs} runs, and {ROWS} rows, with a completely random initial centriods yields")
    print(
        F"The average number of instances that are in the wrong cluster: {avg_differences}")
    print(
        F"The average number of iterations to convergence: {avg_iterations}")
    print(
        F"Over {total_runs} runs, and {ROWS} rows, with randomly chosen initial centriods that represents each of the digits yields")
    print(
        F"The average number of instances that are in the wrong cluster: {avg_differences2}")
    print(
        F"The average number of iterations to convergence: {avg_iterations2}")
    print("k=5")
    print("Labels Grouped:")
    iterations, centrioid_clusters = find_centriods_randomly(
        5, data)
    label_groups = []
    for i in range(len(centrioid_clusters)):
        print(most_common_digit(centrioid_clusters[i], labels))
        label_groups.append([])
        for j in range(len(centrioid_clusters[i])):
            label_groups[i].append(labels[centrioid_clusters[i][j]])
    print(label_groups)
    # shows the images of all of the centriods for one run
    find_and_print_centriods(10, data)
