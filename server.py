#!/usr/bin/env python
import web
import json
from subprocess import call




urls = (
    '/users', 'list_users',
    '/users/(.*)', 'get_user',
    '/playbook/run', 'run_playbook'
)

app = web.application(urls, globals())

class run_playbook:
    def POST(self):
        data = web.data()
        data = json.loads(data)
        fname=data["file"]
        call(["ansible-playbook", fname])
        
    def GET(self):
        print("GET")


class list_users:        
    def GET(self):
	output = 'users:[';
	for child in root:
                print 'child', child.tag, child.attrib
                output += str(child.attrib) + ','
	output += ']';
        return output

class get_user:
    def GET(self, user):
	for child in root:
		if child.attrib['id'] == user:
		    return str(child.attrib)

if __name__ == "__main__":
    app.run()
