httoop
======

An object oriented HTTP/1.1 library. (HTTP/2 will probably follow in the future).

Httoop can be used to parse, compose and work with HTTP-Request- and Response-Messages.

It is an generic library for implementing HTTP servers, clients, caches and proxies.

Httoop provides an powerful interface using the vocabularity used in RFC 7230 - 7235 and focuses on implementing HTTP "compliant" as defined in [RFC 7230 Section 2.5](http://tools.ietf.org/html/rfc7230#section-2.5).

"An implementation is not compliant if it fails to satisfy one or more of the MUST or REQUIRED level requirements for the protocols it implements."
[RFC 2616 Section 1.2](http://tools.ietf.org/html/rfc2616#section-1.2)

On top of the object oriented abstraction of HTTP httoop provides an easy way to support WSGI.


HTTP and extensions are defined in the following RFC's:

* HTTP/1.1 RFC 7230 [Message Syntax and Routing](http://tools.ietf.org/html/7230)

* HTTP/1.1 RFC 7231 [Semantics and Content](http://tools.ietf.org/html/7231)

* HTTP/1.1 RFC 7232 [Conditional Requests](http://tools.ietf.org/html/7232)

* HTTP/1.1 RFC 7233 [Range Requests](http://tools.ietf.org/html/7233)

* HTTP/1.1 RFC 7234 [Caching](http://tools.ietf.org/html/7234)

* HTTP/1.1 RFC 7235 [Authentication](http://tools.ietf.org/html/7235)

* HTTP/2 RFC 7540 [Hypertext Transfer Protocol Version 2](https://tools.ietf.org/html/rfc7540)

* HTTP/2 RFC 7541 [HPACK: Header Compression for HTTP/2](https://tools.ietf.org/html/rfc7541)

* RFC 5987 [Character Set and Language Encoding for Hypertext Transfer Protocol (HTTP) Header Field Parameters](https://tools.ietf.org/html/rfc5987)

* Uniform Resource Identifier (URI) ([RFC 3986](https://tools.ietf.org/html/rfc3986))

* Internet Message Format ([RFC 822](http://tools.ietf.org/html/822), [2822](http://tools.ietf.org/html/2822), [5322](http://tools.ietf.org/html/5322))

* HTTP Authentication: Basic and Digest Access Authentication ([RFC 2617](http://tools.ietf.org/html/2617))

* Additional HTTP Status Codes ([RFC 6585](http://tools.ietf.org/html/6585))

* Forwarded HTTP Extension [RFC 7239](https://tools.ietf.org/html/rfc7239)

* Prefer Header for HTTP [RFC 7240](https://tools.ietf.org/html/rfc7240)

* PATCH Method for HTTP ([RFC 5789](http://tools.ietf.org/html/5789))

* Use of the Content-Disposition Header Field in the Hypertext Transfer Protocol (HTTP) ([RFC 6266](http://tools.ietf.org/html/6266))

* Upgrading to TLS Within HTTP/1.1 ([RFC 2817](http://tools.ietf.org/html/2817))

* Transparent Content Negotiation in HTTP ([RFC 2295](http://tools.ietf.org/html/2295))

* HTTP Remote Variant Selection Algorithm -- RVSA/1.0 ([RFC 2296](http://tools.ietf.org/html/2296))

* HTTP State Management Mechanism ([RFC 6265](http://tools.ietf.org/html/6265))

* HTTP Extensions for Web Distributed Authoring and Versioning (WebDAV) ([RFC 4918](http://tools.ietf.org/html/4918))

* Hyper Text Coffee Pot Control Protocol (HTCPCP/1.0) ([RFC 2324](http://tools.ietf.org/html/2324))

Extended information about hypermedia, WWW and how HTTP is meant to be used:

* Web Linking ([RFC 5988](http://tools.ietf.org/html/5988))

* Representational State Transfer [REST](http://www.ics.uci.edu/~fielding/pubs/dissertation/rest_arch_style.htm)

* [Test Cases for HTTP Content-Disposition header field](http://greenbytes.de/tech/tc2231/)
