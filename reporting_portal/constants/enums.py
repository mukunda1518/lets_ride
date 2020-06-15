from enum import Enum

class Role(Enum):
    USER = 'USER'
    RP = 'RP'
    ADMIN = 'ADMIN'

class Severity(Enum):
    HIGH = 'HIGH'
    LOW = 'LOW'
    MEDIUM = 'MEDIUM'

class Status(Enum):
    REPORTED = 'REPORTED'
    ACKNOWLEDGED_BY_RP = 'ACKNOWLEDGED_BY_RP'
    ACTION_IN_PROGRESS = 'ACTION_IN_PROGRESS'
    RESOLVED = 'RESOLVED'
    CLOSED = 'CLOSED'
