# install flask using pip3

package { 'flask':
    ensure   => '2.1.0',
    name     => 'flask',
    provider => 'pip3'
}

package { 'werkzeug':
    ensure   => '1.0.1',
    name     => 'Werkzeug',
    provider => 'pip3',
    require  => Package['flask'],
}

