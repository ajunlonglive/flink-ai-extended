# -*- coding: utf-8 -*-
#
# Licensed to the Apache Software Foundation (ASF) under one
# or more contributor license agreements.  See the NOTICE file
# distributed with this work for additional information
# regarding copyright ownership.  The ASF licenses this file
# to you under the Apache License, Version 2.0 (the
# "License"); you may not use this file except in compliance
# with the License.  You may obtain a copy of the License at
#
#   http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing,
# software distributed under the License is distributed on an
# "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY
# KIND, either express or implied.  See the License for the
# specific language governing permissions and limitations
# under the License.
#
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: notification_service.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf.internal import enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
from google.protobuf import service as _service
from google.protobuf import service_reflection
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='notification_service.proto',
  package='notification_service',
  syntax='proto3',
  serialized_options=b'\n\035com.aiflow.notification.proto\210\001\001\220\001\001',
  serialized_pb=b'\n\x1anotification_service.proto\x12\x14notification_service\"n\n\nEventProto\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\t\x12\x12\n\nevent_type\x18\x03 \x01(\t\x12\x0f\n\x07version\x18\x04 \x01(\x05\x12\x13\n\x0b\x63reate_time\x18\x05 \x01(\x03\x12\n\n\x02id\x18\x06 \x01(\x03\"C\n\x10SendEventRequest\x12/\n\x05\x65vent\x18\x01 \x01(\x0b\x32 .notification_service.EventProto\"n\n\x12SendEventsResponse\x12\x13\n\x0breturn_code\x18\x01 \x01(\t\x12\x12\n\nreturn_msg\x18\x02 \x01(\t\x12/\n\x05\x65vent\x18\x03 \x01(\x0b\x32 .notification_service.EventProto\"]\n\x11ListEventsRequest\x12/\n\x05\x65vent\x18\x01 \x01(\x0b\x32 .notification_service.EventProto\x12\x17\n\x0ftimeout_seconds\x18\x02 \x01(\x05\"C\n\x14ListAllEventsRequest\x12\x12\n\nstart_time\x18\x01 \x01(\x03\x12\x17\n\x0ftimeout_seconds\x18\x02 \x01(\x05\">\n\x17ListEventsFromIdRequest\x12\n\n\x02id\x18\x01 \x01(\x03\x12\x17\n\x0ftimeout_seconds\x18\x02 \x01(\x05\"o\n\x12ListEventsResponse\x12\x13\n\x0breturn_code\x18\x01 \x01(\t\x12\x12\n\nreturn_msg\x18\x02 \x01(\t\x12\x30\n\x06\x65vents\x18\x03 \x03(\x0b\x32 .notification_service.EventProto\"D\n\x1cGetLatestVersionByKeyRequest\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\x17\n\x0ftimeout_seconds\x18\x02 \x01(\x05\"T\n\x18GetLatestVersionResponse\x12\x13\n\x0breturn_code\x18\x01 \x01(\t\x12\x12\n\nreturn_msg\x18\x02 \x01(\t\x12\x0f\n\x07version\x18\x03 \x01(\x03*&\n\x0cReturnStatus\x12\x0b\n\x07SUCCESS\x10\x00\x12\t\n\x05\x45RROR\x10\x01\x32\xb0\x04\n\x13NotificationService\x12_\n\tsendEvent\x12&.notification_service.SendEventRequest\x1a(.notification_service.SendEventsResponse\"\x00\x12\x61\n\nlistEvents\x12\'.notification_service.ListEventsRequest\x1a(.notification_service.ListEventsResponse\"\x00\x12g\n\rlistAllEvents\x12*.notification_service.ListAllEventsRequest\x1a(.notification_service.ListEventsResponse\"\x00\x12m\n\x10listEventsFromId\x12-.notification_service.ListEventsFromIdRequest\x1a(.notification_service.ListEventsResponse\"\x00\x12}\n\x15getLatestVersionByKey\x12\x32.notification_service.GetLatestVersionByKeyRequest\x1a..notification_service.GetLatestVersionResponse\"\x00\x42%\n\x1d\x63om.aiflow.notification.proto\x88\x01\x01\x90\x01\x01\x62\x06proto3'
)

