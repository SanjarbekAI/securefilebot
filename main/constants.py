from enum import Enum


class UserStatus(str, Enum):
    active = "active"
    inactive = "inactive"


class DirectoryStatus(str, Enum):
    active = "active"
    inactive = "inactive"


class FileStatus(str, Enum):
    active = "active"
    inactive = "inactive"
    deleted = "deleted"


class FileType(str, Enum):
    photo = "photo"
    video = "video"
    video_note = "video_note"
    document = "document"
    voice = "voice"
    text = "text"
    audio = "audio"
    contact = "contact"
    location = "location"
    animation = "animation"