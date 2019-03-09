import re
import pytest
from collections import Counter
from itertools import product
from difflib import SequenceMatcher

TOP_NUMBER = 10
RSS_FEED = 'rss.xml'
SIMILAR = 0.87
IDENTICAL = 1.0

TAG_HTML1 = re.compile(r'<category>(\S+?)</category>')  ## +? makes RE non-greedy mode   ## 'data science' will not match the pattern
TAG_HTML = re.compile(r'<category>([^<]+)</category>')  ## [^<]  any thing not a '<' will be matched. ^ inside [] is logic NOT 

REPLACE_CHARS = str.maketrans('-',' ')

def get_tags():
    """Find all tags in RSS_FEED.
    Replace dash with whitespace.
    """
    with open(RSS_FEED) as f:
        tags = TAG_HTML.findall(f.read().lower())
    return [ tag.translate(REPLACE_CHARS) for tag in tags]

def get_top_tags(tags):
    """Get the TOP_NUMBER of most common tags"""
    cntr = Counter(tags)
    return cntr.most_common()[:TOP_NUMBER]

def get_similarities(tags):
    """Find set of tags pairs with similarity ratio of > SIMILAR"""
    for (tag0, tag1) in product(tags, tags):
        if tag0 != tag1:
            pair = tuple(sorted((tag0, tag1)))   ## so that there is not duplicate like for switching key and value
            seq = SequenceMatcher(None, *pair)
            similarity_ratio = seq.ratio()

            if  SIMILAR < similarity_ratio < IDENTICAL:
                yield pair


def get_similarities_0(tags):
    """Find set of tags pairs with similarity ratio of > SIMILAR"""
    for pair in product(tags, tags):
        # performance enhancements 1.992s -> 0.144s
        if pair[0][0] != pair[1][0]:
            continue
        pair = tuple(sorted(pair))  # set needs hashable type
        similarity = SequenceMatcher(None, *pair).ratio()
        if SIMILAR < similarity < IDENTICAL:
            yield pair


def test_get_tags():
    assert len(get_tags()) == 189

if __name__ == "__main__":
    tags = get_tags()

    top_tags = get_top_tags(tags)
    print('* Top {} tags:'.format(TOP_NUMBER))
    for tag, count in top_tags:
        print('{:<20} {}'.format(tag, count))

    # similar_tags = dict(get_similarities(tags))
    similar_tags = dict(get_similarities(tags))
    print()
    print('* Similar tags:')
    for singular, plural in similar_tags.items():
        print('{:<20} {}'.format(singular, plural))
