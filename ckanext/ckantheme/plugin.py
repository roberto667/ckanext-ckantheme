from ckan.common import CKANConfig
import ckan.plugins as plugins
import ckan.plugins.toolkit as toolkit


class CkanthemePlugin(plugins.SingletonPlugin):
    plugins.implements(plugins.IConfigurer)

    # IConfigurer

    def update_config(self, config: CKANConfig):
        toolkit.add_template_directory(config_, 'templates')
        toolkit.add_public_directory(config_, 'public')
        toolkit.add_resource('fanstatic',
            'ckantheme')
        toolkit.add_resource('assets', 'ckantheme')
