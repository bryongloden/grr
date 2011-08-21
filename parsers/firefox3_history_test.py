#!/usr/bin/env python
#
# Copyright 2011 Google Inc.
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.





import datetime
import os

from grr.client import conf
from grr.client import conf as flags
from grr.lib import test_lib
from grr.parsers import firefox3_history

FLAGS = flags.FLAGS

# Test method names dont conform with Google style


class Firefox3HistoryTest(test_lib.GRRBaseTest):
  """Test parsing of Firefox 3 history files."""

  # places.sqlite contains a single history entry:
  # 2011-07-01 11:16:21.371935	FIREFOX3_VISIT \
  # 	http://news.google.com/	Google News
  def testBasicParsing(self):
    """Test we can parse a standard file."""
    history_file = os.path.join(self.base_path, "places.sqlite")
    history = firefox3_history.Firefox3History(open(history_file))
    # Parse returns (timestamp, dtype, url, title)
    entries = [x for x in history.Parse()]

    try:
      dt1 = datetime.datetime(1970, 1, 1)
      dt1 += datetime.timedelta(microseconds=entries[0][0])
    except TypeError:
      dt1 = entries[0][0]
    except ValueError:
      dt1 = entries[0][0]

    self.assertEquals(str(dt1), "2011-07-01 11:16:21.371935")
    self.assertEquals(entries[0][2], "http://news.google.com/")
    self.assertEquals(entries[0][3], "Google News")
    self.assertEquals(len(entries), 1)


def main(argv):
  test_lib.main(argv)

if __name__ == "__main__":
  conf.StartMain(main)
