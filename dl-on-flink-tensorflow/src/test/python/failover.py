#  Copyright 2022 Deep Learning on Flink Authors
#
#  Licensed under the Apache License, Version 2.0 (the "License");
#  you may not use this file except in compliance with the License.
#  You may obtain a copy of the License at
#
#      http://www.apache.org/licenses/LICENSE-2.0
#
#  Unless required by applicable law or agreed to in writing, software
#  distributed under the License is distributed on an "AS IS" BASIS,
#  WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
#  See the License for the specific language governing permissions and
#  limitations under the License.

import sys
import time
import traceback
import logging
import logging.config


def map_func(context):
    key = context.identity
    index = context.index
    fail_num = context.get_current_attempt_index()
    logging.info(key + " fail num: " + str(fail_num))
    sys.stdout.flush()
    if 1 == index and fail_num < 2:
        time.sleep(5)
        logging.info(key + " failover!")
        sys.stdout.flush()
        raise Exception("fail over!")

    for i in range(5):
        logging.info(key + " run num: " + str(i))
        sys.stdout.flush()
        time.sleep(5)


if __name__ == "__main__":
    pass
