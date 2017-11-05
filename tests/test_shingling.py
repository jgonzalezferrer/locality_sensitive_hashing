from nose.tools import assert_equal

from locality_sensitive_hashing.shingling import Shingling
from locality_sensitive_hashing.minhashing import MinHashing
from locality_sensitive_hashing.utility import compare_sets, compare_signatures


def test_strings_shingling_similarity():
    editorial = "editorial"
    factorial = "factorial"
    expected_values = [(1, 0.6), (5, 0.25), (9, 0.0)]

    for k, expected in expected_values:
        editorial_shingle = Shingling(editorial, k)
        factorial_shingle = Shingling(factorial, k)
        jaccard_similarity = compare_sets(editorial_shingle.shingles, factorial_shingle.shingles)

        assert_equal(jaccard_similarity, expected, "Jaccard similarity of '{}' and '{}' failed. "
                                                   "Expected: {}, got: {}. "
                     .format(editorial, factorial, expected, jaccard_similarity))


def test_minhash_similarity():
    str1 = "Lorem ipsum is a pseudo-Latin text used in web design, typography, layout, and printing in place of " \
           "English to emphasise design elements over content. It's also called placeholder (or filler) text. It's a " \
           "convenient tool for mock-ups. It helps to outline the visual elements of a document or presentation, eg " \
           "typography, font, or layout. Lorem ipsum is mostly a part of a Latin text by the classical author and " \
           "philosopher Cicero. Its words and letters have been changed by addition or removal, so to deliberately " \
           "render its content nonsensical; it's not genuine, correct, or comprehensible Latin anymore. While lorem " \
           "ipsum's still resembles classical Latin, it actually has no meaning whatsoever. As Cicero's text doesn't " \
           "contain the letters K, W, or Z, alien to latin, these, and others are often inserted randomly to mimic " \
           "the typographic appearence of European languages, as are digraphs not to be found in the original."

    str2 = "Lorem ipsum is a pseudo-Latin text used in web design, typography, layout, and printing in place of " \
           "English to emphasise design elements over content. It's also called placeholder (or filler) text. It's a " \
           "convenient tool for mock-ups. It helps to outline the visual elements of a document or presentation, eg " \
           "typography, font, or layout. Lorem ipsum is mostly a part of a Latin text by the classical author and " \
           "philosopher Cicero. Its words and letters have been changed by addition or removal, so to deliberately " \
           "render its content nonsensical; it's not genuine, correct, or comprehensible Latin anymore. " \
           "While lorem ipsum's still resembles classical Latin, it actually has no meaning whatsoever."

    str1_shingle = Shingling(str1, 10)
    str2_shingle = Shingling(str2, 10)

    str1_minhashing = MinHashing(str1_shingle.shingles, 100)
    str2_minhashing = MinHashing(str2_shingle.shingles, 100)

    print(compare_signatures(str1_minhashing.signature, str2_minhashing.signature))


if __name__ == "__main__":
    test_minhash_similarity()