# -*- coding: utf-8 -*-
from tests import WordFusionTestCase

class IndexPage(WordFusionTestCase):
    '''Test the index page.'''

    def test_index_page(self):
        '''Test if index page is loaded, and contain data.'''

        rv = self.app.get('/')
        assert b'Word Fusion' in rv.data
