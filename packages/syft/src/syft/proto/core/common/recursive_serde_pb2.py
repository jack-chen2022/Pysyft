# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: proto/core/common/recursive_serde.proto
"""Generated protocol buffer code."""
# third party
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database

# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


DESCRIPTOR = _descriptor.FileDescriptor(
    name="proto/core/common/recursive_serde.proto",
    package="syft.core.common",
    syntax="proto3",
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
<<<<<<< HEAD
    serialized_pb=b"\n'proto/core/common/recursive_serde.proto\x12\x10syft.core.common\"0\n\x0eRecursiveSerde\x12\x10\n\x08obj_type\x18\x01 \x01(\t\x12\x0c\n\x04\x64\x61ta\x18\x02 \x01(\x0c\x62\x06proto3",
=======
    serialized_pb=b"\n'proto/core/common/recursive_serde.proto\x12\x10syft.core.common\"<\n\x0eRecursiveSerde\x12\x0c\n\x04\x64\x61ta\x18\x01 \x01(\x0c\x12\x1c\n\x14\x66ully_qualified_name\x18\x02 \x01(\tb\x06proto3",
>>>>>>> d6688c7d1a2dea7ca122cde60e0a14b3690aa678
)


_RECURSIVESERDE = _descriptor.Descriptor(
    name="RecursiveSerde",
    full_name="syft.core.common.RecursiveSerde",
    filename=None,
    file=DESCRIPTOR,
    containing_type=None,
    create_key=_descriptor._internal_create_key,
    fields=[
        _descriptor.FieldDescriptor(
<<<<<<< HEAD
            name="obj_type",
            full_name="syft.core.common.RecursiveSerde.obj_type",
            index=0,
            number=1,
            type=9,
            cpp_type=9,
            label=1,
            has_default_value=False,
            default_value=b"".decode("utf-8"),
=======
            name="data",
            full_name="syft.core.common.RecursiveSerde.data",
            index=0,
            number=1,
            type=12,
            cpp_type=9,
            label=1,
            has_default_value=False,
            default_value=b"",
>>>>>>> d6688c7d1a2dea7ca122cde60e0a14b3690aa678
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
<<<<<<< HEAD
            name="data",
            full_name="syft.core.common.RecursiveSerde.data",
            index=1,
            number=2,
            type=12,
            cpp_type=9,
            label=1,
            has_default_value=False,
            default_value=b"",
=======
            name="fully_qualified_name",
            full_name="syft.core.common.RecursiveSerde.fully_qualified_name",
            index=1,
            number=2,
            type=9,
            cpp_type=9,
            label=1,
            has_default_value=False,
            default_value=b"".decode("utf-8"),
>>>>>>> d6688c7d1a2dea7ca122cde60e0a14b3690aa678
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
    serialized_start=61,
<<<<<<< HEAD
    serialized_end=109,
=======
    serialized_end=121,
>>>>>>> d6688c7d1a2dea7ca122cde60e0a14b3690aa678
)

DESCRIPTOR.message_types_by_name["RecursiveSerde"] = _RECURSIVESERDE
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

RecursiveSerde = _reflection.GeneratedProtocolMessageType(
    "RecursiveSerde",
    (_message.Message,),
    {
        "DESCRIPTOR": _RECURSIVESERDE,
        "__module__": "proto.core.common.recursive_serde_pb2"
        # @@protoc_insertion_point(class_scope:syft.core.common.RecursiveSerde)
    },
)
_sym_db.RegisterMessage(RecursiveSerde)


# @@protoc_insertion_point(module_scope)
