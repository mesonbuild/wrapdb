#!/usr/bin/env python3

# Copyright 2025 Benjamin Gilbert <bgilbert@backtick.net>

# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at

#     https://www.apache.org/licenses/LICENSE-2.0

# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

import json
import os
import sys
import yaml
import typing as T

UPSTREAM_OWNER = 'mesonbuild'

with open(sys.argv[1]) as f:
    jobs: list[dict[str, T.Any]] = yaml.safe_load(f)

if os.environ['GITHUB_REPOSITORY_OWNER'] != UPSTREAM_OWNER:
    jobs = [j for j in jobs if not j.get('selfhosted', False)]

with open(os.environ['GITHUB_OUTPUT'], 'a') as f:
    f.write('matrix=')
    json.dump(jobs, f, separators=(',', ':'))
    f.write('\n')
