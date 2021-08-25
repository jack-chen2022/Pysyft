# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: proto/lib/transformers/batch_encoding.proto
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
    common_object_pb2 as proto_dot_core_dot_common_dot_common__object__pb2,
)
from syft.proto.lib.python import dict_pb2 as proto_dot_lib_dot_python_dot_dict__pb2

DESCRIPTOR = _descriptor.FileDescriptor(
    name="proto/lib/transformers/batch_encoding.proto",
    package="syft.lib.transformers",
    syntax="proto3",
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
    serialized_pb=b'\n+proto/lib/transformers/batch_encoding.proto\x12\x15syft.lib.transformers\x1a%proto/core/common/common_object.proto\x1a\x1bproto/lib/python/dict.proto"W\n\rBatchEncoding\x12!\n\x02id\x18\x01 \x01(\x0b\x32\x15.syft.core.common.UID\x12#\n\x04\x64\x61ta\x18\x02 \x01(\x0b\x32\x15.syft.lib.python.Dictb\x06proto3',
    dependencies=[
        proto_dot_core_dot_common_dot_common__object__pb2.DESCRIPTOR,
        proto_dot_lib_dot_python_dot_dict__pb2.DESCRIPTOR,
    ],
)


_BATCHENCODING = _descriptor.Descriptor(
    name="BatchEncoding",
    full_name="syft.lib.transformers.BatchEncoding",
    filename=None,
    file=DESCRIPTOR,
    containing_type=None,
    create_key=_descriptor._internal_create_key,
    fields=[
        _descriptor.FieldDescriptor(
            name="id",
            full_name="syft.lib.transformers.BatchEncoding.id",
            index=0,
            number=1,
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
            name="data",
            full_name="syft.lib.transformers.BatchEncoding.data",
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
    ],
    extensions=[],
    nested_types=[],
    enum_types=[],
    serialized_options=None,
    is_extendable=False,
    syntax="proto3",
    extension_ranges=[],
    oneofs=[],
    serialized_start=138,
    serialized_end=225,
)

_BATCHENCODING.fields_by_name[
    "id"
].message_type = proto_dot_core_dot_common_dot_common__object__pb2._UID
_BATCHENCODING.fields_by_name[
    "data"
].message_type = proto_dot_lib_dot_python_dot_dict__pb2._DICT
DESCRIPTOR.message_types_by_name["BatchEncoding"] = _BATCHENCODING
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

BatchEncoding = _reflection.GeneratedProtocolMessageType(
    "BatchEncoding",
    (_message.Message,),
    {
        "DESCRIPTOR": _BATCHENCODING,
        "__module__": "proto.lib.transformers.batch_encoding_pb2"
        # @@protoc_insertion_point(class_scope:syft.lib.transformers.BatchEncoding)
    },
)
_sym_db.RegisterMessage(BatchEncoding)


# @@protoc_insertion_point(module_scope)
