def compare_sets(set1, set2):

    set_intersection = set1.intersection(set2)
    set_union = set1.union(set2)

    jaccard_similarity = len(set_intersection)/len(set_union)
    return jaccard_similarity
