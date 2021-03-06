# -*- coding: utf-8 -*-

from binascii import Error as Base64Error
from base64 import decodestring as decode_base64, encodestring as encode_base64

from httoop.header.element import HeaderElement
from httoop.exceptions import InvalidHeader
from httoop.util import _


class BasicAuthRequestScheme(object):

	@staticmethod
	def parse(authinfo):
		try:
			authinfo = authinfo.encode('ascii')
		except ValueError:
			raise InvalidHeader(_(u'Invalid base64 in basic authentication'))

		try:
			username, password = decode_base64(authinfo.strip()).split(':')
		except Base64Error:
			raise InvalidHeader(_(u'Basic authentication contains invalid base64'))
		except ValueError:
			raise InvalidHeader(_(u'No username:password provided'))

		authinfo = {
			'username': username.decode('ISO8859-1'),
			'password': password.decode('ISO8859-1')
		}
		return authinfo

	@staticmethod
	def compose(authinfo):
		username = authinfo['username']
		password = authinfo['password']
		username = username.encode('ISO8859-1')
		password = password.encode('ISO8859-1')
		return encode_base64(b'%s:%s' % (username, password)).strip()


class BasicAuthResponseScheme(object):

	@staticmethod
	def parse(authinfo):
		params = HeaderElement.parseparams(b'X;%s' % authinfo)[1]
		params.setdefault('realm', '')
		return params

	@staticmethod
	def compose(authinfo):
		return HeaderElement.formatparam(b'realm', authinfo['realm'].encode('ISO8859-1', 'replace'), True)
