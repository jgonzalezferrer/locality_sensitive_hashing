class Compare:
    def __init__(self, set1, set2):
        """

        :param set1:
        :param set2:
        """
        self.set1 = set1
        self.set2 = set2
        self._compare_sets()

    def _compare_sets(self):

        set_intersection = self.set1.intersection(self.set2)
        set_union = self.set1.union(self.set2)

        self.compare_sets = len(set_intersection) / len(set_union)

    def jaccard_similarity(self):
        pass
