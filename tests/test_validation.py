import lxml.etree
import pytest

from pathlib import Path

TESTDIR = Path(__file__).parent
BASEDIR = TESTDIR.parent
XRRL_PATH = BASEDIR.joinpath('xrrl.xsd')


def parse(path):
    return lxml.etree.parse(str(path))


def get_schema(path):
    return lxml.etree.XMLSchema(parse(path))


def assert_schema_from_path(schema, path):
    schema.assert_(parse(path))


@pytest.fixture
def xrrl_schema():
    return get_schema(XRRL_PATH)


@pytest.fixture
def xsd_schema():
    return get_schema(TESTDIR.joinpath('XMLSchema.xsd'))


def test_xsd_validity(xsd_schema):
    assert_schema_from_path(xsd_schema, XRRL_PATH)


def test_structures_module_validity(xsd_schema):
    assert_schema_from_path(
        xsd_schema,
        BASEDIR.joinpath('xrrl-structures-1.xsd'))


def test_basic_rule(xrrl_schema):
    doc = parse(TESTDIR.joinpath('rule.xrrl'))
    xrrl_schema.assert_(doc)
