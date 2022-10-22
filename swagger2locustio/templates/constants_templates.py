"""Module: constants templates"""

from jinja2 import Template

CONSTANTS_BASE_FILE = Template(
    """from apps.helper import Helper

API_PREFIX = ""

"""
)

CONSTANTS_FILE = Template(
    """from apps.helper import Helper

{% for const in constants %}# value type -> {{ const.type }}
{{ const.name }} = [{{ const.val }}]
{% endfor %}
"""
)
