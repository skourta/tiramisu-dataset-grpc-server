from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class TiramisuFunctionName(_message.Message):
    __slots__ = ["name"]
    NAME_FIELD_NUMBER: _ClassVar[int]
    name: str
    def __init__(self, name: _Optional[str] = ...) -> None: ...

class TiramisuFunction(_message.Message):
    __slots__ = ["name", "content", "cpp", "wrapper"]
    NAME_FIELD_NUMBER: _ClassVar[int]
    CONTENT_FIELD_NUMBER: _ClassVar[int]
    CPP_FIELD_NUMBER: _ClassVar[int]
    WRAPPER_FIELD_NUMBER: _ClassVar[int]
    name: str
    content: str
    cpp: str
    wrapper: bytes
    def __init__(self, name: _Optional[str] = ..., content: _Optional[str] = ..., cpp: _Optional[str] = ..., wrapper: _Optional[bytes] = ...) -> None: ...

class DatasetSize(_message.Message):
    __slots__ = ["size"]
    SIZE_FIELD_NUMBER: _ClassVar[int]
    size: int
    def __init__(self, size: _Optional[int] = ...) -> None: ...

class Empty(_message.Message):
    __slots__ = []
    def __init__(self) -> None: ...

class TiramisuListOfFunctions(_message.Message):
    __slots__ = ["names"]
    NAMES_FIELD_NUMBER: _ClassVar[int]
    names: _containers.RepeatedScalarFieldContainer[str]
    def __init__(self, names: _Optional[_Iterable[str]] = ...) -> None: ...
