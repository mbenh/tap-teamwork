import singer

from tap_teamwork.base import BaseStream, TimeRangeByObjectStream


LOGGER = singer.get_logger()


class CompaniesStream(BaseStream):
    TABLE = "companies"
    RESPONSE_KEY = "companies"

    CACHE_RESULTS = True

    @property
    def path(self):
        return f"companies.json"

    # The 'companies' endpoint is only in API version 1, so requires a different base
    def get_url_base(self):
        return self.config["hostname"] + "/"


class LatestActivityStream(BaseStream):
    TABLE = "latest_activity"
    RESPONSE_KEY = "activities"

    CACHE_RESULTS = True

    @property
    def path(self):
        return f"latestactivity.json"


class MilestonesStream(BaseStream):
    TABLE = "milestones"
    RESPONSE_KEY = "milestones"

    CACHE_RESULTS = True

    @property
    def path(self):
        return "milestones.json"


class ProjectsStream(BaseStream):
    TABLE = "projects"
    RESPONSE_KEY = "projects"

    @property
    def path(self):
        return f"projects.json"


class PeopleStream(BaseStream):
    TABLE = "people"
    RESPONSE_KEY = "people"

    CACHE_RESULTS = True

    @property
    def path(self):
        return f"people.json"


class ProjectUpdatesStream(BaseStream):
    TABLE = "project_updates"
    RESPONSE_KEY = "projectUpdates"

    CACHE_RESULTS = True

    @property
    def path(self):
        return "projects/updates.json"


class RisksStream(BaseStream):
    TABLE = "risks"
    RESPONSE_KEY = "risks"

    CACHE_RESULTS = True

    @property
    def path(self):
        return f"risks.json"


class TagsStream(BaseStream):
    TABLE = "tags"
    RESPONSE_KEY = "tags"

    CACHE_RESULTS = True

    @property
    def path(self):
        return f"tags.json"


class TasksStream(BaseStream):
    TABLE = "tasks"
    RESPONSE_KEY = "todo-items"

    CACHE_RESULTS = True

    @property
    def path(self):
        return f"tasks.json"

    # The 'companies' endpoint is only in API version 1, so requires a different base
    def get_url_base(self):
        return self.config["hostname"] + "/"


AVAILABLE_STREAMS = [
    CompaniesStream,
    LatestActivityStream,
    ProjectsStream,
    ProjectUpdatesStream,
    PeopleStream,
    MilestonesStream,
    RisksStream,
    TagsStream,
    TasksStream,
]
