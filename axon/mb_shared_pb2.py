# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: mb_shared.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()

from my_git.playPub.axon import mb_shared_infra_pb2 as mb__shared__infra__pb2

from my_git.playPub.axon.mb_shared_infra_pb2 import *

DESCRIPTOR = _descriptor.FileDescriptor(
  name='mb_shared.proto',
  package='com.bt.magicbox',
  syntax='proto3',
  serialized_options=_b('\242\002\002MB'),
  serialized_pb=_b('\n\x0fmb_shared.proto\x12\x0f\x63om.bt.magicbox\x1a\x15mb_shared_infra.proto\".\n\x0eHomographyData\x12\x1c\n\x10homographyMatrix\x18\x01 \x03(\x01\x42\x02\x10\x01\"\n\n\x08GeoModel\"\x93\x01\n\rFrameMetadata\x12\n\n\x02id\x18\x01 \x01(\r\x12\x0f\n\x07timeUtc\x18\x02 \x01(\x04\x12\x30\n\nrasterInfo\x18\x03 \x01(\x0b\x32\x1c.com.bt.magicbox.FrameRaster\x12\x33\n\nhomography\x18\x04 \x01(\x0b\x32\x1f.com.bt.magicbox.HomographyData\"k\n\x18SharedResourceDescriptor\x12\x0b\n\x03uri\x18\x01 \x01(\t\x12\x11\n\tsizeBytes\x18\x02 \x01(\r\x12\x16\n\x0e\x65ntrySizeBytes\x18\x03 \x01(\r\x12\x17\n\x0fnumberOfEntries\x18\x04 \x01(\r\"\xaf\x01\n\x14\x46rameCaptureMetadata\x12\x16\n\x0e\x65xposureTimeNs\x18\x01 \x01(\x04\x12\x0c\n\x04gain\x18\x02 \x01(\x04\x12;\n\x10lightMetringMode\x18\x03 \x01(\x0e\x32!.com.bt.magicbox.LightMetringMode\x12\"\n\x1a\x65xposureCompensationOffset\x18\x04 \x01(\x02\x12\x10\n\x08\x61perture\x18\x05 \x01(\x02\"\x8e\x02\n\x0b\x46rameRaster\x12(\n\x04size\x18\x01 \x01(\x0b\x32\x1a.com.bt.magicbox.SizeInt32\x12\x10\n\x08\x63hannels\x18\x02 \x01(\r\x12\x10\n\x08\x62itDepth\x18\x03 \x01(\r\x12\x0e\n\x06stride\x18\x04 \x01(\r\x12\x46\n\x13\x63ontainerDescriptor\x18\x05 \x01(\x0b\x32).com.bt.magicbox.SharedResourceDescriptor\x12\x19\n\x11offsetInContainer\x18\x06 \x01(\r\x12>\n\x0f\x63\x61ptureMetadata\x18\x07 \x01(\x0b\x32%.com.bt.magicbox.FrameCaptureMetadata*/\n\x11GeoLocationSource\x12\x07\n\x03GPS\x10\x00\x12\x11\n\rGEO_ANCHORING\x10\x01*\xb7\x01\n\x10LightMetringMode\x12\x1e\n\x1aLIGHT_METRING_MODE_UNKNOWN\x10\x00\x12\x1e\n\x1aLIGHT_METRING_MODE_AVARAGE\x10\x01\x12\x1b\n\x17LIGHT_METRING_MODE_SPOT\x10\x02\x12\x1e\n\x1aLIGHT_METRING_MODE_PARTIAL\x10\x03\x12&\n\"LIGHT_METRING_MODE_CENTER_WEIGHTED\x10\x04\x42\x05\xa2\x02\x02MBP\x00\x62\x06proto3')
  ,
  dependencies=[mb__shared__infra__pb2.DESCRIPTOR,],
  public_dependencies=[mb__shared__infra__pb2.DESCRIPTOR,])

_GEOLOCATIONSOURCE = _descriptor.EnumDescriptor(
  name='GeoLocationSource',
  full_name='com.bt.magicbox.GeoLocationSource',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='GPS', index=0, number=0,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='GEO_ANCHORING', index=1, number=1,
      serialized_options=None,
      type=None),
  ],
  containing_type=None,
  serialized_options=None,
  serialized_start=829,
  serialized_end=876,
)
_sym_db.RegisterEnumDescriptor(_GEOLOCATIONSOURCE)

