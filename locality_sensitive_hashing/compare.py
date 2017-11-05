
class Compare:

    def compare_sets(self, set1, set2):
        """

        :param set1:
        :param set2:
        :return:
        """

        set_intersection = set1.intersection(set2)
        set_union = set1.union(set2)

        jaccard_similarity = len(set_intersection)/len(set_union)
        return jaccard_similarity

    def jaccard_similarity(self):
        pass
