from locality_sensitive_hashing.minhashing import MinHashing
from locality_sensitive_hashing.shingling import Shingling
import locality_sensitive_hashing.lsh as lsh

from tqdm import tqdm, trange

# You can run this code for different portions of the dataset.
# It ships with data set sizes 100, 1000, 2500, and 10000.
numDocs = 100


def read_ground_truth(truthFile):
    plagiaries = {}

    # Open the truth file.
    f = open(truthFile, "r")

    # For each line of the files...
    for line in f:

        # Strip the newline character, if present.
        if line[-1] == '\n':
            line = line[0:-1]

        docs = line.split(" ")

        # Map the two documents to each other.
        plagiaries[docs[0]] = docs[1]
        plagiaries[docs[1]] = docs[0]

    # Close the data file.
    f.close()

    return plagiaries


def compute_k_shingles(dataFile, k=5):
    doc_list = []
    shingle_set = {}

    f = open(dataFile, "r")

    for i in tqdm(range(numDocs),
                  desc="Computing {}-shingles for {} documents".format(k, numDocs)):
        document = f.readline()
        doc_id, doc_body = document.split(" ", 1)

        doc_list.append(doc_id)
        shingle_set[doc_id] = Shingling(doc_body, k).shingles

    # Close the data file.
    f.close()

    return doc_list, shingle_set


def compute_minhash(shingle_set, doc_list, threshold, n=100):
    minhash_doc_list = []
    for i in tqdm(range(numDocs),
                  desc="Calculating min hash for {} documents".format(numDocs)):
        set1 = shingle_set[doc_list[i]]
        min1 = MinHashing(set1, n)
        minhash_doc_list.append(min1.signature)

    return minhash_doc_list


def main():
    text = "The hash, then, is only stable if you don't restart the Python process or set PYTHONHASHSEED to a fixed " \
           "decimal number "

    dataFile = "../data/articles_" + str(numDocs) + ".train"
    truthFile = "../data/articles_" + str(numDocs) + ".truth"

    plagiaries = read_ground_truth(truthFile)
    doc_list, shingle_set = compute_k_shingles(dataFile, k=5)

    minhash_docs = compute_minhash(shingle_set, doc_list, threshold=0.5, n=100)

    lsh_threshold = 0.8
    doc_signitures_dict = dict(zip(doc_list, minhash_docs))

    lsh_sim = lsh.LSH(doc_signitures_dict, lsh_threshold).similar_pairs

    print(plagiaries)
    print(lsh_sim)


if __name__ == "__main__":
    main()
