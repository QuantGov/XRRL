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


@pytest.fixture
def xrrl_schema():
    return get_schema(XRRL_PATH)


def test_xsd_validity():
    get_schema(TESTDIR.joinpath('XMLSchema.xsd')).assert_(parse(XRRL_PATH))


def test_basic_rule(xrrl_schema):
    xrrl_schema.assert_(parse(TESTDIR.joinpath('rule.xrrl')))
