# 0x19. Application server

## Notes:

In order to setup virtualenv (after installation):
`$ virutalenv <name_env>`

To activate virtualenv previously setup:
`$ source <name_env>/bin/activate`

Use Gunicorn to serve the project:
`$ gunicorn --bind 0.0.0.0:<port> <path_to_flask_route_file>:<name_of_Flask_instance>`
[i.e.] `$ gunicorn --bind 0.0.0.0:8001 web_flask.0-hello_route:app`

Once Gunicorn is serving a specific route/project:
`$ curl 0.0.0.0:8001/`

Above is an example of manually binding port with route, but setting up nginx to listen to the port/route:
1. Setup upstart file. i.e. 0-welcome_gunicorn-upstart_config
2. Setup nginx conf file. i.e. 0-welcome_gunicorn-nginx_config
3. `$ sudo service nginx restart`
4. `$ sudo service <name> start`
5. `$ curl http://0.0.0.0:<port>`

Directory to save the upstart file:
`/etc/init/<project_name>.conf`

Directory to save the nginx conf file:
`/etc/nginx/sites-available/<project_name>`

The nginx conf file must be linked to the `sites-enabled` dir (make sure to restart nginx after doing this):
`$ sudo ln -s /etc/nginx/sites-available/<project_name> /etc/nginx/sites-enabled`
