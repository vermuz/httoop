# -*- coding: utf-8 -*-
u"""Utilities for python2/3 compatibility"""

__all__ = [
	'PY3', 'Unicode', 'iteritems',
	'to_unicode', 'to_ascii', 'decode_header',
	'IFile', 'partial', 'formatdate', 'parsedate',
	'CaseInsensitiveDict', 'decode_rfc2231',
]

import sys
from functools import partial

PY3 = sys.version_info[0] == 3

try:
	Unicode = unicode
except NameError:
	Unicode = str

try:
	from email.utils import formatdate, parsedate, decode_rfc2231
	formatdate = partial(formatdate, usegmt=True)
except ImportError:  # pragma: no cover
	from rfc822 import formatdate, parsedate

try:
	from email.Header import decode_header
except ImportError: # pragma: no cover
	from email.header import decode_header


def iteritems(d, **kw):
	return iter(getattr(d, 'items' if PY3 else 'iteritems')(**kw))


def to_unicode(string):
	if string is None:
		return u''
	if isinstance(string, bytes):
		try:
			return string.decode('UTF-8')
		except UnicodeDecodeError:
			return string.decode('ISO8859-1')
	return Unicode(string)


def to_ascii(string):
	if isinstance(string, Unicode):
		return string.encode('ascii', 'ignore')
	return bytes(string).decode('ascii', 'ignore').encode('ascii')


def if_has(func):
	def _decorated(self, *args, **kwargs):
		if hasattr(self.fd, func.__name__):
			return func(self, *args, **kwargs)
		return False
	return _decorated


class IFile(object):
	u"""The file interface"""
	__slots__ = ('fd')

	@property
	def name(self):
		return getattr(self.fd, 'name', None)

	@if_has
	def close(self):
		return self.fd.close()

	@if_has
	def flush(self):
		return self.fd.flush()

	@if_has
	def read(self, *size):
		return self.fd.read(*size[:1])

	@if_has
	def readline(self, *size):
		return self.fd.readline(*size[:1])

	@if_has
	def readlines(self, *size):
		return self.fd.readlines(*size[:1])

	@if_has
	def write(self, bytes_):
		return self.fd.write(bytes_)

	@if_has
	def writelines(self, sequence_of_strings):
		return self.fd.writelines(sequence_of_strings)

	@if_has
	def seek(self, offset, whence=0):
		return self.fd.seek(offset, whence)

	@if_has
	def tell(self):
		return self.fd.tell()

	@if_has
	def truncate(self, size=None):
		return self.fd.truncate(size)


class CaseInsensitiveDict(dict):
	"""A case-insensitive dict subclass optimized for HTTP header use.

		Each key is stored as case insensitive ascii
		Each value is stored as unicode
	"""

	@staticmethod
	def formatkey(key):
		return to_ascii(key).title()

	@staticmethod
	def formatvalue(value):
		return value

	def __init__(self, *args, **kwargs):
		d = dict(*args, **kwargs)
		for key, value in iteritems(d):
			dict.__setitem__(self, self.formatkey(key), self.formatvalue(value))
		dict.__init__(self)

	def __getitem__(self, key):
		return dict.__getitem__(self, self.formatkey(key))

	def __setitem__(self, key, value):
		dict.__setitem__(self, self.formatkey(key), self.formatvalue(value))

	def __delitem__(self, key):
		dict.__delitem__(self, self.formatkey(key))

	def __contains__(self, key):
		return dict.__contains__(self, self.formatkey(key))

	def get(self, key, default=None):
		return dict.get(self, self.formatkey(key), default)

	def update(self, E):
		for key in E.keys():
			self[self.formatkey(key)] = self.formatvalue(E[key])

	def setdefault(self, key, x=None):
		key = self.formatkey(key)
		try:
			return dict.__getitem__(self, key)
		except KeyError:
			self[key] = self.formatvalue(x)
			return dict.__getitem__(self, key)

	def pop(self, key, default=None):
		return dict.pop(self, self.formatkey(key), default)

	@classmethod
	def fromkeys(cls, seq, value=None):
		newdict = cls()
		for k in seq:
			newdict[k] = cls.formatvalue(value)
		return newdict
