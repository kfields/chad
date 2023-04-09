import os

from ariadne import (
    load_schema_from_path,
    make_executable_schema,
    snake_case_fallback_resolvers,
)

from .types import types
from .resolvers import *

type_defs = load_schema_from_path(
    os.path.join(os.path.dirname(__file__), "schemas")
)

schema = make_executable_schema(type_defs, types, snake_case_fallback_resolvers)
