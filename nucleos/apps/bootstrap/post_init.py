from __future__ import absolute_import

import datetime

from django.utils.timezone import now

from nucleos import __version__
from navigation.api import register_links

from .classes import FixtureMetadata
from .links import (link_bootstrap_setup_create, link_bootstrap_setup_execute,
    link_bootstrap_setup_list, link_bootstrap_setup_edit, link_bootstrap_setup_delete,
    link_bootstrap_setup_view, link_bootstrap_setup_dump, link_bootstrap_setup_export,
    link_bootstrap_setup_import_from_url, link_bootstrap_setup_import_from_file,
    link_bootstrap_setup_repository_sync)
from .literals import (FIXTURE_METADATA_CREATED, FIXTURE_METADATA_EDITED,
    FIXTURE_METADATA_nucleos_VERSION, FIXTURE_METADATA_FORMAT, FIXTURE_METADATA_NAME,
    FIXTURE_METADATA_DESCRIPTION, DATETIME_STRING_FORMAT, FIXTURE_METADATA_SLUG)
from .models import BootstrapSetup

register_links([BootstrapSetup], [link_bootstrap_setup_view, link_bootstrap_setup_edit, link_bootstrap_setup_delete, link_bootstrap_setup_execute, link_bootstrap_setup_export])
register_links([BootstrapSetup], [link_bootstrap_setup_list, link_bootstrap_setup_create, link_bootstrap_setup_dump, link_bootstrap_setup_import_from_file, link_bootstrap_setup_import_from_url, link_bootstrap_setup_repository_sync], menu_name='secondary_menu')
register_links(['bootstrap_setup_list', 'bootstrap_setup_create', 'bootstrap_setup_dump', 'bootstrap_setup_import_from_file', 'bootstrap_setup_import_from_url', 'bootstrap_setup_repository_sync'], [link_bootstrap_setup_list, link_bootstrap_setup_create, link_bootstrap_setup_dump, link_bootstrap_setup_import_from_file, link_bootstrap_setup_import_from_url, link_bootstrap_setup_repository_sync], menu_name='secondary_menu')

FixtureMetadata(FIXTURE_METADATA_CREATED, generate_function=lambda fixture_instance: fixture_instance.created.strftime(DATETIME_STRING_FORMAT), read_function=lambda x: datetime.datetime.strptime(x, DATETIME_STRING_FORMAT), property_name='created')
FixtureMetadata(FIXTURE_METADATA_EDITED, generate_function=lambda fixture_instance: now().strftime(DATETIME_STRING_FORMAT))
FixtureMetadata(FIXTURE_METADATA_nucleos_VERSION, generate_function=lambda fixture_instance: __version__)
FixtureMetadata(FIXTURE_METADATA_FORMAT, generate_function=lambda fixture_instance: fixture_instance.type, property_name='type')
FixtureMetadata(FIXTURE_METADATA_NAME, generate_function=lambda fixture_instance: fixture_instance.name, property_name='name')
FixtureMetadata(FIXTURE_METADATA_SLUG, generate_function=lambda fixture_instance: fixture_instance.slug, property_name='slug')
FixtureMetadata(FIXTURE_METADATA_DESCRIPTION, generate_function=lambda fixture_instance: fixture_instance.description, property_name='description')
