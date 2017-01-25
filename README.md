# linkhum-url

URLs which users provide could be both in human-readable form and in
URL-encoded form. `linkhum-url` gem parses URLs in any representation
and returns both representations: human-readable and URL-encoded.

`linkhum-url` handles IDNs and Punycode in domain names.  Behind the
scenes `addressable` gem is used to handle actual URL parsing.

This is a sister gem to
[`linkhum`](https://github.com/zverok/linkhum).

[![Build Status](https://travis-ci.org/squadette/linkhum-url.svg?branch=master)](https://travis-ci.org/squadette/linkhum-url)

## Usage

`linkhum-url` has only one method: `Linkhum::URL.parse(url)`.  It
accepts URL in any representation (usually provided by user) and
returns `Hash` with two keys: `:human_readable` and `:url_encoded`.
Human-readable representation should be displayed to the user, while
URL-encoded representation should be used for HTTP queries, HTML
embedding etc.

    $ irb
    2.3.0 :001 > require 'linkhum-url'
     => true
    2.3.0 :002 > Linkhum::URL.parse("https://example.org")
     => {:human_readable=>"https://example.org", :url_encoded=>"https://example.org"}
    2.3.0 :003 > Linkhum::URL.parse("https://пивбар-хмель.рф/поиск.html?q=пивбар")
     => {:human_readable=>"https://пивбар-хмель.рф/поиск.html?q=пивбар", :url_encoded=>"https://xn----7sbcdsn0agvo0d1e.xn--p1ai/%D0%BF%D0%BE%D0%B8%D1%81%D0%BA.html?q=%D0%BF%D0%B8%D0%B2%D0%B1%D0%B0%D1%80"}
    2.3.0 :004 > Linkhum::URL.parse("https://xn--80abcx8ak.xn--p1ai/%D0%BF%D0%BE%D0%B8%D1%81%D0%BA.html?q=%D0%BF%D0%B8%D0%B2%D0%B1%D0%B0%D1%80")
     => {:human_readable=>"https://пивбар-хмель.рф/поиск.html?q=пивбар", :url_encoded=>"https://xn----7sbcdsn0agvo0d1e.xn--p1ai/%D0%BF%D0%BE%D0%B8%D1%81%D0%BA.html?q=%D0%BF%D0%B8%D0%B2%D0%B1%D0%B0%D1%80"}

## Install

    $ sudo apt-get install idn   # Debian/Ubuntu
    $ brew install libidn        # Mac OS X

    $ gem install linkhum-url

## License

`linkhum-url` released under MIT License.

Copyright (C) Alexey Makhotkin, 2016-2017.
