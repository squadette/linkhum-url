Gem::Specification.new do |s|
  s.name        = 'linkhum-url'
  s.version     = '0.1.1'
  s.date        = '2016-12-04'
  s.summary     = "Linkhum-URL creates both URL-encoded and readable versions of URLs"
  s.description = "Input URL could be both human-readable and URL-encoded.  Two URLs are returned as result: human-readable and URL-encoded"
  s.authors     = ["Alexey Makhotkin"]
  s.email       = 'squadette@gmail.com'
  s.files       = ["lib/linkhum/url.rb", "lib/linkhum-url.rb", "LICENSE.txt", "README.md", "CHANGELOG.md" ]
  s.homepage    = 'http://rubygems.org/gems/linkhum-url'
  s.license     = 'MIT'
  s.add_runtime_dependency "addressable", "~> 2.0"
  s.add_runtime_dependency "idn-ruby", "~> 0.1.0"
  s.add_development_dependency "rake", ">= 10.0.0"
  s.add_development_dependency "rspec", "~> 3.0"
end
