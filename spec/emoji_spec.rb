# coding: utf-8  # -*- ruby -*-
require 'spec_helper'

describe Linkhum::URL do
  it "handles emoji domains" do
    lu = Linkhum::URL.parse("https://🤖👊.ws/")
    expect(lu[:human_readable]).to eql("https://🤖👊.ws/")
    expect(lu[:url_encoded]).to eql("https://xn--vp8hx0f.ws/")
  end

  it "handles Punycode/percent-encoded emoji domains" do
    pending "ruby-idn does not support Emoji domains"
    lu = Linkhum::URL.parse("https://xn--vp8hx0f.ws/")
    expect(lu[:human_readable]).to eql("https://🤖👊.ws/")
    expect(lu[:url_encoded]).to eql("https://xn--vp8hx0f.ws/")
  end
end
