import ckan.plugins as p
import ckan.plugins.toolkit as toolkit


class CkanthemePlugin(p.SingletonPlugin):
    p.implements(p.IConfigurer, inherit=True)
    p.implements(p.ITemplateHelpers)

    # IConfigurer

    def update_config(self, config):
        config['ckan.site_title'] = 'OBEMI'
        config['ckan.locale_default'] = 'pt_BR'

        # Add this plugin's templates dir to CKAN's extra_template_paths, so
        # that CKAN will use this plugin's custom templates.
        # 'templates' is the path to the templates dir, relative to this
        # plugin.py file.
        p.toolkit.add_template_directory(config, 'templates')
        p.toolkit.add_public_directory(config, 'public')
        p.toolkit.add_resource('fanstatic',
            'ckantheme')
        p.toolkit.add_resource('assets', 'ckantheme')
        p.toolkit.add_public_directory(config, 'assets/')

    def get_helpers(self):
        from ckanext.ckantheme import helpers as ckantheme_helpers
        return{
            'most_popular_groups': ckantheme_helpers.most_popular_groups
        }
