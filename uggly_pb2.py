# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: uggly.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x0buggly.proto\x12\x05uggly\">\n\x05Pixel\x12\t\n\x01\x63\x18\n \x01(\x05\x12\x18\n\x02st\x18\x0b \x01(\x0b\x32\x0c.uggly.Style\x12\x10\n\x08isBorder\x18\x0c \x01(\x08\"\xf8\x01\n\x06\x44ivBox\x12\x0c\n\x04name\x18\t \x01(\t\x12\x0e\n\x06\x62order\x18\n \x01(\x08\x12\x0f\n\x07\x62orderW\x18\x0b \x01(\x05\x12\x12\n\nborderChar\x18\x0c \x01(\x05\x12\x10\n\x08\x66illChar\x18\x0e \x01(\x05\x12\x0e\n\x06startX\x18\x0f \x01(\x05\x12\x0e\n\x06startY\x18\x10 \x01(\x05\x12\r\n\x05width\x18\x11 \x01(\x05\x12\x0e\n\x06Height\x18\x12 \x01(\x05\x12\x1c\n\x06pixels\x18\x13 \x03(\x0b\x32\x0c.uggly.Pixel\x12\x1e\n\x08\x62orderSt\x18\x14 \x01(\x0b\x32\x0c.uggly.Style\x12\x1c\n\x06\x66illSt\x18\x15 \x01(\x0b\x32\x0c.uggly.Style\"X\n\x08TextBlob\x12\x0f\n\x07\x63ontent\x18\n \x01(\t\x12\x0c\n\x04wrap\x18\x0b \x01(\x08\x12\x1b\n\x05style\x18\x0c \x01(\x0b\x32\x0c.uggly.Style\x12\x10\n\x08\x64ivNames\x18\x0f \x03(\t\"(\n\x08\x44ivBoxes\x12\x1c\n\x05\x62oxes\x18\n \x03(\x0b\x32\r.uggly.DivBox\"-\n\x05Style\x12\n\n\x02\x66g\x18\n \x01(\t\x12\n\n\x02\x62g\x18\x0b \x01(\t\x12\x0c\n\x04\x61ttr\x18\x0c \x01(\t\"i\n\x04Link\x12\x11\n\tkeyStroke\x18\n \x01(\t\x12\x10\n\x08pageName\x18\x0b \x01(\t\x12\x0e\n\x06server\x18\x0c \x01(\t\x12\x0c\n\x04port\x18\r \x01(\t\x12\x0e\n\x06secure\x18\x10 \x01(\x08\x12\x0e\n\x06stream\x18\x11 \x01(\x08\"*\n\tDivScroll\x12\x0f\n\x07\x64ivName\x18\n \x01(\t\x12\x0c\n\x04\x64own\x18\x0b \x01(\x08\"\"\n\x0e\x46ormActivation\x12\x10\n\x08\x66ormName\x18\n \x01(\t\"\x9d\x01\n\tKeyStroke\x12\x11\n\tkeyStroke\x18\n \x01(\t\x12\x1b\n\x04link\x18\x14 \x01(\x0b\x32\x0b.uggly.LinkH\x00\x12%\n\tdivScroll\x18\x15 \x01(\x0b\x32\x10.uggly.DivScrollH\x00\x12/\n\x0e\x66ormActivation\x18\x16 \x01(\x0b\x32\x15.uggly.FormActivationH\x00\x42\x08\n\x06\x41\x63tion\"\xd1\x02\n\x07TextBox\x12\x0c\n\x04name\x18\n \x01(\t\x12\x10\n\x08tabOrder\x18\x0b \x01(\x05\x12\x14\n\x0c\x64\x65\x66\x61ultValue\x18\x0c \x01(\t\x12\x13\n\x0b\x64\x65scription\x18\r \x01(\t\x12\x11\n\tpositionX\x18\x0e \x01(\x05\x12\x11\n\tpositionY\x18\x0f \x01(\x05\x12\x0e\n\x06height\x18\x10 \x01(\x05\x12\r\n\x05width\x18\x11 \x01(\x05\x12!\n\x0bstyleCursor\x18\x12 \x01(\x0b\x32\x0c.uggly.Style\x12\x1f\n\tstyleFill\x18\x13 \x01(\x0b\x32\x0c.uggly.Style\x12\x1f\n\tstyleText\x18\x14 \x01(\x0b\x32\x0c.uggly.Style\x12&\n\x10styleDescription\x18\x15 \x01(\x0b\x32\x0c.uggly.Style\x12\x17\n\x0fshowDescription\x18\x16 \x01(\x08\x12\x10\n\x08password\x18\x17 \x01(\x08\"i\n\x04\x46orm\x12\x0c\n\x04name\x18\n \x01(\t\x12\x0f\n\x07\x64ivName\x18\x0b \x01(\t\x12!\n\ttextBoxes\x18\x0c \x03(\x0b\x32\x0e.uggly.TextBox\x12\x1f\n\nsubmitLink\x18\r \x01(\x0b\x32\x0b.uggly.Link\"A\n\x08\x46ormData\x12\x0c\n\x04name\x18\n \x01(\t\x12\'\n\x0btextBoxData\x18\x0b \x03(\x0b\x32\x12.uggly.TextBoxData\"-\n\x0bTextBoxData\x12\x0c\n\x04name\x18\n \x01(\t\x12\x10\n\x08\x63ontents\x18\x0b \x01(\t\"J\n\x08\x45lements\x12\"\n\ttextBlobs\x18\n \x03(\x0b\x32\x0f.uggly.TextBlob\x12\x1a\n\x05\x66orms\x18\x0b \x03(\x0b\x32\x0b.uggly.Form\"0\n\x0bPageListing\x12\x0c\n\x04name\x18\n \x01(\t\x12\x13\n\x0b\x64\x65scription\x18\x0b \x01(\t\"\xc2\x01\n\x0cPageResponse\x12!\n\x08\x64ivBoxes\x18\n \x01(\x0b\x32\x0f.uggly.DivBoxes\x12!\n\x08\x65lements\x18\x0b \x01(\x0b\x32\x0f.uggly.Elements\x12\x0c\n\x04name\x18\x0c \x01(\t\x12$\n\nkeyStrokes\x18\r \x03(\x0b\x32\x10.uggly.KeyStroke\x12!\n\nsetCookies\x18\x0e \x03(\x0b\x32\r.uggly.Cookie\x12\x15\n\rstreamDelayMs\x18\x0f \x01(\x05\"\xd2\x01\n\x06\x43ookie\x12\x0b\n\x03key\x18\n \x01(\t\x12\r\n\x05value\x18\x0b \x01(\t\x12\x0e\n\x06server\x18\x0c \x01(\t\x12\x0f\n\x07private\x18\r \x01(\x08\x12\x0f\n\x07\x65xpires\x18\x0e \x01(\t\x12(\n\x08sameSite\x18\x0f \x01(\x0e\x32\x16.uggly.Cookie.SameSite\x12\x0c\n\x04page\x18\x10 \x01(\t\x12\x0e\n\x06secure\x18\x11 \x01(\x08\x12\x10\n\x08metadata\x18\x12 \x01(\x08\" \n\x08SameSite\x12\n\n\x06STRICT\x10\x00\x12\x08\n\x04NONE\x10\x01\"\xcb\x01\n\x0bPageRequest\x12\x0c\n\x04name\x18\n \x01(\t\x12\x13\n\x0b\x63lientWidth\x18\x0b \x01(\x05\x12\x14\n\x0c\x63lientHeight\x18\x0c \x01(\x05\x12!\n\x08\x66ormData\x18\r \x03(\x0b\x32\x0f.uggly.FormData\x12\x0e\n\x06server\x18\x0e \x01(\t\x12\x0c\n\x04port\x18\x0f \x01(\t\x12\x0e\n\x06secure\x18\x10 \x01(\x08\x12\"\n\x0bsendCookies\x18\x11 \x03(\x0b\x32\r.uggly.Cookie\x12\x0e\n\x06stream\x18\x12 \x01(\x08\"@\n\x0c\x46\x65\x65\x64Response\x12!\n\x05pages\x18\n \x03(\x0b\x32\x12.uggly.PageListing\x12\r\n\x05notes\x18\x0b \x01(\t\"\x1f\n\x0b\x46\x65\x65\x64Request\x12\x10\n\x08sendData\x18\n \x01(\x08\x32<\n\x04\x46\x65\x65\x64\x12\x34\n\x07GetFeed\x12\x12.uggly.FeedRequest\x1a\x13.uggly.FeedResponse\"\x00\x32z\n\x04Page\x12\x34\n\x07GetPage\x12\x12.uggly.PageRequest\x1a\x13.uggly.PageResponse\"\x00\x12<\n\rGetPageStream\x12\x12.uggly.PageRequest\x1a\x13.uggly.PageResponse\"\x00\x30\x01\x42\x1cZ\x1agithub.com/rendicott/ugglyb\x06proto3')



