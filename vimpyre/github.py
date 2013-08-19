#!/usr/bin/env python
#coding:utf-8

import requests
from contextlib import closing
try:
    import simplejson as json
except ImportError:
    import json

class GitHub(object):

    def __init__(self):
        self._filter_keyword = False

    def _search_results(self, keyword):
        if self._filter_keyword:
            keyword = keyword.split('/')[-1]

        url = 'https://api.github.com/search/repositories?q=%s+language:VimL' % keyword
        with closing(requests.get(url, headers={'Accept': 'application/vnd.github.preview'})) as r:
            if r.status_code == 200:
                results = json.loads(r.content)
                return results
        
        return False

    def _render_format(self, results):
        items = []
        if results and (results['total_count'] > 0):
            for entry in results['items']:
                if not entry['description']:
                    entry['description'] = 'None'
                items.append({'name': entry['name'], 'description': entry['description'], 'url': entry['html_url']})
        return items

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

