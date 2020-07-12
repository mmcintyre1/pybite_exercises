import os
from collections import Counter
import re
import urllib.request

tempfile = os.path.join('tmp', 'feed.txt')
urllib.request.urlretrieve(
    'https://bites-data.s3.us-east-2.amazonaws.com/feed',
    tempfile
)

with open(tempfile) as f:
    content = f.read().lower()


def get_pybites_top_tags(n=10):
    """use Counter to get the top 10 PyBites tags from the feed
       data already loaded into the content variable"""
    category_pattern = re.compile('<category>(.*?)</category>')
    categories = Counter(re.findall(category_pattern, content))
    return categories.most_common(n)


if __name__ == '__main__':
    print(get_pybites_top_tags(n=5))