_PIXEL = DESCRIPTOR.message_types_by_name['Pixel']
_DIVBOX = DESCRIPTOR.message_types_by_name['DivBox']
_TEXTBLOB = DESCRIPTOR.message_types_by_name['TextBlob']
_DIVBOXES = DESCRIPTOR.message_types_by_name['DivBoxes']
_STYLE = DESCRIPTOR.message_types_by_name['Style']
_LINK = DESCRIPTOR.message_types_by_name['Link']
_DIVSCROLL = DESCRIPTOR.message_types_by_name['DivScroll']
_FORMACTIVATION = DESCRIPTOR.message_types_by_name['FormActivation']
_KEYSTROKE = DESCRIPTOR.message_types_by_name['KeyStroke']
_TEXTBOX = DESCRIPTOR.message_types_by_name['TextBox']
_FORM = DESCRIPTOR.message_types_by_name['Form']
_FORMDATA = DESCRIPTOR.message_types_by_name['FormData']
_TEXTBOXDATA = DESCRIPTOR.message_types_by_name['TextBoxData']
_ELEMENTS = DESCRIPTOR.message_types_by_name['Elements']
_PAGELISTING = DESCRIPTOR.message_types_by_name['PageListing']
_PAGERESPONSE = DESCRIPTOR.message_types_by_name['PageResponse']
_COOKIE = DESCRIPTOR.message_types_by_name['Cookie']
_PAGEREQUEST = DESCRIPTOR.message_types_by_name['PageRequest']
_FEEDRESPONSE = DESCRIPTOR.message_types_by_name['FeedResponse']
_FEEDREQUEST = DESCRIPTOR.message_types_by_name['FeedRequest']
_COOKIE_SAMESITE = _COOKIE.enum_types_by_name['SameSite']
Pixel = _reflection.GeneratedProtocolMessageType('Pixel', (_message.Message,), {
  'DESCRIPTOR' : _PIXEL,
  '__module__' : 'uggly_pb2'
  # @@protoc_insertion_point(class_scope:uggly.Pixel)
  })