GeoLocationSource = enum_type_wrapper.EnumTypeWrapper(_GEOLOCATIONSOURCE)
_LIGHTMETRINGMODE = _descriptor.EnumDescriptor(
  name='LightMetringMode',
  full_name='com.bt.magicbox.LightMetringMode',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='LIGHT_METRING_MODE_UNKNOWN', index=0, number=0,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='LIGHT_METRING_MODE_AVARAGE', index=1, number=1,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='LIGHT_METRING_MODE_SPOT', index=2, number=2,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='LIGHT_METRING_MODE_PARTIAL', index=3, number=3,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='LIGHT_METRING_MODE_CENTER_WEIGHTED', index=4, number=4,
      serialized_options=None,
      type=None),
  ],
  containing_type=None,
  serialized_options=None,
  serialized_start=879,
  serialized_end=1062,
)
_sym_db.RegisterEnumDescriptor(_LIGHTMETRINGMODE)

LightMetringMode = enum_type_wrapper.EnumTypeWrapper(_LIGHTMETRINGMODE)
GPS = 0
GEO_ANCHORING = 1
LIGHT_METRING_MODE_UNKNOWN = 0
LIGHT_METRING_MODE_AVARAGE = 1
LIGHT_METRING_MODE_SPOT = 2
LIGHT_METRING_MODE_PARTIAL = 3
LIGHT_METRING_MODE_CENTER_WEIGHTED = 4



_HOMOGRAPHYDATA = _descriptor.Descriptor(
  name='HomographyData',
  full_name='com.bt.magicbox.HomographyData',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='homographyMatrix', full_name='com.bt.magicbox.HomographyData.homographyMatrix', index=0,
      number=1, type=1, cpp_type=5, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=_b('\020\001'), file=DESCRIPTOR),
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
  serialized_start=59,
  serialized_end=105,
)


_GEOMODEL = _descriptor.Descriptor(
  name='GeoModel',
  full_name='com.bt.magicbox.GeoModel',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
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
  serialized_start=107,
  serialized_end=117,
)


_FRAMEMETADATA = _descriptor.Descriptor(
  name='FrameMetadata',
  full_name='com.bt.magicbox.FrameMetadata',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='id', full_name='com.bt.magicbox.FrameMetadata.id', index=0,
      number=1, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='timeUtc', full_name='com.bt.magicbox.FrameMetadata.timeUtc', index=1,
      number=2, type=4, cpp_type=4, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='rasterInfo', full_name='com.bt.magicbox.FrameMetadata.rasterInfo', index=2,
      number=3, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='homography', full_name='com.bt.magicbox.FrameMetadata.homography', index=3,
      number=4, type=11, cpp_type=10, label=1,
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
  serialized_start=120,
  serialized_end=267,
)


_SHAREDRESOURCEDESCRIPTOR = _descriptor.Descriptor(
  name='SharedResourceDescriptor',
  full_name='com.bt.magicbox.SharedResourceDescriptor',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='uri', full_name='com.bt.magicbox.SharedResourceDescriptor.uri', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='sizeBytes', full_name='com.bt.magicbox.SharedResourceDescriptor.sizeBytes', index=1,
      number=2, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='entrySizeBytes', full_name='com.bt.magicbox.SharedResourceDescriptor.entrySizeBytes', index=2,
      number=3, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='numberOfEntries', full_name='com.bt.magicbox.SharedResourceDescriptor.numberOfEntries', index=3,
      number=4, type=13, cpp_type=3, label=1,
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
  serialized_start=269,
  serialized_end=376,
)


_FRAMECAPTUREMETADATA = _descriptor.Descriptor(
  name='FrameCaptureMetadata',
  full_name='com.bt.magicbox.FrameCaptureMetadata',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='exposureTimeNs', full_name='com.bt.magicbox.FrameCaptureMetadata.exposureTimeNs', index=0,
      number=1, type=4, cpp_type=4, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='gain', full_name='com.bt.magicbox.FrameCaptureMetadata.gain', index=1,
      number=2, type=4, cpp_type=4, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='lightMetringMode', full_name='com.bt.magicbox.FrameCaptureMetadata.lightMetringMode', index=2,
      number=3, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='exposureCompensationOffset', full_name='com.bt.magicbox.FrameCaptureMetadata.exposureCompensationOffset', index=3,
      number=4, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='aperture', full_name='com.bt.magicbox.FrameCaptureMetadata.aperture', index=4,
      number=5, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=float(0),
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
  serialized_start=379,
  serialized_end=554,
)


