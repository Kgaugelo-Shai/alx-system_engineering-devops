# Puppet script

exec { 'apt-get-update':
  command => '/usr/bin/apt-get update',
}

package { 'nginx':
  ensure  => installed,
  require => Exec['apt-get-update'],
}

file { '/var/www/html/index.html':
  content => 'Hello World!',
  require => Package['nginx'],
}

exec {'redirect_me':
  command  => 'sed -i "24i\	rewrite ^/redirect_me https://github/Kgaugelo-Shai permanent;" /etc/nginx/sites-available/default',
  provider => 'shell'
}

service { 'nginx':
  ensure  => running,
  require => Package['nginx'],
}
    
