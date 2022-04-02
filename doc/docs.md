# Protocol Documentation
<a name="top"></a>

## Table of Contents

- [uggly.proto](#uggly-proto)
    - [DivBox](#uggly-DivBox)
    - [DivBoxes](#uggly-DivBoxes)
    - [Elements](#uggly-Elements)
    - [FeedRequest](#uggly-FeedRequest)
    - [FeedResponse](#uggly-FeedResponse)
    - [Form](#uggly-Form)
    - [FormData](#uggly-FormData)
    - [Link](#uggly-Link)
    - [PageListing](#uggly-PageListing)
    - [PageRequest](#uggly-PageRequest)
    - [PageResponse](#uggly-PageResponse)
    - [Pixel](#uggly-Pixel)
    - [PixelSlice](#uggly-PixelSlice)
    - [Style](#uggly-Style)
    - [TextBlob](#uggly-TextBlob)
    - [TextBox](#uggly-TextBox)
    - [TextBoxData](#uggly-TextBoxData)
  
    - [Feed](#uggly-Feed)
    - [Page](#uggly-Page)
  
- [Scalar Value Types](#scalar-value-types)



<a name="uggly-proto"></a>
<p align="right"><a href="#top">Top</a></p>

## uggly.proto



<a name="uggly-DivBox"></a>

### DivBox
DivBox is a core element of the protocol. No content can exist
outside of a DivBox. It requires that some basic properties are included
such as fill and border geometry but the rawContents property is open
to fill with whatever content is desired.


| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| name | [string](#string) |  |  |
| border | [bool](#bool) |  |  |
| borderW | [int32](#int32) |  |  |
| borderChar | [int32](#int32) |  |  |
| fillChar | [int32](#int32) |  |  |
| startX | [int32](#int32) |  |  |
| startY | [int32](#int32) |  |  |
| width | [int32](#int32) |  |  |
| Height | [int32](#int32) |  |  |
| rawContents | [PixelSlice](#uggly-PixelSlice) | repeated |  |
| borderSt | [Style](#uggly-Style) |  |  |
| fillSt | [Style](#uggly-Style) |  |  |






<a name="uggly-DivBoxes"></a>

### DivBoxes
DivBoxes is an array of DivBox


| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| boxes | [DivBox](#uggly-DivBox) | repeated |  |






<a name="uggly-Elements"></a>

### Elements



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| textBlobs | [TextBlob](#uggly-TextBlob) | repeated |  |
| forms | [Form](#uggly-Form) | repeated |  |






<a name="uggly-FeedRequest"></a>

### FeedRequest



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| sendData | [bool](#bool) |  |  |






<a name="uggly-FeedResponse"></a>

### FeedResponse



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| pages | [PageListing](#uggly-PageListing) | repeated |  |
| notes | [string](#string) |  |  |






<a name="uggly-Form"></a>

### Form



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| name | [string](#string) |  |  |
| divName | [string](#string) |  |  |
| textBoxes | [TextBox](#uggly-TextBox) | repeated |  |
| submitLink | [Link](#uggly-Link) |  |  |






<a name="uggly-FormData"></a>

### FormData



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| name | [string](#string) |  |  |
| textBoxData | [TextBoxData](#uggly-TextBoxData) | repeated |  |






<a name="uggly-Link"></a>

### Link



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| keyStroke | [string](#string) |  |  |
| pageName | [string](#string) |  |  |
| server | [string](#string) |  |  |
| port | [string](#string) |  |  |
| formName | [string](#string) |  |  |






<a name="uggly-PageListing"></a>

### PageListing



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| name | [string](#string) |  |  |






<a name="uggly-PageRequest"></a>

### PageRequest



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| name | [string](#string) |  |  |
| clientWidth | [int32](#int32) |  |  |
| clientHeight | [int32](#int32) |  |  |
| formData | [FormData](#uggly-FormData) | repeated |  |






<a name="uggly-PageResponse"></a>

### PageResponse



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| divBoxes | [DivBoxes](#uggly-DivBoxes) |  |  |
| elements | [Elements](#uggly-Elements) |  |  |
| name | [string](#string) |  |  |
| links | [Link](#uggly-Link) | repeated |  |






<a name="uggly-Pixel"></a>

### Pixel



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| c | [int32](#int32) |  |  |
| st | [Style](#uggly-Style) |  |  |
| isBorder | [bool](#bool) |  |  |






<a name="uggly-PixelSlice"></a>

### PixelSlice



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| pixels | [Pixel](#uggly-Pixel) | repeated |  |






<a name="uggly-Style"></a>

### Style
Style is a base property used in divBox fill, border fill, and textboxes
with fg being foreground color, bg being background color, and attr
being text attributes like strikethrough and underline.

It&#39;s essentially a passthrough of the capabilities of tcell&#39;s style
https://github.com/gdamore/tcell/blob/master/style.go


| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| fg | [string](#string) |  |  |
| bg | [string](#string) |  |  |
| attr | [string](#string) |  |  |






<a name="uggly-TextBlob"></a>

### TextBlob
TextBlob is a special kind of element that natively understands
text blocks intended for human readability. Obviously it has a content
property but also understands things like text style and text wrap when 
the text is larger than the width of the container it was assigned to. 

A TextBlob can be assigned to multiple Divs in case you wanted to re-use
text in multiple places for some reason.


| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| content | [string](#string) |  |  |
| wrap | [bool](#bool) |  |  |
| style | [Style](#uggly-Style) |  |  |
| divNames | [string](#string) | repeated |  |






<a name="uggly-TextBox"></a>

### TextBox



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| name | [string](#string) |  |  |
| tabOrder | [int32](#int32) |  |  |
| defaultValue | [string](#string) |  |  |
| description | [string](#string) |  |  |
| positionX | [int32](#int32) |  | relative within DivBox |
| positionY | [int32](#int32) |  | relative within DivBox |
| height | [int32](#int32) |  |  |
| width | [int32](#int32) |  |  |
| styleCursor | [Style](#uggly-Style) |  |  |
| styleFill | [Style](#uggly-Style) |  |  |
| styleText | [Style](#uggly-Style) |  |  |
| styleDescription | [Style](#uggly-Style) |  |  |
| showDescription | [bool](#bool) |  |  |






<a name="uggly-TextBoxData"></a>

### TextBoxData



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| name | [string](#string) |  |  |
| contents | [string](#string) |  |  |





 

 

 


<a name="uggly-Feed"></a>

### Feed


| Method Name | Request Type | Response Type | Description |
| ----------- | ------------ | ------------- | ------------|
| GetFeed | [FeedRequest](#uggly-FeedRequest) | [FeedResponse](#uggly-FeedResponse) |  |


<a name="uggly-Page"></a>

### Page


| Method Name | Request Type | Response Type | Description |
| ----------- | ------------ | ------------- | ------------|
| GetPage | [PageRequest](#uggly-PageRequest) | [PageResponse](#uggly-PageResponse) |  |

 



## Scalar Value Types

| .proto Type | Notes | C++ | Java | Python | Go | C# | PHP | Ruby |
| ----------- | ----- | --- | ---- | ------ | -- | -- | --- | ---- |
| <a name="double" /> double |  | double | double | float | float64 | double | float | Float |
| <a name="float" /> float |  | float | float | float | float32 | float | float | Float |
| <a name="int32" /> int32 | Uses variable-length encoding. Inefficient for encoding negative numbers – if your field is likely to have negative values, use sint32 instead. | int32 | int | int | int32 | int | integer | Bignum or Fixnum (as required) |
| <a name="int64" /> int64 | Uses variable-length encoding. Inefficient for encoding negative numbers – if your field is likely to have negative values, use sint64 instead. | int64 | long | int/long | int64 | long | integer/string | Bignum |
| <a name="uint32" /> uint32 | Uses variable-length encoding. | uint32 | int | int/long | uint32 | uint | integer | Bignum or Fixnum (as required) |
| <a name="uint64" /> uint64 | Uses variable-length encoding. | uint64 | long | int/long | uint64 | ulong | integer/string | Bignum or Fixnum (as required) |
| <a name="sint32" /> sint32 | Uses variable-length encoding. Signed int value. These more efficiently encode negative numbers than regular int32s. | int32 | int | int | int32 | int | integer | Bignum or Fixnum (as required) |
| <a name="sint64" /> sint64 | Uses variable-length encoding. Signed int value. These more efficiently encode negative numbers than regular int64s. | int64 | long | int/long | int64 | long | integer/string | Bignum |
| <a name="fixed32" /> fixed32 | Always four bytes. More efficient than uint32 if values are often greater than 2^28. | uint32 | int | int | uint32 | uint | integer | Bignum or Fixnum (as required) |
| <a name="fixed64" /> fixed64 | Always eight bytes. More efficient than uint64 if values are often greater than 2^56. | uint64 | long | int/long | uint64 | ulong | integer/string | Bignum |
| <a name="sfixed32" /> sfixed32 | Always four bytes. | int32 | int | int | int32 | int | integer | Bignum or Fixnum (as required) |
| <a name="sfixed64" /> sfixed64 | Always eight bytes. | int64 | long | int/long | int64 | long | integer/string | Bignum |
| <a name="bool" /> bool |  | bool | boolean | boolean | bool | bool | boolean | TrueClass/FalseClass |
| <a name="string" /> string | A string must always contain UTF-8 encoded or 7-bit ASCII text. | string | String | str/unicode | string | string | string | String (UTF-8) |
| <a name="bytes" /> bytes | May contain any arbitrary sequence of bytes. | string | ByteString | str | []byte | ByteString | string | String (ASCII-8BIT) |