_FRAMERASTER = _descriptor.Descriptor(
  name='FrameRaster',
  full_name='com.bt.magicbox.FrameRaster',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='size', full_name='com.bt.magicbox.FrameRaster.size', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='channels', full_name='com.bt.magicbox.FrameRaster.channels', index=1,
      number=2, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='bitDepth', full_name='com.bt.magicbox.FrameRaster.bitDepth', index=2,
      number=3, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='stride', full_name='com.bt.magicbox.FrameRaster.stride', index=3,
      number=4, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='containerDescriptor', full_name='com.bt.magicbox.FrameRaster.containerDescriptor', index=4,
      number=5, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='offsetInContainer', full_name='com.bt.magicbox.FrameRaster.offsetInContainer', index=5,
      number=6, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='captureMetadata', full_name='com.bt.magicbox.FrameRaster.captureMetadata', index=6,
      number=7, type=11, cpp_type=10, label=1,
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
  serialized_start=557,
  serialized_end=827,
)

_FRAMEMETADATA.fields_by_name['rasterInfo'].message_type = _FRAMERASTER
_FRAMEMETADATA.fields_by_name['homography'].message_type = _HOMOGRAPHYDATA
_FRAMECAPTUREMETADATA.fields_by_name['lightMetringMode'].enum_type = _LIGHTMETRINGMODE
_FRAMERASTER.fields_by_name['size'].message_type = mb__shared__infra__pb2._SIZEINT32
_FRAMERASTER.fields_by_name['containerDescriptor'].message_type = _SHAREDRESOURCEDESCRIPTOR
_FRAMERASTER.fields_by_name['captureMetadata'].message_type = _FRAMECAPTUREMETADATA
DESCRIPTOR.message_types_by_name['HomographyData'] = _HOMOGRAPHYDATA
DESCRIPTOR.message_types_by_name['GeoModel'] = _GEOMODEL
DESCRIPTOR.message_types_by_name['FrameMetadata'] = _FRAMEMETADATA
DESCRIPTOR.message_types_by_name['SharedResourceDescriptor'] = _SHAREDRESOURCEDESCRIPTOR
DESCRIPTOR.message_types_by_name['FrameCaptureMetadata'] = _FRAMECAPTUREMETADATA
DESCRIPTOR.message_types_by_name['FrameRaster'] = _FRAMERASTER
DESCRIPTOR.enum_types_by_name['GeoLocationSource'] = _GEOLOCATIONSOURCE
DESCRIPTOR.enum_types_by_name['LightMetringMode'] = _LIGHTMETRINGMODE
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

HomographyData = _reflection.GeneratedProtocolMessageType('HomographyData', (_message.Message,), {
  'DESCRIPTOR' : _HOMOGRAPHYDATA,
  '__module__' : 'mb_shared_pb2'
  # @@protoc_insertion_point(class_scope:com.bt.magicbox.HomographyData)
  })
_sym_db.RegisterMessage(HomographyData)

GeoModel = _reflection.GeneratedProtocolMessageType('GeoModel', (_message.Message,), {
  'DESCRIPTOR' : _GEOMODEL,
  '__module__' : 'mb_shared_pb2'
  # @@protoc_insertion_point(class_scope:com.bt.magicbox.GeoModel)
  })
_sym_db.RegisterMessage(GeoModel)

FrameMetadata = _reflection.GeneratedProtocolMessageType('FrameMetadata', (_message.Message,), {
  'DESCRIPTOR' : _FRAMEMETADATA,
  '__module__' : 'mb_shared_pb2'
  # @@protoc_insertion_point(class_scope:com.bt.magicbox.FrameMetadata)
  })
_sym_db.RegisterMessage(FrameMetadata)

SharedResourceDescriptor = _reflection.GeneratedProtocolMessageType('SharedResourceDescriptor', (_message.Message,), {
  'DESCRIPTOR' : _SHAREDRESOURCEDESCRIPTOR,
  '__module__' : 'mb_shared_pb2'
  # @@protoc_insertion_point(class_scope:com.bt.magicbox.SharedResourceDescriptor)
  })
_sym_db.RegisterMessage(SharedResourceDescriptor)

FrameCaptureMetadata = _reflection.GeneratedProtocolMessageType('FrameCaptureMetadata', (_message.Message,), {
  'DESCRIPTOR' : _FRAMECAPTUREMETADATA,
  '__module__' : 'mb_shared_pb2'
  # @@protoc_insertion_point(class_scope:com.bt.magicbox.FrameCaptureMetadata)
  })
_sym_db.RegisterMessage(FrameCaptureMetadata)

FrameRaster = _reflection.GeneratedProtocolMessageType('FrameRaster', (_message.Message,), {
  'DESCRIPTOR' : _FRAMERASTER,
  '__module__' : 'mb_shared_pb2'
  # @@protoc_insertion_point(class_scope:com.bt.magicbox.FrameRaster)
  })
_sym_db.RegisterMessage(FrameRaster)


DESCRIPTOR._options = None
_HOMOGRAPHYDATA.fields_by_name['homographyMatrix']._options = None
# @@protoc_insertion_point(module_scope)
