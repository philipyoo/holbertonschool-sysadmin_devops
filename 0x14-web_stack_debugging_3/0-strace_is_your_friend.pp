# Use strace to find out why Apache is returning a 500 error
exec { 'fix-apache':
  command => "sed -i 's/phpp/php/g' /var/www/html/wp-settings.php",
  path    => ['/usr/bin', '/usr/sbin', '/bin']
}
