from __future__ import unicode_literals

from mopidy import config, ext

__version__ = '0.3.1'


class Extension(ext.Extension):

    dist_name = 'Mopidy-Local-SQLite'
    ext_name = 'local-sqlite'
    version = __version__

    def get_default_config(self):
        import os
        conf_file = os.path.join(os.path.dirname(__file__), 'ext.conf')
        return config.read(conf_file)

    def get_config_schema(self):
        schema = super(Extension, self).get_config_schema()
        schema['hash'] = config.String()
        schema['use_album_mbid_uri'] = config.Boolean()
        schema['use_artist_mbid_uri'] = config.Boolean()
        schema['foreign_keys'] = config.Boolean()
        schema['timeout'] = config.Integer(optional=True, minimum=1)
        schema['extract_images'] = config.Boolean()
        schema['image_dir'] = config.String()
        schema['image_base_uri'] = config.String(optional=True)
        schema['default_image_extension'] = config.String(optional=True)
        return schema

    def setup(self, registry):
        from .library import SQLiteLibrary
        registry.add('local:library', SQLiteLibrary)