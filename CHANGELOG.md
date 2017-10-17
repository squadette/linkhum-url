0.1.7:

* percent-encode square brackets in :url_encoded part of the result, because of HTTParty;

0.1.5:

* More fixes to URLs with special symbols in query strings (tnx @markiz);

0.1.4:

* Handle URLs with hashtags in query strings (tnx @markiz);

0.1.3:

* Handle IDNs that begin with ASCII;

0.1.2:

* Handle explicit port numbers in URLs;

0.1.1:

* Handle percent-encoded non-UTF8 query strings: return
percent-encoded value as human-readable (we have no way of guessing the original encoding);

0.1.0:

* Initial release.
