# Install puppet-lint
package { 'puppet-lint':
  ensure   => 'latest',
  name     => 'puppet-lint',
  provider => 'gem'
}