_RETURNSTATUS = _descriptor.EnumDescriptor(
  name='ReturnStatus',
  full_name='notification_service.ReturnStatus',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='SUCCESS', index=0, number=0,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='ERROR', index=1, number=1,
      serialized_options=None,
      type=None),
  ],
  containing_type=None,
  serialized_options=None,
  serialized_start=842,
  serialized_end=880,
)
_sym_db.RegisterEnumDescriptor(_RETURNSTATUS)

ReturnStatus = enum_type_wrapper.EnumTypeWrapper(_RETURNSTATUS)
SUCCESS = 0
ERROR = 1



_EVENTPROTO = _descriptor.Descriptor(
  name='EventProto',
  full_name='notification_service.EventProto',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='key', full_name='notification_service.EventProto.key', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='value', full_name='notification_service.EventProto.value', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='event_type', full_name='notification_service.EventProto.event_type', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='version', full_name='notification_service.EventProto.version', index=3,
      number=4, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='create_time', full_name='notification_service.EventProto.create_time', index=4,
      number=5, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='id', full_name='notification_service.EventProto.id', index=5,
      number=6, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=52,
  serialized_end=162,
)


_SENDEVENTREQUEST = _descriptor.Descriptor(
  name='SendEventRequest',
  full_name='notification_service.SendEventRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='event', full_name='notification_service.SendEventRequest.event', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=164,
  serialized_end=231,
)


_SENDEVENTSRESPONSE = _descriptor.Descriptor(
  name='SendEventsResponse',
  full_name='notification_service.SendEventsResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='return_code', full_name='notification_service.SendEventsResponse.return_code', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='return_msg', full_name='notification_service.SendEventsResponse.return_msg', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='event', full_name='notification_service.SendEventsResponse.event', index=2,
      number=3, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=233,
  serialized_end=343,
)


_LISTEVENTSREQUEST = _descriptor.Descriptor(
  name='ListEventsRequest',
  full_name='notification_service.ListEventsRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='event', full_name='notification_service.ListEventsRequest.event', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='timeout_seconds', full_name='notification_service.ListEventsRequest.timeout_seconds', index=1,
      number=2, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=345,
  serialized_end=438,
)


_LISTALLEVENTSREQUEST = _descriptor.Descriptor(
  name='ListAllEventsRequest',
  full_name='notification_service.ListAllEventsRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='start_time', full_name='notification_service.ListAllEventsRequest.start_time', index=0,
      number=1, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='timeout_seconds', full_name='notification_service.ListAllEventsRequest.timeout_seconds', index=1,
      number=2, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=440,
  serialized_end=507,
)


_LISTEVENTSFROMIDREQUEST = _descriptor.Descriptor(
  name='ListEventsFromIdRequest',
  full_name='notification_service.ListEventsFromIdRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='id', full_name='notification_service.ListEventsFromIdRequest.id', index=0,
      number=1, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='timeout_seconds', full_name='notification_service.ListEventsFromIdRequest.timeout_seconds', index=1,
      number=2, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=509,
  serialized_end=571,
)


_LISTEVENTSRESPONSE = _descriptor.Descriptor(
  name='ListEventsResponse',
  full_name='notification_service.ListEventsResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='return_code', full_name='notification_service.ListEventsResponse.return_code', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='return_msg', full_name='notification_service.ListEventsResponse.return_msg', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='events', full_name='notification_service.ListEventsResponse.events', index=2,
      number=3, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=573,
  serialized_end=684,
)


_GETLATESTVERSIONBYKEYREQUEST = _descriptor.Descriptor(
  name='GetLatestVersionByKeyRequest',
  full_name='notification_service.GetLatestVersionByKeyRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='key', full_name='notification_service.GetLatestVersionByKeyRequest.key', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='timeout_seconds', full_name='notification_service.GetLatestVersionByKeyRequest.timeout_seconds', index=1,
      number=2, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=686,
  serialized_end=754,
)


