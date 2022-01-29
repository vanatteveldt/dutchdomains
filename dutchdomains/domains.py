import json
from typing import Iterable, Tuple
import jsonlines

_CATEGORIES = None


def get_categories():
    global _CATEGORIES
    if _CATEGORIES is None:
        _CATEGORIES = {x['url']: x for x in read_categories()}
    return _CATEGORIES


def read_categories(filename='dutchdomains.jsonl'):
    with jsonlines.open(filename) as reader:
        for d in reader:
            categories = d.pop('categories')
            cat = max(categories, key=categories.get)
            yield dict(url=d['url'], category=cat, icon=d.get('icon-large'))


def get_domains(domains: Iterable[str]) -> Iterable[Tuple[str, dict]]:
    categories = get_categories()
    for domain in domains:
        for alias in (domain, domain.replace("www.", ""), f"www.{domain}"):
            if alias in categories:
                yield domain, categories[alias]


if __name__ == '__main__':
    result = dict(get_domains(["twitter.com", "mediamarkt.nl", "www.ajaxshowtime.com", "www.twitter.com"]))
    print(result)
    print(json.dumps(result, indent=2))
