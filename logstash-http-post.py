#!/usr/bin/env python

# Copyright 2015 Google Inc. All rights reserved.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

import os
import uuid

from datetime import datetime
from locust import HttpLocust, TaskSet, task

json = os.environ.get("JSON") 

class MetricsTaskSet(TaskSet):

    @task
    def post_metrics(self):
        self.client.post("/", json, verify=False)
 

class MetricsLocust(HttpLocust):
    task_set = MetricsTaskSet
#    min_wait = 10
#    max_wait = 250
