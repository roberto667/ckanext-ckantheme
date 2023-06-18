import ckan.plugins as p
from ckan.plugins import toolkit as tk


class CkanthemePlugin(p.SingletonPlugin):
    p.implements(p.IConfigurer, inherit=True)

    # IConfigurer

    def update_config(self, config):

        # Add this plugin's templates dir to CKAN's extra_template_paths, so
        # that CKAN will use this plugin's custom templates.
        # 'templates' is the path to the templates dir, relative to this
        # plugin.py file.
        tk.add_template_directory(config, 'templates')
        tk.add_public_directory(config, 'public')
        tk..add_resource('fanstatic',
            'ckantheme')
        tk.add_resource('assets', 'ckantheme')
        tk.add_public_directory(config, 'assets/')
