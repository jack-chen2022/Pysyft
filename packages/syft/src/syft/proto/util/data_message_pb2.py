# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: proto/util/data_message.proto
"""Generated protocol buffer code."""
# third party
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder

# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(
    b'\n\x1dproto/util/data_message.proto\x12\tsyft.util"F\n\x0b\x44\x61taMessage\x12\x14\n\x0cmagic_header\x18\x01 \x01(\t\x12\x10\n\x08obj_type\x18\x02 \x01(\t\x12\x0f\n\x07\x63ontent\x18\x03 \x01(\x0c\x62\x06proto3'
)

_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, globals())
_builder.BuildTopDescriptorsAndMessages(
    DESCRIPTOR, "proto.util.data_message_pb2", globals()
)
if _descriptor._USE_C_DESCRIPTORS == False:

    DESCRIPTOR._options = None
    _DATAMESSAGE._serialized_start = 44
    _DATAMESSAGE._serialized_end = 114
# @@protoc_insertion_point(module_scope)