_GETLATESTVERSIONRESPONSE = _descriptor.Descriptor(
  name='GetLatestVersionResponse',
  full_name='notification_service.GetLatestVersionResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='return_code', full_name='notification_service.GetLatestVersionResponse.return_code', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='return_msg', full_name='notification_service.GetLatestVersionResponse.return_msg', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='version', full_name='notification_service.GetLatestVersionResponse.version', index=2,
      number=3, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=756,
  serialized_end=840,
)

_SENDEVENTREQUEST.fields_by_name['event'].message_type = _EVENTPROTO
_SENDEVENTSRESPONSE.fields_by_name['event'].message_type = _EVENTPROTO
_LISTEVENTSREQUEST.fields_by_name['event'].message_type = _EVENTPROTO
_LISTEVENTSRESPONSE.fields_by_name['events'].message_type = _EVENTPROTO
DESCRIPTOR.message_types_by_name['EventProto'] = _EVENTPROTO
DESCRIPTOR.message_types_by_name['SendEventRequest'] = _SENDEVENTREQUEST
DESCRIPTOR.message_types_by_name['SendEventsResponse'] = _SENDEVENTSRESPONSE
DESCRIPTOR.message_types_by_name['ListEventsRequest'] = _LISTEVENTSREQUEST
DESCRIPTOR.message_types_by_name['ListAllEventsRequest'] = _LISTALLEVENTSREQUEST
DESCRIPTOR.message_types_by_name['ListEventsFromIdRequest'] = _LISTEVENTSFROMIDREQUEST
DESCRIPTOR.message_types_by_name['ListEventsResponse'] = _LISTEVENTSRESPONSE
DESCRIPTOR.message_types_by_name['GetLatestVersionByKeyRequest'] = _GETLATESTVERSIONBYKEYREQUEST
DESCRIPTOR.message_types_by_name['GetLatestVersionResponse'] = _GETLATESTVERSIONRESPONSE
DESCRIPTOR.enum_types_by_name['ReturnStatus'] = _RETURNSTATUS
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

EventProto = _reflection.GeneratedProtocolMessageType('EventProto', (_message.Message,), {
  'DESCRIPTOR' : _EVENTPROTO,
  '__module__' : 'notification_service_pb2'
  # @@protoc_insertion_point(class_scope:notification_service.EventProto)
  })
_sym_db.RegisterMessage(EventProto)

SendEventRequest = _reflection.GeneratedProtocolMessageType('SendEventRequest', (_message.Message,), {
  'DESCRIPTOR' : _SENDEVENTREQUEST,
  '__module__' : 'notification_service_pb2'
  # @@protoc_insertion_point(class_scope:notification_service.SendEventRequest)
  })
_sym_db.RegisterMessage(SendEventRequest)

SendEventsResponse = _reflection.GeneratedProtocolMessageType('SendEventsResponse', (_message.Message,), {
  'DESCRIPTOR' : _SENDEVENTSRESPONSE,
  '__module__' : 'notification_service_pb2'
  # @@protoc_insertion_point(class_scope:notification_service.SendEventsResponse)
  })
_sym_db.RegisterMessage(SendEventsResponse)

ListEventsRequest = _reflection.GeneratedProtocolMessageType('ListEventsRequest', (_message.Message,), {
  'DESCRIPTOR' : _LISTEVENTSREQUEST,
  '__module__' : 'notification_service_pb2'
  # @@protoc_insertion_point(class_scope:notification_service.ListEventsRequest)
  })
_sym_db.RegisterMessage(ListEventsRequest)

ListAllEventsRequest = _reflection.GeneratedProtocolMessageType('ListAllEventsRequest', (_message.Message,), {
  'DESCRIPTOR' : _LISTALLEVENTSREQUEST,
  '__module__' : 'notification_service_pb2'
  # @@protoc_insertion_point(class_scope:notification_service.ListAllEventsRequest)
  })
_sym_db.RegisterMessage(ListAllEventsRequest)

ListEventsFromIdRequest = _reflection.GeneratedProtocolMessageType('ListEventsFromIdRequest', (_message.Message,), {
  'DESCRIPTOR' : _LISTEVENTSFROMIDREQUEST,
  '__module__' : 'notification_service_pb2'
  # @@protoc_insertion_point(class_scope:notification_service.ListEventsFromIdRequest)
  })
