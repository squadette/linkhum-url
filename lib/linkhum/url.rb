module Linkhum
  class URL
    require 'addressable'
    require 'idn'

    include IDN

    def self.parse(url)
      au = Addressable::URI.parse(url)
      human_readable = { scheme: au.scheme, userinfo: au.userinfo }
      url_encoded = { scheme: au.scheme, userinfo: au.userinfo }

      if au.host =~ /\bxn--/
        human_readable[:host] = Idna.toUnicode(au.host)
      else
        human_readable[:host] = au.host
      end
      url_encoded[:host] = au.normalized_host

      url_encoded[:port] = au.port ? ":#{au.port}" : ""
      human_readable[:port] = url_encoded[:port]

      human_readable[:path] = unencode_component(au.path, false)
      # this code handles bug in Addressable::URI (up to 2.5.0), which
      # converts paths to Unicode NFKC (it should only do that for
      # hostnames).  Patch to Addressable::URI pending.
      au_path = au.path.dup
      if au_path =~ /\A[\x00-\x7F]*\z/
        au_path = unencode_component(au_path)
      end
      au_path.force_encoding(Encoding::ASCII_8BIT)
      url_encoded[:path] = encode_component(au_path)
      decoded_path = human_readable[:path].dup
      if !decoded_path.force_encoding(Encoding::UTF_8).valid_encoding?
          human_readable[:path] = au.path
      end

      human_readable[:query] = unencode_component(au.query, false)
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
          au_query = unencode_component(au_query)
        end
        au_query.force_encoding(Encoding::ASCII_8BIT)
      end
      url_encoded[:query] = encode_component(au_query)

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
      "#{parts[:scheme]}://#{userinfo_part}#{parts[:host]}#{parts[:port]}#{parts[:path]}#{query_part}#{fragment_part}"
    end

    def self.encode_component(string, skip_percent_sign = true)
      chars_to_keep_unencoded = "\\:\\/\\?\\#\\@\\!\\$\\&\\'\\(\\)\\*\\+\\,\\;\\=" + Addressable::URI::CharacterClasses::UNRESERVED
      chars_to_keep_unencoded << '\\%' if skip_percent_sign
      Addressable::URI.encode_component(string, chars_to_keep_unencoded)
    end

    def self.unencode_component(string, skip_special_chars = true)
      chars_to_keep_encoded = skip_special_chars ? "%#&?+[]" : ""
      Addressable::URI.unencode_component(string, String, chars_to_keep_encoded)
    end
  end
end
