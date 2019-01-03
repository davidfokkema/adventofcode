import unittest

from repose_record import (find_guard_with_most_sleep,
                           find_minute_with_most_sleep, add_up_repose_records)


TEST_INPUT = """\
[1518-11-01 00:00] Guard #10 begins shift
[1518-11-01 00:05] falls asleep
[1518-11-01 00:25] wakes up
[1518-11-01 00:30] falls asleep
[1518-11-01 00:55] wakes up
[1518-11-01 23:58] Guard #99 begins shift
[1518-11-02 00:40] falls asleep
[1518-11-02 00:50] wakes up
[1518-11-03 00:05] Guard #10 begins shift
[1518-11-03 00:24] falls asleep
[1518-11-03 00:29] wakes up
[1518-11-04 00:02] Guard #99 begins shift
[1518-11-04 00:36] falls asleep
[1518-11-04 00:46] wakes up
[1518-11-05 00:03] Guard #99 begins shift
[1518-11-05 00:45] falls asleep
[1518-11-05 00:55] wakes up
""".splitlines()


class ReposeRecordTest(unittest.TestCase):
    def setUp(self):
        self.records = add_up_repose_records(TEST_INPUT)

    def test_find_guard_with_most_sleep(self):
        self.assertEqual(find_guard_with_most_sleep(self.records), '#10')

    def test_find_minute_with_most_sleep(self):
        self.assertEqual(find_minute_with_most_sleep(self.records, '#10'), 24)

    def test_make_repose_record(self):
        self.assertEqual(self.records['#10'][4], 0)
        self.assertEqual(self.records['#10'][5], 1)
        self.assertEqual(self.records['#10'][24], 2)


if __name__ == '__main__':
    unittest.main()
