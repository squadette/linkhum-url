Gem::Specification.new do |s|
  s.name        = 'linkhum-url'
  s.version     = '0.1.6'
  s.date        = '2017-10-17'
  s.summary     = "Linkhum-URL creates both URL-encoded and readable versions of URLs"
  s.description = "Input URL could be either human-readable, or URL-encoded.  Two URLs are returned as result: human-readable and URL-encoded."
  s.authors     = ["Alexey Makhotkin"]
  s.email       = 'squadette@gmail.com'
  s.files       = ["lib/linkhum/url.rb", "lib/linkhum-url.rb", "LICENSE.txt", "README.md", "CHANGELOG.md" ]
  s.homepage    = 'http://rubygems.org/gems/linkhum-url'
  s.license     = 'MIT'

  s.required_ruby_version = '~> 2.0'
  s.add_runtime_dependency "addressable", "~> 2.0"
  s.add_runtime_dependency "idn-ruby", "~> 0.1.0"
  s.add_development_dependency "rake", "~> 10.0"
  s.add_development_dependency "rspec", "~> 3.0"
  s.add_development_dependency "travis", "~> 1.8"
end
