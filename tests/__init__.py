# -*- coding: utf-8 -*-
'''A test package for Word Fusion.'''

import unittest
import tempfile

import wordfusion

class WordFusionTestCase(unittest.TestCase):
    '''Class that define the setUp and tearDown.'''

    def setUp(self):
        '''Prepare the app to be tested.
        Request the test client.
        Init the testing database.
        '''
        wordfusion.app.config.from_object('wordfusion.config.Testing')

        self.app = wordfusion.app.test_client()

        with wordfusion.app.app_context():
            wordfusion.database.init_db()

    def tearDown(self):
        pass

from tests.indexpage import IndexPage

if __name__ == '__main__':
    unittest.main()
