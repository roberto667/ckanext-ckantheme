import ckan.plugins as p
import ckan.plugins.toolkit as toolkit
import ckan.lib.helpers as h


def most_popular_groups():
    '''Return a sorted list of the groups with the most datasets.'''
    # Get a list of all the site's groups from CKAN, sorted by number of
    # datasets.
    groups = toolkit.get_action('group_list')(
        data_dict={'sort': 'packages desc', 'all_fields': True})

    return groups