_sym_db.RegisterMessage(Pixel)

DivBox = _reflection.GeneratedProtocolMessageType('DivBox', (_message.Message,), {
  'DESCRIPTOR' : _DIVBOX,
  '__module__' : 'uggly_pb2'
  # @@protoc_insertion_point(class_scope:uggly.DivBox)
  })
_sym_db.RegisterMessage(DivBox)

TextBlob = _reflection.GeneratedProtocolMessageType('TextBlob', (_message.Message,), {
  'DESCRIPTOR' : _TEXTBLOB,
  '__module__' : 'uggly_pb2'
  # @@protoc_insertion_point(class_scope:uggly.TextBlob)
  })
_sym_db.RegisterMessage(TextBlob)

DivBoxes = _reflection.GeneratedProtocolMessageType('DivBoxes', (_message.Message,), {
  'DESCRIPTOR' : _DIVBOXES,
  '__module__' : 'uggly_pb2'
  # @@protoc_insertion_point(class_scope:uggly.DivBoxes)
  })
_sym_db.RegisterMessage(DivBoxes)

Style = _reflection.GeneratedProtocolMessageType('Style', (_message.Message,), {
  'DESCRIPTOR' : _STYLE,
  '__module__' : 'uggly_pb2'
  # @@protoc_insertion_point(class_scope:uggly.Style)
  })
