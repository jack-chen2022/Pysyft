# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: proto/lib/python/list.proto
"""Generated protocol buffer code."""
# third party
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database

# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


# syft absolute
from syft.proto.core.common import (
    recursive_serde_pb2 as proto_dot_core_dot_common_dot_recursive__serde__pb2,
)

DESCRIPTOR = _descriptor.FileDescriptor(
    name="proto/lib/python/list.proto",
    package="syft.lib.python",
    syntax="proto3",
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
    serialized_pb=b"\n\x1bproto/lib/python/list.proto\x12\x0fsyft.lib.python\x1a'proto/core/common/recursive_serde.proto\"Y\n\x04List\x12\x0c\n\x04\x64\x61ta\x18\x01 \x03(\x0c\x12,\n\x02id\x18\x02 \x01(\x0b\x32 .syft.core.common.RecursiveSerde\x12\x15\n\rtemporary_box\x18\x03 \x01(\x08\x62\x06proto3",
    dependencies=[
        proto_dot_core_dot_common_dot_recursive__serde__pb2.DESCRIPTOR,
    ],
)


_LIST = _descriptor.Descriptor(
    name="List",
    full_name="syft.lib.python.List",
    filename=None,
    file=DESCRIPTOR,
    containing_type=None,
    create_key=_descriptor._internal_create_key,
    fields=[
        _descriptor.FieldDescriptor(
            name="data",
            full_name="syft.lib.python.List.data",
            index=0,
            number=1,
            type=12,
            cpp_type=9,
            label=3,
            has_default_value=False,
            default_value=[],
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            file=DESCRIPTOR,
            create_key=_descriptor._internal_create_key,
        ),
        _descriptor.FieldDescriptor(
            name="id",
            full_name="syft.lib.python.List.id",
            index=1,
            number=2,
            type=11,
            cpp_type=10,
            label=1,
            has_default_value=False,
            default_value=None,
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            file=DESCRIPTOR,
            create_key=_descriptor._internal_create_key,
        ),
        _descriptor.FieldDescriptor(
            name="temporary_box",
            full_name="syft.lib.python.List.temporary_box",
            index=2,
            number=3,
            type=8,
            cpp_type=7,
            label=1,
            has_default_value=False,
            default_value=False,
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            file=DESCRIPTOR,
            create_key=_descriptor._internal_create_key,
        ),
    ],
    extensions=[],
    nested_types=[],
    enum_types=[],
    serialized_options=None,
    is_extendable=False,
    syntax="proto3",
    extension_ranges=[],
    oneofs=[],
    serialized_start=89,
    serialized_end=178,
)

_LIST.fields_by_name[
    "id"
].message_type = proto_dot_core_dot_common_dot_recursive__serde__pb2._RECURSIVESERDE
DESCRIPTOR.message_types_by_name["List"] = _LIST
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

List = _reflection.GeneratedProtocolMessageType(
    "List",
    (_message.Message,),
    {
        "DESCRIPTOR": _LIST,
        "__module__": "proto.lib.python.list_pb2"
        # @@protoc_insertion_point(class_scope:syft.lib.python.List)
    },
)
_sym_db.RegisterMessage(List)


# @@protoc_insertion_point(module_scope)
