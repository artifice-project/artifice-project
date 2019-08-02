import unittest
import os
import sys
import datetime

import artifice.util as util


class TimesTest(unittest.TestCase):

    def setUp(self):
        '''
        IF THESE VALUES ARE MODIFIED, TESTS WILL BREAK!
        '''
        self.pkg = 'artifice.util.times'
        self.then = datetime.datetime(2019, 8, 1, 20, 59, 28, 641644)
        self.now = datetime.datetime(2019, 8, 2, 20, 38, 8, 941428)
        self.timedelta = self.now - self.then
        self.known_dhm = (0, 23, 38)
        self.known_sentence = '23 hours ago'


    def test_import_times(self):
        '''
        ensures that package import did not fail silently
        '''
        module = self.pkg
        self.assertIn(module, sys.modules)


    def test_right_now(self):
        '''
        ensure that right_now() is including milliseconds
        '''
        a = util.right_now()
        b = util.right_now()
        self.assertNotEqual(a,b)


    def test_days_hours_minutes(self):
        '''
        ensure that timedelta is properly calculated
        '''
        dhm = util.days_hours_minutes(self.timedelta)
        self.assertEqual(self.known_dhm, dhm)


    def test_elapsed_time_tuple(self):
        dhm = util.elapsed_time(self.timedelta)
        self.assertTupleEqual(self.known_dhm, dhm)


    def test_elapsed_time_dict(self):
        dhm = util.elapsed_time(self.timedelta, as_dict=True)
        self.assertIsInstance(dhm, dict)


    def test_render_time_weeks(self):
        t = (14, 4, 8)
        sentence = util.render_time(*t)
        self.assertEqual('2 weeks ago', sentence)


    def test_render_time_week(self):
        t = (7, 4, 8)
        sentence = util.render_time(*t)
        self.assertEqual('1 week ago', sentence)


    def test_render_time_days(self):
        t = (6, 9, 12)
        sentence = util.render_time(*t)
        self.assertEqual('6 days ago', sentence)


    def test_render_time_day(self):
        t = (1, 9, 12)
        sentence = util.render_time(*t)
        self.assertEqual('1 day ago', sentence)


    def test_render_time_hours(self):
        t = (0, 13, 58)
        sentence = util.render_time(*t)
        self.assertEqual('13 hours ago', sentence)


    def test_render_time_hour(self):
        t = (0, 1, 58)
        sentence = util.render_time(*t)
        self.assertEqual('1 hour ago', sentence)


    def test_render_time_minutes(self):
        t = (0, 0, 11)
        sentence = util.render_time(*t)
        self.assertEqual('11 minutes ago', sentence)


    def test_render_time_minute(self):
        t = (0, 0, 1)
        sentence = util.render_time(*t)
        self.assertEqual('1 minute ago', sentence)


    def test_render_time_now(self):
        sentence = util.render_time(0, 0, 0)
        self.assertEqual('Just Now', sentence)


    def test_decorate_time_arg(self):
        sentence = util.decorate_time(self.timedelta)
        self.assertEqual(self.known_sentence, sentence)


    def test_decorate_time_args(self):
        sentence = util.decorate_time(self.then, self.now)
        self.assertEqual(self.known_sentence, sentence)



if __name__ == '__main__':
    unittest.main()
