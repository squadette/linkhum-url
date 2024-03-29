Gem::Specification.new do |s|
  s.name        = 'linkhum-url'
  s.version     = '0.1.9'
  s.date        = '2023-01-07'
  s.summary     = "Linkhum-URL creates both URL-encoded and readable versions of URLs"
  s.description = "Input URL could be either human-readable, or URL-encoded.  Two URLs are returned as result: human-readable and URL-encoded."
  s.authors     = ["Alexey Makhotkin"]
  s.email       = 'squadette@gmail.com'
  s.files       = ["lib/linkhum/url.rb", "lib/linkhum-url.rb", "LICENSE.txt", "README.md", "CHANGELOG.md" ]
  s.homepage    = 'http://rubygems.org/gems/linkhum-url'
  s.license     = 'MIT'

  s.required_ruby_version = '>= 2.00'
  s.add_runtime_dependency "addressable", "~> 2.0"
  s.add_runtime_dependency "idn-ruby", "~> 0.1.0"
  s.add_development_dependency "rake", "~> 10.0"
  s.add_development_dependency "rspec", "~> 3.0"
  s.add_development_dependency "json", "~> 2.6.0"
end
