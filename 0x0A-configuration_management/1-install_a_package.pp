# Install a package using puppet
class { 'python':
  version => '3',
}

python::pyvenv { '/opt/myenv':
  ensure   => 'present',
  version  => '3',
  pip      => 'present',
  systempkgs => 'false',
  owner    => 'root',
  group    => 'root',
}

python::pip { 'flask':
  ensure  => '2.1.0',
  virtualenv => '/opt/myenv',
  pip_provider => 'pip3',
}
