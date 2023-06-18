import ckan.plugins as p
import ckan.plugins.toolkit as toolkit


class CkanthemePlugin(p.SingletonPlugin):
    p.implements(p.IConfigurer, inherit=True)

    # IConfigurer

    def update_config(self, config):

        # Add this plugin's templates dir to CKAN's extra_template_paths, so
        # that CKAN will use this plugin's custom templates.
        # 'templates' is the path to the templates dir, relative to this
        # plugin.py file.
        p.toolkit.add_template_directory(config, 'templates')
        p.toolkit.add_public_directory(config, 'public')
        p.toolkit.add_resource('fanstatic',
            'ckantheme')
        p.toolkit.add_resource('assets', 'ckantheme')
