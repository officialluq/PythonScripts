# data set source: https://www.kaggle.com/datasets/imoore/age-dataset
from multiprocessing import Pool
import sys


def chunks(l, n):
    return (l[i:i + n] for i in range(0, len(l), n))


def Map(L):
    results = []
    for w in L:
        results.append((w, 1))
    return results


def Partition(L):
    tf = {}

    for sublist in L:
        for p in sublist:
            # Append the tuple to the list in the map
            try:
                tf[p[0]].append(p)
            except KeyError:
                tf[p[0]] = [p]
    return tf


def Reduce(Mapping):
    return (Mapping[0], sum(pair[1] for pair in Mapping[1]))


if __name__ == '__main__':
    storage = []
    with open('data.csv', 'r', encoding="utf-8") as file:
        file.readline()
        for line in file:
            if line.split(",")[9].isdigit():
                storage.append(int(line.split(",")[9]))
    print("Build a pool of 8 processes")
    pool = Pool(processes=32)
    print("Fragment the string data into 8 chunks", file=sys.stderr)
    partitioned_stars = list(chunks(storage, len(storage) // 8))
    single_count_tuples = pool.map(Map, partitioned_stars)
    token_to_tuples = Partition(single_count_tuples)
    #print(token_to_tuples)

    term_frequencies = pool.map(Reduce, token_to_tuples.items())
    term_frequencies.sort(key=lambda x: x[0])  # nb of stars
    for pair in term_frequencies[:20]:
        print( "%i occurs %i times" % pair )
