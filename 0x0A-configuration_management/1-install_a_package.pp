#!/usr/bin/pup
# Install a version of flask (2.1.0) using pip3
exec {'install_flask':
  command => '/usr/bin/pip3 install flask==2.1.0',
  unless  => '/usr/bin/pip3 show flask | grep -q "version: 2.1.0"'
}
