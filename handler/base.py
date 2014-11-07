# -*- coding:utf-8 -*-
import tornado.web

class BaseHandler(tornado.web.RequestHandler):
    @property
    def env(self):
        return self.application.env

    @property
    def db(self):
        return self.application.db

    def render(self, template_name, **kwargs):
        if kwargs.get('jinja2'):
            template = self.env.get_template(template_name)
            self.write(template.render(kwargs))
        else:
            super().render(template_name, **kwargs)

    def prepare(self):
        pass

    def write_error(self, status_code, **kwargs):
        super().write_error(status_code, **kwargs)
        if self.settings.get("serve_traceback") and "exc_info" in kwargs:
            try:
                import ipdb as pdb
            except:
                import pdb
            pdb.post_mortem(kwargs['exc_info'][2])