_sym_db.RegisterMessage(Style)

Link = _reflection.GeneratedProtocolMessageType('Link', (_message.Message,), {
  'DESCRIPTOR' : _LINK,
  '__module__' : 'uggly_pb2'
  # @@protoc_insertion_point(class_scope:uggly.Link)
  })
_sym_db.RegisterMessage(Link)

DivScroll = _reflection.GeneratedProtocolMessageType('DivScroll', (_message.Message,), {
  'DESCRIPTOR' : _DIVSCROLL,
  '__module__' : 'uggly_pb2'
  # @@protoc_insertion_point(class_scope:uggly.DivScroll)
  })
_sym_db.RegisterMessage(DivScroll)

FormActivation = _reflection.GeneratedProtocolMessageType('FormActivation', (_message.Message,), {
  'DESCRIPTOR' : _FORMACTIVATION,
  '__module__' : 'uggly_pb2'
  # @@protoc_insertion_point(class_scope:uggly.FormActivation)
  })
_sym_db.RegisterMessage(FormActivation)

KeyStroke = _reflection.GeneratedProtocolMessageType('KeyStroke', (_message.Message,), {
  'DESCRIPTOR' : _KEYSTROKE,
  '__module__' : 'uggly_pb2'
  # @@protoc_insertion_point(class_scope:uggly.KeyStroke)
  })
_sym_db.RegisterMessage(KeyStroke)

TextBox = _reflection.GeneratedProtocolMessageType('TextBox', (_message.Message,), {
  'DESCRIPTOR' : _TEXTBOX,
  '__module__' : 'uggly_pb2'
  # @@protoc_insertion_point(class_scope:uggly.TextBox)
  })
_sym_db.RegisterMessage(TextBox)

Form = _reflection.GeneratedProtocolMessageType('Form', (_message.Message,), {
  'DESCRIPTOR' : _FORM,
  '__module__' : 'uggly_pb2'
  # @@protoc_insertion_point(class_scope:uggly.Form)
  })
_sym_db.RegisterMessage(Form)

FormData = _reflection.GeneratedProtocolMessageType('FormData', (_message.Message,), {
  'DESCRIPTOR' : _FORMDATA,
  '__module__' : 'uggly_pb2'
  # @@protoc_insertion_point(class_scope:uggly.FormData)
  })
_sym_db.RegisterMessage(FormData)

TextBoxData = _reflection.GeneratedProtocolMessageType('TextBoxData', (_message.Message,), {
  'DESCRIPTOR' : _TEXTBOXDATA,
  '__module__' : 'uggly_pb2'
  # @@protoc_insertion_point(class_scope:uggly.TextBoxData)
  })
_sym_db.RegisterMessage(TextBoxData)

Elements = _reflection.GeneratedProtocolMessageType('Elements', (_message.Message,), {
  'DESCRIPTOR' : _ELEMENTS,
  '__module__' : 'uggly_pb2'
  # @@protoc_insertion_point(class_scope:uggly.Elements)
  })
_sym_db.RegisterMessage(Elements)

PageListing = _reflection.GeneratedProtocolMessageType('PageListing', (_message.Message,), {
  'DESCRIPTOR' : _PAGELISTING,
  '__module__' : 'uggly_pb2'
  # @@protoc_insertion_point(class_scope:uggly.PageListing)
  })
_sym_db.RegisterMessage(PageListing)

PageResponse = _reflection.GeneratedProtocolMessageType('PageResponse', (_message.Message,), {
  'DESCRIPTOR' : _PAGERESPONSE,
  '__module__' : 'uggly_pb2'
  # @@protoc_insertion_point(class_scope:uggly.PageResponse)
  })
