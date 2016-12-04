require 'spec_helper' # -*- ruby -*- 

describe Linkhum::URL do
  it "handles ASCII-only URLs" do
    lu = Linkhum::URL.parse("https://example.org/foobar.html?q=baz#anchor")
    expect(lu[:human_readable]).to eql("https://example.org/foobar.html?q=baz#anchor")
    expect(lu[:url_encoded]).to eql("https://example.org/foobar.html?q=baz#anchor")
  end
end
