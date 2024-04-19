# Install Flask package using pip3

package { 'Flask':
  ensure   => '2.1.0',
  provider => 'pip3',
  require  => Package['python3-pip'], # Ensure that pip3 is installed
}

package { 'Werkzeug':
  ensure   => '2.1.1',
  provider => 'pip3',
  require  => Package['python3-pip']
}

# Ensure that python3-pip is installed
package {'python3-pip':
  ensure => installed,
}
