# coding: utf-8
require 'spec_helper' # -*- ruby -*- 

describe Linkhum::URL do
  it "handles ASCII-only URLs" do
    lu = Linkhum::URL.parse("https://example.org/foobar.html?q=baz#anchor")
    expect(lu[:human_readable]).to eql("https://example.org/foobar.html?q=baz#anchor")
    expect(lu[:url_encoded]).to eql("https://example.org/foobar.html?q=baz#anchor")
  end

  it "handles IDNs" do
    lu = Linkhum::URL.parse("https://пивбар.рф/")
    expect(lu[:human_readable]).to eql("https://пивбар.рф/")
    expect(lu[:url_encoded]).to eql("https://xn--80abcx8ak.xn--p1ai/")
  end

  it "handles Punycode hostnames" do
    lu = Linkhum::URL.parse("https://xn--80abcx8ak.xn--p1ai/")
    expect(lu[:human_readable]).to eql("https://пивбар.рф/")
    expect(lu[:url_encoded]).to eql("https://xn--80abcx8ak.xn--p1ai/")
  end

  it "handles non-ASCII pathnames" do
    lu = Linkhum::URL.parse("https://example.org/пивбар.html")
    expect(lu[:human_readable]).to eql("https://example.org/пивбар.html")
    expect(lu[:url_encoded]).to eql("https://example.org/%D0%BF%D0%B8%D0%B2%D0%B1%D0%B0%D1%80.html")
  end

  it "handles percent-encoded pathnames" do
    lu = Linkhum::URL.parse("https://example.org/%D0%BF%D0%B8%D0%B2%D0%B1%D0%B0%D1%80.html")
    expect(lu[:human_readable]).to eql("https://example.org/пивбар.html")
    expect(lu[:url_encoded]).to eql("https://example.org/%D0%BF%D0%B8%D0%B2%D0%B1%D0%B0%D1%80.html")
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


end
