# -*- coding: utf-8 -*-


from __future__ import absolute_import
from dp_tornado.engine.helper import Helper as dpHelper

import time
import datetime as abs_datetime


class DatetimeHelper(dpHelper):
    def now(self, timezone=None):
        return abs_datetime.datetime.now(tz=timezone)

    def from_datetime(self, datetime, timezone=None):
        if not timezone:
            return datetime

        if not datetime.tzinfo:
            return self.helper.datetime.timezone.localize(datetime=datetime, timezone=timezone)
        else:
            return self.helper.datetime.timezone.normalize(datetime=datetime, timezone=timezone)

    def from_timestamp(self, timestamp, timezone=None, ms=False):
        timestamp = self.helper.numeric.cast.long(timestamp)

        # TZ Info from Zone
        if timezone and self.helper.misc.type.check.string(timezone):
            timezone = self.helper.datetime.timezone.tzinfo_from_zone(timezone)

        if ms:  # with microseconds
            datetime = abs_datetime.datetime.fromtimestamp(timestamp // 1000, tz=timezone)
            datetime = datetime.replace(microsecond=timestamp % 1000 * 1000)
            return datetime
        else:
            return abs_datetime.datetime.fromtimestamp(timestamp, tz=timezone)

    def convert(self, datetime=None, timezone=None, timestamp=None, ms=False):
        if isinstance(datetime, abs_datetime.datetime):
            if timezone:
                datetime = self.from_datetime(datetime=datetime, timezone=timezone)
        elif timestamp:
            if self.helper.misc.type.check.numeric(timestamp):
                datetime = self.from_timestamp(timestamp=timestamp, timezone=timezone, ms=ms)
            else:
                raise Exception('The specified timestamp value is invalid.')
        elif not datetime:
            datetime = self.now(timezone=timezone)
        else:
            raise Exception('The specified datetime value is invalid.')

        return datetime

    def tuple(self, datetime=None, timezone=None, timestamp=None, ms=False):
        datetime = self.convert(datetime=datetime, timezone=timezone, timestamp=timestamp, ms=ms)
        time_set = [datetime.year, datetime.month, datetime.day, datetime.hour, datetime.minute, datetime.second]

        if ms:
            time_set.append(datetime.microsecond)

        if datetime.tzinfo:
            time_set.append(self.helper.datetime.timezone.zone_from_tzinfo(datetime.tzinfo))

        return time_set
