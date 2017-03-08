from __future__ import unicode_literals

import datetime
import os
import subprocess
from functools import lru_cache

from utils.date import ChinaTz


def get_version(version):
    """Returns a PEP 386-compliant version number from VERSION."""
    assert len(version) == 5
    assert version[3] in ('alpha', 'beta', 'rc', 'final')

    # Now build the two parts of the version number:
    # major = X.Y[.Z]
    # sub = .devN - for pre-alpha releases
    #     | {a|b|c}N - for alpha, beta and rc releases

    major = get_major_version(version)

    sub = ''
    if version[3] == 'alpha' and version[4] == 0:
        git_changeset = get_git_changeset()
        if git_changeset:
            sub = '.dev%s' % git_changeset

    elif version[3] != 'final':
        mapping = {'alpha': 'a', 'beta': 'b', 'rc': 'c'}
        sub = mapping[version[3]] + str(version[4])

    return str(major + sub)


def get_major_version(version):
    """Returns major version from VERSION."""
    parts = 2 if version[2] == 0 else 3
    major = '.'.join(str(x) for x in version[:parts])
    return major


@lru_cache()
def get_git_changeset():
    """Returns a numeric identifier of the latest git changeset.

    The result is the Utc timestamp of the changeset in YYYYMMDDHHMMSS format.
    This value isn't guaranteed to be unique, but collisions are very unlikely,
    so it's sufficient for generating the development version numbers.
    """
    repo_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    git_log = subprocess.Popen('git log --pretty=format:%ct --quiet -1 HEAD',
                               stdout=subprocess.PIPE, stderr=subprocess.PIPE,
                               shell=True, cwd=repo_dir,
                               universal_newlines=True)
    timestamp = git_log.communicate()[0]
    try:
        timestamp = datetime.datetime.fromtimestamp(timestamp=int(timestamp),
                                                    tz=ChinaTz())
    except ValueError:
        return None
    return timestamp.strftime('%Y%m%d%H%M%S')
