# Puppet manifest to set file limits for holberton user
file_line { 'set nofile limit for holberton':
  path  => '/etc/security/limits.conf',
  line  => 'holberton soft nofile 4096',
  match => '^holberton.*nofile',
}

file_line { 'set hard nofile limit for holberton':
  path  => '/etc/security/limits.conf',
  line  => 'holberton hard nofile 4096',
  match => '^holberton.*nofile',
}
