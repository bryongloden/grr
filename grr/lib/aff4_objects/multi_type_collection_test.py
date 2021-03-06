#!/usr/bin/env python
"""Tests for MultiTypeCollection."""

from grr.lib import aff4
from grr.lib import data_store
from grr.lib import flags
from grr.lib import rdfvalue
from grr.lib import test_lib
from grr.lib import utils

from grr.lib.aff4_objects import multi_type_collection

from grr.lib.rdfvalues import flows as rdf_flows


class MultiTypeCollectionTest(test_lib.AFF4ObjectTest):

  def setUp(self):
    super(MultiTypeCollectionTest, self).setUp()
    self.collection = aff4.FACTORY.Create(
        "aff4:/mt_collection/testAddScan",
        multi_type_collection.MultiTypeCollection,
        token=self.token)

  def testWrapsValueInGrrMessageIfNeeded(self):
    self.collection.Add(rdfvalue.RDFInteger(42))

    items = list(self.collection)
    self.assertTrue(isinstance(items[0], rdf_flows.GrrMessage))
    self.assertEqual(items[0].payload, 42)

  def testValuesOfSingleTypeAreAddedAndIterated(self):
    for i in range(100):
      self.collection.Add(rdf_flows.GrrMessage(payload=rdfvalue.RDFInteger(i)))

    for index, v in enumerate(self.collection):
      self.assertEqual(index, v.payload)

  def testExtractsTypesFromGrrMessage(self):
    self.collection.Add(rdf_flows.GrrMessage(payload=rdfvalue.RDFInteger(0)))
    self.collection.Add(rdf_flows.GrrMessage(payload=rdfvalue.RDFString("foo")))
    self.collection.Add(
        rdf_flows.GrrMessage(payload=rdfvalue.RDFURN("aff4:/foo/bar")))

    self.assertEqual(
        set([
            rdfvalue.RDFInteger.__name__, rdfvalue.RDFString.__name__,
            rdfvalue.RDFURN.__name__
        ]), set(self.collection.ListStoredTypes()))

  def testStoresEmptyGrrMessage(self):
    self.collection.Add(rdf_flows.GrrMessage())

    self.assertListEqual([rdf_flows.GrrMessage.__name__],
                         self.collection.ListStoredTypes())

  def testValuesOfMultipleTypesCanBeIteratedTogether(self):
    original_values = set()
    for i in range(100):
      self.collection.Add(rdf_flows.GrrMessage(payload=rdfvalue.RDFInteger(i)))
      original_values.add(rdf_flows.GrrMessage(payload=rdfvalue.RDFInteger(i)))

      self.collection.Add(rdf_flows.GrrMessage(payload=rdfvalue.RDFString(i)))
      original_values.add(rdf_flows.GrrMessage(payload=rdfvalue.RDFString(i)))

    self.assertEqual(
        sorted([v.payload for v in original_values]),
        sorted([v.payload for v in self.collection]))

  def testLengthOfCollectionIsCorrectWhenMultipleTypesAreUsed(self):
    for i in range(100):
      self.collection.Add(rdf_flows.GrrMessage(payload=rdfvalue.RDFInteger(i)))
      self.collection.Add(rdf_flows.GrrMessage(payload=rdfvalue.RDFString(i)))

    self.assertEqual(200, len(self.collection))

  def testValuesOfMultipleTypesCanBeIteratedPerType(self):
    for i in range(100):
      self.collection.Add(rdf_flows.GrrMessage(payload=rdfvalue.RDFInteger(i)))
      self.collection.Add(rdf_flows.GrrMessage(payload=rdfvalue.RDFString(i)))

    for index, (
        _, v
    ) in enumerate(self.collection.ScanByType(rdfvalue.RDFInteger.__name__)):
      self.assertEqual(index, v.payload)

    for index, (
        _, v
    ) in enumerate(self.collection.ScanByType(rdfvalue.RDFString.__name__)):
      self.assertEqual(str(index), v.payload)

  def testLengthIsReportedCorrectlyForEveryType(self):
    for i in range(99):
      self.collection.Add(rdf_flows.GrrMessage(payload=rdfvalue.RDFInteger(i)))

    for i in range(101):
      self.collection.Add(rdf_flows.GrrMessage(payload=rdfvalue.RDFString(i)))

    self.assertEqual(99,
                     self.collection.LengthByType(rdfvalue.RDFInteger.__name__))
    self.assertEqual(101,
                     self.collection.LengthByType(rdfvalue.RDFString.__name__))

  def testDeletingCollectionDeletesAllSubcollections(self):
    self.collection.Add(rdf_flows.GrrMessage(payload=rdfvalue.RDFInteger(0)))
    self.collection.Add(rdf_flows.GrrMessage(payload=rdfvalue.RDFString("foo")))
    self.collection.Add(
        rdf_flows.GrrMessage(payload=rdfvalue.RDFURN("aff4:/foo/bar")))
    # Need to make sure the object actually exists so we can delete it.
    self.collection.Flush()

    aff4.FACTORY.Delete(self.collection.urn, token=self.token)
    for urn in data_store.DB.subjects.keys():
      self.assertFalse(utils.SmartStr(self.collection.urn) in urn)


def main(argv):
  # Run the full test suite
  test_lib.GrrTestProgram(argv=argv)


if __name__ == "__main__":
  flags.StartMain(main)