_sym_db.RegisterMessage(ListEventsFromIdRequest)

ListEventsResponse = _reflection.GeneratedProtocolMessageType('ListEventsResponse', (_message.Message,), {
  'DESCRIPTOR' : _LISTEVENTSRESPONSE,
  '__module__' : 'notification_service_pb2'
  # @@protoc_insertion_point(class_scope:notification_service.ListEventsResponse)
  })
_sym_db.RegisterMessage(ListEventsResponse)

GetLatestVersionByKeyRequest = _reflection.GeneratedProtocolMessageType('GetLatestVersionByKeyRequest', (_message.Message,), {
  'DESCRIPTOR' : _GETLATESTVERSIONBYKEYREQUEST,
  '__module__' : 'notification_service_pb2'
  # @@protoc_insertion_point(class_scope:notification_service.GetLatestVersionByKeyRequest)
  })
_sym_db.RegisterMessage(GetLatestVersionByKeyRequest)

GetLatestVersionResponse = _reflection.GeneratedProtocolMessageType('GetLatestVersionResponse', (_message.Message,), {
  'DESCRIPTOR' : _GETLATESTVERSIONRESPONSE,
  '__module__' : 'notification_service_pb2'
  # @@protoc_insertion_point(class_scope:notification_service.GetLatestVersionResponse)
  })
_sym_db.RegisterMessage(GetLatestVersionResponse)


DESCRIPTOR._options = None

_NOTIFICATIONSERVICE = _descriptor.ServiceDescriptor(
  name='NotificationService',
  full_name='notification_service.NotificationService',
  file=DESCRIPTOR,
  index=0,
  serialized_options=None,
  serialized_start=883,
  serialized_end=1443,
  methods=[
  _descriptor.MethodDescriptor(
    name='sendEvent',
    full_name='notification_service.NotificationService.sendEvent',
    index=0,
    containing_service=None,
    input_type=_SENDEVENTREQUEST,
    output_type=_SENDEVENTSRESPONSE,
    serialized_options=None,
  ),
  _descriptor.MethodDescriptor(
    name='listEvents',
    full_name='notification_service.NotificationService.listEvents',
    index=1,
    containing_service=None,
    input_type=_LISTEVENTSREQUEST,
    output_type=_LISTEVENTSRESPONSE,
    serialized_options=None,
  ),
  _descriptor.MethodDescriptor(
    name='listAllEvents',
    full_name='notification_service.NotificationService.listAllEvents',
    index=2,
    containing_service=None,
    input_type=_LISTALLEVENTSREQUEST,
    output_type=_LISTEVENTSRESPONSE,
    serialized_options=None,
  ),
  _descriptor.MethodDescriptor(
    name='listEventsFromId',
    full_name='notification_service.NotificationService.listEventsFromId',
    index=3,
    containing_service=None,
    input_type=_LISTEVENTSFROMIDREQUEST,
    output_type=_LISTEVENTSRESPONSE,
    serialized_options=None,
  ),
  _descriptor.MethodDescriptor(
    name='getLatestVersionByKey',
    full_name='notification_service.NotificationService.getLatestVersionByKey',
    index=4,
    containing_service=None,
    input_type=_GETLATESTVERSIONBYKEYREQUEST,
    output_type=_GETLATESTVERSIONRESPONSE,
    serialized_options=None,
  ),
])
_sym_db.RegisterServiceDescriptor(_NOTIFICATIONSERVICE)

DESCRIPTOR.services_by_name['NotificationService'] = _NOTIFICATIONSERVICE

NotificationService = service_reflection.GeneratedServiceType('NotificationService', (_service.Service,), dict(
  DESCRIPTOR = _NOTIFICATIONSERVICE,
  __module__ = 'notification_service_pb2'
  ))

NotificationService_Stub = service_reflection.GeneratedServiceStubType('NotificationService_Stub', (NotificationService,), dict(
  DESCRIPTOR = _NOTIFICATIONSERVICE,
  __module__ = 'notification_service_pb2'
  ))


# @@protoc_insertion_point(module_scope)
