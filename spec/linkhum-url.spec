# coding: utf-8  # -*- ruby -*-
require 'spec_helper'

describe Linkhum::URL do
  it "handles ASCII-only URLs" do
    lu = Linkhum::URL.parse("https://example.org/foobar.html?q=baz#anchor")
    expect(lu[:human_readable]).to eql("https://example.org/foobar.html?q=baz#anchor")
    expect(lu[:url_encoded]).to eql("https://example.org/foobar.html?q=baz#anchor")
  end

  it "handles IDNs" do
    lu = Linkhum::URL.parse("https://пивбар-хмель.рф/")
    expect(lu[:human_readable]).to eql("https://пивбар-хмель.рф/")
    expect(lu[:url_encoded]).to eql("https://xn----7sbcdsn0agvo0d1e.xn--p1ai/")
  end

  it "handles Punycode hostnames" do
    lu = Linkhum::URL.parse("https://xn----7sbcdsn0agvo0d1e.xn--p1ai/")
    expect(lu[:human_readable]).to eql("https://пивбар-хмель.рф/")
    expect(lu[:url_encoded]).to eql("https://xn----7sbcdsn0agvo0d1e.xn--p1ai/")
  end

  it "handles Punycode hostnames which begin with ASCII" do
    lu = Linkhum::URL.parse("https://18.xn--b1aew.xn--p1ai/")
    expect(lu[:human_readable]).to eql("https://18.мвд.рф/")
    expect(lu[:url_encoded]).to eql("https://18.xn--b1aew.xn--p1ai/")
  end

  it "handles port numbers" do
    lu = Linkhum::URL.parse("http://linkhum.dev:8080/something.html")
    expect(lu[:human_readable]).to eql("http://linkhum.dev:8080/something.html")
    expect(lu[:url_encoded]).to eql("http://linkhum.dev:8080/something.html")
  end

  it "handles non-ASCII pathnames" do
    lu = Linkhum::URL.parse("https://example.org/пивбар-хмель.html")
    expect(lu[:human_readable]).to eql("https://example.org/пивбар-хмель.html")
    expect(lu[:url_encoded]).to eql("https://example.org/%D0%BF%D0%B8%D0%B2%D0%B1%D0%B0%D1%80-%D1%85%D0%BC%D0%B5%D0%BB%D1%8C.html")
  end

  it "handles percent-encoded pathnames" do
    lu = Linkhum::URL.parse("https://example.org/%D0%BF%D0%B8%D0%B2%D0%B1%D0%B0%D1%80-%D1%85%D0%BC%D0%B5%D0%BB%D1%8C.html")
    expect(lu[:human_readable]).to eql("https://example.org/пивбар-хмель.html")
    expect(lu[:url_encoded]).to eql("https://example.org/%D0%BF%D0%B8%D0%B2%D0%B1%D0%B0%D1%80-%D1%85%D0%BC%D0%B5%D0%BB%D1%8C.html")
  end

  it "handles non-ASCII query strings" do
    lu = Linkhum::URL.parse("https://example.org/search.html?q=пивбар")
    expect(lu[:human_readable]).to eql("https://example.org/search.html?q=пивбар")
    expect(lu[:url_encoded]).to eql("https://example.org/search.html?q=%D0%BF%D0%B8%D0%B2%D0%B1%D0%B0%D1%80")
  end

  it "handles percent-encoded query strings" do
    lu = Linkhum::URL.parse("https://example.org/search.html?q=%D0%BF%D0%B8%D0%B2%D0%B1%D0%B0%D1%80")
    expect(lu[:human_readable]).to eql("https://example.org/search.html?q=пивбар")
    expect(lu[:url_encoded]).to eql("https://example.org/search.html?q=%D0%BF%D0%B8%D0%B2%D0%B1%D0%B0%D1%80")
  end

  it "percent-encodes square brackets in paths" do
    lu = Linkhum::URL.parse("http://www.example.com/image[2].jpg")
    expect(lu[:human_readable]).to eql("http://www.example.com/image[2].jpg")
    expect(lu[:url_encoded]).to eql("http://www.example.com/image%5B2%5D.jpg")
  end

  it "handles non-ASCII fragments" do
    lu = Linkhum::URL.parse("https://example.org/venues.html#пивбар")
    expect(lu[:human_readable]).to eql("https://example.org/venues.html#пивбар")
    expect(lu[:url_encoded]).to eql("https://example.org/venues.html#пивбар")
  end

  it "handles username/password" do
    lu = Linkhum::URL.parse("https://user:pass1@example.org/")
    expect(lu[:human_readable]).to eql("https://user:pass1@example.org/")
    expect(lu[:url_encoded]).to eql("https://user:pass1@example.org/")
  end

  [ # see http://unicode.org/reports/tr15/
    ["NFD", "Çalışma.jpg", "C%CC%A7al%C4%B1s%CC%A7ma.jpg"],
    ["NFC", "Çalışma.jpg", "%C3%87al%C4%B1%C5%9Fma.jpg"]
  ].each do |testcase|
    it "handles Unicode #{testcase[0]}-encoded paths" do
      lu = Linkhum::URL.parse("https://example.org/#{testcase[1]}")
      expect(lu[:human_readable]).to eql("https://example.org/#{testcase[1]}")
      expect(lu[:url_encoded]).to eql("https://example.org/#{testcase[2]}")
    end

    it "handles percent-encoded paths in Unicode #{testcase[0]}" do
      lu = Linkhum::URL.parse("https://example.org/#{testcase[2]}")
      expect(lu[:human_readable]).to eql("https://example.org/#{testcase[1]}")
      expect(lu[:url_encoded]).to eql("https://example.org/#{testcase[2]}")
    end

    it "handles Unicode #{testcase[0]}-encoded query strings" do
      lu = Linkhum::URL.parse("https://example.org/search.html?q=#{testcase[1]}")
      expect(lu[:human_readable]).to eql("https://example.org/search.html?q=#{testcase[1]}")
      expect(lu[:url_encoded]).to eql("https://example.org/search.html?q=#{testcase[2]}")
    end

    it "handles percent-encoded query strings in Unicode #{testcase[0]}" do
      lu = Linkhum::URL.parse("https://example.org/search.html?q=#{testcase[2]}")
      expect(lu[:human_readable]).to eql("https://example.org/search.html?q=#{testcase[1]}")
      expect(lu[:url_encoded]).to eql("https://example.org/search.html?q=#{testcase[2]}")
    end
  end

  it "handles non-UTF8 percent-encoded URLs" do
    lu = Linkhum::URL.parse("http://www.alib.ru/find3.php4?tfind=%EB%EE%F6%E8%FF")
    expect(lu[:human_readable]).to eql("http://www.alib.ru/find3.php4?tfind=%EB%EE%F6%E8%FF")
    expect(lu[:url_encoded]).to eql("http://www.alib.ru/find3.php4?tfind=%EB%EE%F6%E8%FF")
  end

  it "handles Punycode/percent-encoded Devanagari" do
    lu = Linkhum::URL.parse("http://xn--p1b6ci4b4b3a.xn--11b5bs3a9aj6g/%E0%A4%AE%E0%A5%81%E0%A4%96%E0%A5%8D%E0%A4%AF_%E0%A4%AA%E0%A5%83%E0%A4%B7%E0%A5%8D%E0%A4%A0")
    expect(lu[:human_readable]).to eql("http://उदाहरण.परीक्षा/मुख्य_पृष्ठ")
    expect(lu[:url_encoded]).to eql("http://xn--p1b6ci4b4b3a.xn--11b5bs3a9aj6g/%E0%A4%AE%E0%A5%81%E0%A4%96%E0%A5%8D%E0%A4%AF_%E0%A4%AA%E0%A5%83%E0%A4%B7%E0%A5%8D%E0%A4%A0")
  end

  it "handles Devanagari" do
    lu = Linkhum::URL.parse("http://उदाहरण.परीक्षा/मुख्य_पृष्ठ")
    expect(lu[:human_readable]).to eql("http://उदाहरण.परीक्षा/मुख्य_पृष्ठ")
    expect(lu[:url_encoded]).to eql("http://xn--p1b6ci4b4b3a.xn--11b5bs3a9aj6g/%E0%A4%AE%E0%A5%81%E0%A4%96%E0%A5%8D%E0%A4%AF_%E0%A4%AA%E0%A5%83%E0%A4%B7%E0%A5%8D%E0%A4%A0")
  end

  ["%", "#", "?", "&", "+", "[", "]"].each do |char|
    encoded_char = URI.encode_www_form_component(char)

    it "handles percent-encoded #{char} symbol in path" do
      url = "http://example.com/#{encoded_char}"
      lu = Linkhum::URL.parse(url)
      expect(lu[:human_readable]).to eql("http://example.com/#{char}")
      expect(lu[:url_encoded]).to eql("http://example.com/#{encoded_char}")
    end

    it "handles percent-encoded #{char} symbol in query" do
      url = "http://example.com/?query=#{encoded_char}"
      lu = Linkhum::URL.parse(url)
      expect(lu[:human_readable]).to eql("http://example.com/?query=#{char}")
      expect(lu[:url_encoded]).to eql("http://example.com/?query=#{encoded_char}")
    end
  end

  it "accepts an instance of Addressable" do
    uri = Addressable::URI.parse("https://github.com/sporkmonger/addressable")
    lu = Linkhum::URL.parse(uri)
    expect(lu[:human_readable]).to eql("https://github.com/sporkmonger/addressable")
    expect(lu[:url_encoded]).to eql("https://github.com/sporkmonger/addressable")
  end
end
