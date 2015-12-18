import pytest
from httoop import URI


@pytest.mark.parametrize('query_string,query', [
	(b'', ()),
	(b'&', ()),
	(b'&&', ()),
	pytest.mark.skipif((b'=', ((u'', u''),))),
	pytest.mark.skipif((b'=a', ((u'', u'a'),))),
	(b'a', ((u'a', u''),)),
	(b'a=', ((u'a', u''),)),
	(b'&a=b', ((u'a', u'b'),)),
	(b'&&a=b&&b=c&d=f&', ((u'a', u'b'), (u'b', u'c'), (u'd', u'f'))),
	(b'a=a+b&b=b+c', ((u'a', u'a b'), (u'b', u'b c'))),
	(b'a=a%20b&b=b%20c', ((u'a', u'a b'), (u'b', u'b c'))),
	(b'a=a+b&b=b%20c', ((u'a', u'a b'), (u'b', u'b c'))),
	(b'a=1&a=2', ((u'a', u'1'), (u'a', u'2'))),
])
def test_query_string_parse(query_string, query):
	uri = URI(b'http://example.com/?%s' % (query_string,))
	assert uri.query == query


@pytest.mark.parametrize('query_string,query', [
	(b'', ()),
	pytest.mark.skipif((b'=', ((u'', u''),))),
	pytest.mark.skipif((b'=a', ((u'', u'a'),))),
	(b'a', ((u'a', u''),)),
	pytest.mark.skipif((b'a=', ((u'a', u''),))),
	(b'a=b', ((u'a', u'b'),)),
	(b'a=b&b=c&d=f', ((u'a', u'b'), (u'b', u'c'), (u'd', u'f'))),
	(b'a=a+b&b=b+c', ((u'a', u'a b'), (u'b', u'b c'))),
	(b'a=1&a=2', ((u'a', u'1'), (u'a', u'2'))),
	(b"a=some+value", {'a': 'some value'}),
	(b"a=some+value/another", {'a': 'some value/another'}),
])
def test_query_string_compose(query_string, query):
	uri = URI(b'http://example.com/')
	uri.query = query
	assert uri.query_string == query_string


@pytest.mark.xfail(reason='API not yet implemented.')
@pytest.mark.parametrize('query_string,encoding,query', [
	(b"key=\u0141%E9", "latin-1", [(u'key', u'\u0141\xE9')]),
	(b"key=\u0141%C3%A9", "utf-8", [(u'key', u'\u0141\xE9')]),
	(b"key=\u0141%C3%A9", "ascii", [(u'key', u'\u0141\ufffd\ufffd')]),
	(b"key=\u0141%E9-", "ascii", [(u'key', u'\u0141\ufffd-')]),
])
def test_parse_encodings(query_string, encoding, query):
	u = URI()
	u.encoding = encoding
	u.parse(b'http://example.com/?%s' % (query_string,))
	assert u.query == tuple(query)


@pytest.mark.xfail(reason='API not yet implemented.')
def test_urlencode_sequences():
	u = URI()
	u.query = {'a': [1, 2], 'b': (3, 4, 5)}
	assert set(u.query_string.split(b'&')) == {b'a=1', b'a=2', b'b=3', b'b=4', b'b=5'}


@pytest.mark.xfail(reason='API not yet implemented.')
def test_urlencode_object():
	class Trivial(object):
		def __str__(self):
			return 'trivial'
		def __unicode__(self):
			return u'trivial'
		def __bytes__(self):
			return b'trivial'

	u = URI()
	u.query = {u'a': Trivial()}
	assert u.query_string == b'a=trivial'