_sym_db.RegisterMessage(PageResponse)

Cookie = _reflection.GeneratedProtocolMessageType('Cookie', (_message.Message,), {
  'DESCRIPTOR' : _COOKIE,
  '__module__' : 'uggly_pb2'
  # @@protoc_insertion_point(class_scope:uggly.Cookie)
  })
_sym_db.RegisterMessage(Cookie)

PageRequest = _reflection.GeneratedProtocolMessageType('PageRequest', (_message.Message,), {
  'DESCRIPTOR' : _PAGEREQUEST,
  '__module__' : 'uggly_pb2'
  # @@protoc_insertion_point(class_scope:uggly.PageRequest)
  })
_sym_db.RegisterMessage(PageRequest)

FeedResponse = _reflection.GeneratedProtocolMessageType('FeedResponse', (_message.Message,), {
  'DESCRIPTOR' : _FEEDRESPONSE,
  '__module__' : 'uggly_pb2'
  # @@protoc_insertion_point(class_scope:uggly.FeedResponse)
  })
_sym_db.RegisterMessage(FeedResponse)

FeedRequest = _reflection.GeneratedProtocolMessageType('FeedRequest', (_message.Message,), {
  'DESCRIPTOR' : _FEEDREQUEST,
  '__module__' : 'uggly_pb2'
  # @@protoc_insertion_point(class_scope:uggly.FeedRequest)
  })
_sym_db.RegisterMessage(FeedRequest)

_FEED = DESCRIPTOR.services_by_name['Feed']
_PAGE = DESCRIPTOR.services_by_name['Page']
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  DESCRIPTOR._serialized_options = b'Z\032github.com/rendicott/uggly'
  _PIXEL._serialized_start=22
  _PIXEL._serialized_end=84
  _DIVBOX._serialized_start=87
  _DIVBOX._serialized_end=335
  _TEXTBLOB._serialized_start=337
  _TEXTBLOB._serialized_end=425
  _DIVBOXES._serialized_start=427
  _DIVBOXES._serialized_end=467
  _STYLE._serialized_start=469
  _STYLE._serialized_end=514
  _LINK._serialized_start=516
  _LINK._serialized_end=621
  _DIVSCROLL._serialized_start=623
  _DIVSCROLL._serialized_end=665
  _FORMACTIVATION._serialized_start=667
  _FORMACTIVATION._serialized_end=701
  _KEYSTROKE._serialized_start=704
  _KEYSTROKE._serialized_end=861
  _TEXTBOX._serialized_start=864
  _TEXTBOX._serialized_end=1201
  _FORM._serialized_start=1203
  _FORM._serialized_end=1308
  _FORMDATA._serialized_start=1310
  _FORMDATA._serialized_end=1375
  _TEXTBOXDATA._serialized_start=1377
  _TEXTBOXDATA._serialized_end=1422
  _ELEMENTS._serialized_start=1424
  _ELEMENTS._serialized_end=1498
  _PAGELISTING._serialized_start=1500
  _PAGELISTING._serialized_end=1548
  _PAGERESPONSE._serialized_start=1551
  _PAGERESPONSE._serialized_end=1745
  _COOKIE._serialized_start=1748
  _COOKIE._serialized_end=1958
  _COOKIE_SAMESITE._serialized_start=1926
  _COOKIE_SAMESITE._serialized_end=1958
  _PAGEREQUEST._serialized_start=1961
  _PAGEREQUEST._serialized_end=2164
  _FEEDRESPONSE._serialized_start=2166
  _FEEDRESPONSE._serialized_end=2230
  _FEEDREQUEST._serialized_start=2232
  _FEEDREQUEST._serialized_end=2263
  _FEED._serialized_start=2265
  _FEED._serialized_end=2325
  _PAGE._serialized_start=2327
  _PAGE._serialized_end=2449
# @@protoc_insertion_point(module_scope)
