# kills a process called killmenow using exec

exec { 'pkill killmenow':
  path => '/usr/bin:/usr/sbin:/bin'
}
