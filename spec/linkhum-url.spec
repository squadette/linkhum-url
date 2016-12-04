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
end
