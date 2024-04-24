# ssh config

file_line { 'Remove passwd auth.':
  path => '/etc/ssh/ssh_config',
  line => 'PasswordAuthentication no'
}

file_line {'Configure private key use':
  path => '/etc/ssh/ssh_config',
  line => 'IdentityFile ~/.ssh/school'
}
