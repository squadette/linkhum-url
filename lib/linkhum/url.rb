module Linkhum
  class URL
    require 'addressable'
    require 'idn'

    include IDN

    def self.parse(url)
      au = Addressable::URI.parse(url)
      human_readable = { scheme: au.scheme, userinfo: au.userinfo }
      url_encoded = { scheme: au.scheme, userinfo: au.userinfo }

      if au.host =~ /\Axn--/
        human_readable[:host] = Idna.toUnicode(au.host)
      else
        human_readable[:host] = au.host
      end
      url_encoded[:host] = au.normalized_host

      human_readable[:path] = au.path
      url_encoded[:path] = au.path

      human_readable[:query] = au.query
      url_encoded[:query] = au.query

      human_readable[:fragment] = au.fragment
      url_encoded[:fragment] = au.fragment

      { human_readable: generate_url(human_readable),
        url_encoded: generate_url(url_encoded) }
    end

    private
    def self.generate_url(parts)
      query_part = parts[:query] ? "?#{parts[:query]}" : ""
      fragment_part = parts[:fragment] ? "##{parts[:fragment]}" : ""
      "#{parts[:scheme]}://#{parts[:userinfo]}#{parts[:host]}#{parts[:path]}#{query_part}#{fragment_part}"
    end
  end
end
