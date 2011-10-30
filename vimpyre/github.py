#!/usr/bin/env python
#coding:utf-8

import requests
import lxml.html as lhtml

class GitHub(object):

    GITHUB_BASE = 'https://github.com'
    GITHUB_SEARCH_BASE = GITHUB_BASE + '/search?langOverride=&language=VimL&q=SEARCH_NAME&repo=&start_value=1&type=Repositories'

    def __init__(self):
        self._filter_keyword = False
        pass

    def _search_results(self, keyword):
        if self._filter_keyword:
            keyword = keyword.split('/')[-1]

        url = self.GITHUB_SEARCH_BASE.replace('SEARCH_NAME', keyword)
        r = requests.get(url)

        if r.status_code == 200:
            dom_root = lhtml.fromstring(r.content)
            results = dom_root.xpath('//div[@class="results"]')[0].xpath('./div[@class="result"]')
            return results
        
        return False

    def _render_format(self, results):
        if results:
            items = []
            for element in results:
                item = {'name': '', 'description': '', 'url': ''}
                try:
                    item['name'] = element.xpath('./h2[@class="title"]/a')[0].text.replace(' ', '').strip()
                    item['description'] = element.xpath('./div[@class="description"]')[0].text.strip()
                    item['url'] = self.GITHUB_BASE + element.xpath('./h2[@class="title"]/a/@href')[0]
                    items.append(item)
                except:
                    pass

            return items
        else:
            return []

    def _filter_result(self, results, keyword):
        return [item for item in results if item['name'] == keyword]

    def search(self, keyword):
        if '/' in keyword:
            self._filter_keyword = True

        results = self._search_results(keyword)
        rets = self._render_format(results)

        if self._filter_keyword:
            return self._filter_result(rets, keyword)
        else:
            return rets
       
if __name__ == '__main__':
    from pprint import pprint
    pprint(GitHub().search('html5.vim'))
    pprint(GitHub().search('vim-scripts/html5.vim'))

