# Create a file in the /tmp directory

# Ensure the directory exists
file { '/tmp':
  ensure => directory,
}

# CReate the file with specified content, permissions, owner, and group
file { '/tmp/school':
  ensure  => file,
  content => 'I love Puppet',
  mode    => '0744',
  owner   => 'www-data',
  group   => 'www-data',
}
