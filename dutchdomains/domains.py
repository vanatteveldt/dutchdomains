import json
from typing import Iterable

from dutchdomains.db import Domain, Category

CATS = {id: label for (id, label) in Category.select(Category.id, Category.label).tuples()}


def get_domains(domains: Iterable[str]) -> Iterable[tuple]:
    for url, logo, cat in Domain.select(Domain.url, Domain.logo, Domain.main_category).where(Domain.url.in_(domains)).tuples():
        yield (url, logo, CATS[cat])


def get_domains_dict(domains: Iterable[str]) -> dict:
    return {url: {"logo": logo, "category": cat}
            for (url, logo, cat) in get_domains(domains)}


if __name__ == '__main__':
    result = get_domains_dict(["twitter.com", "www.mediamarkt.nl", "www.ajaxshowtime.com"])
    print(json.dumps(result, indent=2))