import pathlib

import click
import flac.app
import flac.cli

import {{cookiecutter.project_namespace}}.cli
import {{cookiecutter.project_namespace}}.ext
import {{cookiecutter.project_namespace}}.views

app_dpath = pathlib.Path(__file__).parent


class {{cookiecutter.project_class}}App(flac.app.FlacApp):
    @classmethod
    def create(cls, **kwargs):
        return super().create('{{cookiecutter.project_namespace}}', app_dpath, **kwargs)

    def init_blueprints(self):
        self.register_blueprint({{cookiecutter.project_namespace}}.cli.cli_bp)
        self.register_blueprint({{cookiecutter.project_namespace}}.views.public)

    def on_app_ready(self):
        {{cookiecutter.project_namespace}}.ext.init_ext(self)


@flac.cli.cli_entry({{cookiecutter.project_class}}App)
@click.option('--with-sentry', is_flag=True, default=False,
    help='Enable Sentry (usually only in production)')
def cli(scriptinfo, log_level, with_sentry):
    app = scriptinfo.load_app()
    app.init_app(log_level, with_sentry=with_sentry)
