# coding: utf-8
require 'spec_helper' # -*- ruby -*- 

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

  it "handles non-ASCII fragments" do
    lu = Linkhum::URL.parse("https://example.org/venues.html#пивбар")
    expect(lu[:human_readable]).to eql("https://example.org/venues.html#пивбар")
    expect(lu[:url_encoded]).to eql("https://example.org/venues.html#пивбар")
  end

  unicode_path = "Çalışma.jpg" # see http://unicode.org/reports/tr15/
  [
    ["NFD", unicode_path.unicode_normalize(:nfd), "C%CC%A7al%C4%B1s%CC%A7ma.jpg"],
    ["NFC", unicode_path.unicode_normalize(:nfc), "%C3%87al%C4%B1%C5%9Fma.jpg"]
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

end
