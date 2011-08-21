#!/usr/bin/env python

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

"""Tests the query lexer."""

from grr.client import conf
from grr.lib import lexer
from grr.lib import test_lib


class LexerTests(test_lib.GRRBaseTest):
  """Test the query language parser."""

  def testParser(self):
    """Test parenthesis precedence."""
    # First build an AST from the expression. (Deliberately include \r\n here):
    ast = lexer.SearchParser(""" ('file name' contains "foo") and (size > 100k
or date before "2011-10")""").Parse()

    self.assertEqual(ast.operator, "and")
    self.assertEqual(ast.parts[0].attribute, "file name")
    self.assertEqual(ast.parts[0].operator, "contains")
    self.assertEqual(ast.parts[0].args[0], "foo")
    self.assertEqual(ast.parts[1].operator, "or")
    self.assertEqual(ast.parts[1].parts[0].attribute, "size")
    self.assertEqual(ast.parts[1].parts[0].operator, ">")
    self.assertEqual(ast.parts[1].parts[0].args[0], "100k")
    self.assertEqual(ast.parts[1].parts[1].attribute, "date")
    self.assertEqual(ast.parts[1].parts[1].operator, "before")
    self.assertEqual(ast.parts[1].parts[1].args[0], "2011-10")

  def testParser2(self):
    """Test operator precedence."""
    # First build an AST from the expression. (Deliberately include \r\n here):
    ast = lexer.SearchParser(""" 'file name' contains "hello" and size > 100k
or 'file name' contains "foo" and date before "2011-10" """).Parse()

    self.assertEqual(ast.operator, "or")
    self.assertEqual(ast.parts[0].operator, "and")
    self.assertEqual(ast.parts[0].parts[0].attribute, "file name")
    self.assertEqual(ast.parts[0].parts[0].operator, "contains")
    self.assertEqual(ast.parts[0].parts[0].args[0], "hello")
    self.assertEqual(ast.parts[0].parts[1].attribute, "size")
    self.assertEqual(ast.parts[0].parts[1].operator, ">")
    self.assertEqual(ast.parts[0].parts[1].args[0], "100k")

    self.assertEqual(ast.parts[1].operator, "and")
    self.assertEqual(ast.parts[1].parts[0].attribute, "file name")
    self.assertEqual(ast.parts[1].parts[0].operator, "contains")
    self.assertEqual(ast.parts[1].parts[0].args[0], "foo")
    self.assertEqual(ast.parts[1].parts[1].attribute, "date")
    self.assertEqual(ast.parts[1].parts[1].operator, "before")
    self.assertEqual(ast.parts[1].parts[1].args[0], "2011-10")

  def testParser3(self):
    """Test quote escaping in strings."""
    # The following has an escaped quote.
    ast = lexer.SearchParser(r"""subject matches '"hello" \'world\''""").Parse()

    self.assertEqual(ast.operator, "matches")
    self.assertEqual(ast.args[0], """\"hello" 'world'""")

  def testFailedParser(self):
    """Test that the parser raises for invalid input."""
    # Some illegal expressions
    for expression in (
        """filename contains "foo""",  # Unterminated string
        """(filename contains "foo" """,  # Unbalanced parenthesis
        """filename contains foo or """):  # empty right expression
      parser = lexer.SearchParser(expression)
      self.assertRaises(lexer.ParseError, parser.Parse)


def main(argv):
  test_lib.main(argv)

if __name__ == "__main__":
  conf.StartMain(main)
