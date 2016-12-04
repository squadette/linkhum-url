module Linkhum
  class URL

    def self.parse(url)
      { human_readable: url,
        url_encoded: url }
    end
  end
end
