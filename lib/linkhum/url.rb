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

      human_readable[:path] = Addressable::URI.unencode_component(au.path)
      # this code handles bug in Addressable::URI (up to 2.5.0), which
      # converts paths to Unicode NFKC (it should only do that for
      # hostnames).  Patch to Addressable::URI pending.
      au_path = au.path.dup
      if au_path =~ /\A[\x00-\x7F]*\z/
        au_path = Addressable::URI.unencode_component(au_path)
      end
      au_path.force_encoding(Encoding::ASCII_8BIT)
      url_encoded[:path] = Addressable::URI.encode_component(au_path)

      human_readable[:query] = Addressable::URI.unencode_component(au.query)
      if au.query
        decoded_query = human_readable[:query].dup
        if !decoded_query.force_encoding(Encoding::UTF_8).valid_encoding?
          human_readable[:query] = au.query
        end
      end

      if au.query
        # see above
        au_query = au.query.dup
        if au_query =~ /\A[\x00-\x7F]*\z/
          au_query = Addressable::URI.unencode_component(au_query)
        end
        au_query.force_encoding(Encoding::ASCII_8BIT)
      end
      url_encoded[:query] = Addressable::URI.encode_component(au_query)

      # fragments do not need to be encoded
      human_readable[:fragment] = au.fragment
      url_encoded[:fragment] = au.fragment

      { human_readable: generate_url(human_readable),
        url_encoded: generate_url(url_encoded) }
    end

    private
    def self.generate_url(parts)
      userinfo_part = parts[:userinfo] ? "#{parts[:userinfo]}@" : ""
      query_part = parts[:query] ? "?#{parts[:query]}" : ""
      fragment_part = parts[:fragment] ? "##{parts[:fragment]}" : ""
      "#{parts[:scheme]}://#{userinfo_part}#{parts[:host]}#{parts[:path]}#{query_part}#{fragment_part}"
    end
  end
end
