# Protocol Documentation
<a name="top"></a>

## Table of Contents

- [uggly.proto](#uggly-proto)
    - [Cookie](#uggly-Cookie)
    - [DivBox](#uggly-DivBox)
    - [DivBoxes](#uggly-DivBoxes)
    - [DivScroll](#uggly-DivScroll)
    - [Elements](#uggly-Elements)
    - [FeedRequest](#uggly-FeedRequest)
    - [FeedResponse](#uggly-FeedResponse)
    - [Form](#uggly-Form)
    - [FormActivation](#uggly-FormActivation)
    - [FormData](#uggly-FormData)
    - [KeyStroke](#uggly-KeyStroke)
    - [Link](#uggly-Link)
    - [PageListing](#uggly-PageListing)
    - [PageRequest](#uggly-PageRequest)
    - [PageResponse](#uggly-PageResponse)
    - [Style](#uggly-Style)
    - [TextBlob](#uggly-TextBlob)
    - [TextBox](#uggly-TextBox)
    - [TextBoxData](#uggly-TextBoxData)
  
    - [Cookie.SameSite](#uggly-Cookie-SameSite)
  
    - [Feed](#uggly-Feed)
    - [Page](#uggly-Page)
  
- [Scalar Value Types](#scalar-value-types)



<a name="uggly-proto"></a>
<p align="right"><a href="#top">Top</a></p>

## uggly.proto



<a name="uggly-Cookie"></a>

### Cookie
Cookie loosly follows the cookie spec (https://developer.mozilla.org/en-US/docs/Web/HTTP/Headers/Set-Cookie)
but does not include protections for browser side code as today the uggly spec does not support
client side code.


| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| key | [string](#string) |  | standard key or field name of cookie |
| value | [string](#string) |  | standard value of cookie |
| server | [string](#string) |  | the server which requested this cookie to be set. should be server only without including port e.g., &#34;localhost&#34; or &#34;mysubdomain.domain.com&#34; |
| private | [bool](#bool) |  | private Cookies will never be sent back to server |
| expires | [string](#string) |  | date when cookie expires relative to client in RFC1123 format. If improperly formatted will just be ignored and cookie will be treated as session cookie. |
| sameSite | [Cookie.SameSite](#uggly-Cookie-SameSite) |  |  |
| page | [string](#string) |  | if this cookie should only be sent back on specific pages |
| secure | [bool](#bool) |  | if this cookie should only be sent when connection is secure |
| metadata | [bool](#bool) |  | indicates that this cookie should be sent in header metadata instead of body. This is useful if the server wants to pre-filter traffic, for example if a request is not authenticated it can avoid processing the full PageRequest |






<a name="uggly-DivBox"></a>

### DivBox
DivBox is a core element of the protocol. No content can exist
outside of a DivBox. It requires that some basic properties are included
such as fill and border geometry but the rawContents property is open
to fill with whatever content is desired.


| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| name | [string](#string) |  | the name of the divBox. Used when attaching TextBlobs and forms |
| border | [bool](#bool) |  | whether the div should add a border |
| borderW | [int32](#int32) |  | the width of the border, will stay inside the stated overall dimensions and work its way inward |
| borderChar | [int32](#int32) |  | The character to use as a border character (e.g., &#34;*&#34;) but represented as rune For example, in Python this would be &#39;ord(&#34;*&#34;)&#39; and Go it would be []rune(&#34;*&#34;)[0] |
| fillChar | [int32](#int32) |  | if the DivBox should be filled with a char as a texture. Follows same rune rules as borderChar. |
| startX | [int32](#int32) |  | position on the X axis where the box should start |
| startY | [int32](#int32) |  | position on the Y acis where the box should start |
| width | [int32](#int32) |  | overall width of the box |
| Height | [int32](#int32) |  | overall height of the box |
| borderSt | [Style](#uggly-Style) |  | style to use when rendering border char |
| fillSt | [Style](#uggly-Style) |  | style to use when rendering fill char |






<a name="uggly-DivBoxes"></a>

### DivBoxes
DivBoxes is an array of DivBox


| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| boxes | [DivBox](#uggly-DivBox) | repeated |  |






<a name="uggly-DivScroll"></a>

### DivScroll
If a KeyStroke is of type DivScroll
then this contains information about which
DivBox to scroll and whether or not the direction
is down = true or down = false (e.g., &#39;up&#39;)

WARNING: Not currently implemented in &#39;uggly-client&#39;


| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| divName | [string](#string) |  |  |
| down | [bool](#bool) |  |  |






<a name="uggly-Elements"></a>

### Elements
Elements contains all non-DivBox related
content that could be included in a PageResponse.
Right now this contains TextBlobs and Forms
but will be used for future elements if needed. 
For example, if determined that clients should
handle all Table rendering in the future or something.
Right now tables would have to be stick built by 
the server using DivBoxes and TextBlobs


| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| textBlobs | [TextBlob](#uggly-TextBlob) | repeated |  |
| forms | [Form](#uggly-Form) | repeated |  |






<a name="uggly-FeedRequest"></a>

### FeedRequest
A FeedRequest really needs no properties
as it&#39;s just a call from the client for the
server to send a Feed if it has one.


| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| sendData | [bool](#bool) |  | reserved for future use |






<a name="uggly-FeedResponse"></a>

### FeedResponse
A FeedResponse is essentially a list of 
Pages that the server wishes to expose
to the client. The server can obviously choose
to hide some Pages or if it generates Pages
dynamically it may not even be able to provide
an accurate listing.


| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| pages | [PageListing](#uggly-PageListing) | repeated |  |
| notes | [string](#string) |  | reserved for future use |






<a name="uggly-Form"></a>

### Form
The Form is sent by the server to the client
as part of the PageResponse. It contains
the Form name, the DivBox it should be placed
within (TextBox PositionX and Y coordinates
are relative to the containing DivBox) and a 
list of the TextBox&#39;s included in this form.
It also supports a parameter for a Link that can
be used as a return address when this Form is 
submitted in a PageRequest


| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| name | [string](#string) |  | The name of the form. This will be used in formActivation keystrokes and for atributing formData in PageRequests |
| divName | [string](#string) |  | the DivName that the form should be rendered within. All of the elements of the form will be rendered relative to this divBox |
| textBoxes | [TextBox](#uggly-TextBox) | repeated | The textboxes to be included in this form |
| submitLink | [Link](#uggly-Link) |  | The link that this form will call when the form&#39;s submit action (e.g., &#39;enter&#39;) is triggered |






<a name="uggly-FormActivation"></a>

### FormActivation
If a KeyStroke is of type FormActivation
then this contains the name of the form which
should be activated for that keystroke


| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| formName | [string](#string) |  |  |






<a name="uggly-FormData"></a>

### FormData
FormData contains the form name and any
TextBoxData that was in the form when
the FormData was sent in the PageRequest


| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| name | [string](#string) |  |  |
| textBoxData | [TextBoxData](#uggly-TextBoxData) | repeated |  |






<a name="uggly-KeyStroke"></a>

### KeyStroke
KeyStroke indicates an action that will be executed when the keyStroke
is prssed by the client. This could be one of Link (e.g., new PageRequest),
DivScroll (indicates the client should attempt to re-render textblobs that 
exceed their containing DivBox&#39;s capacity), or FormActivation which would 
look for a form with the given name on the client&#39;s current page.


| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| keyStroke | [string](#string) |  | a string representation of a key on a keyboard. For rune keys (e.g., &#34;j&#34;) simply use the single character. For more complex keys refer to the string representation from the tcell package: https://github.com/gdamore/tcell/blob/master/key.go#L83 

The client may have certain keys reserved that will never be honored. In the current &#34;uggly-client&#34; this includes: F1, F2, F3, F4, F5, F6, F7, and F10 |
| link | [Link](#uggly-Link) |  |  |
| divScroll | [DivScroll](#uggly-DivScroll) |  |  |
| formActivation | [FormActivation](#uggly-FormActivation) |  |  |






<a name="uggly-Link"></a>

### Link
Link contains information about keyboard shortcuts
and destinations for actions. The client will determine
from context whether a Link is to a server page or is 
to be used to pass polling context to a Form that it
already receieved in a PageResponse.


| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| keyStroke | [string](#string) |  | a repeat of the keystroke used in the parent KeyStroke TODO: not sure what happens if they don&#39;t match |
| pageName | [string](#string) |  | the name of the page to be requested in the new PageRequest |
| server | [string](#string) |  | the server to be used in the new PageRequest |
| port | [string](#string) |  | the port to be used in the new PageRequest |
| secure | [bool](#bool) |  | whether or not the new PageRequest should be secure (TLS) |
| stream | [bool](#bool) |  | whether or not the new PageRequest is a stream |






<a name="uggly-PageListing"></a>

### PageListing
A PageListing is basically a key/value
pair of page name and an optional 
description. The client can choose to render
this however it wants and the client injects
it&#39;s own &#34;links&#34; to this content. This is a
lazy way of exposing all the server&#39;s content
without having to build nav menus and manage
links


| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| name | [string](#string) |  |  |
| description | [string](#string) |  |  |






<a name="uggly-PageRequest"></a>

### PageRequest
A PageRequest contains the name of the 
desired page and some metadata about the
cient height and width. The server can choose
to ignore the width and height if it insists 
on statically sized content. Also, the server could
generate a PageResponse saying something like 
&#34;this server insists on a minimum height to view
content&#34; for example.


| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| name | [string](#string) |  | The name of the page being requested |
| clientWidth | [int32](#int32) |  | The width of the client at the time of the request |
| clientHeight | [int32](#int32) |  | The height of the client at the time of the request |
| formData | [FormData](#uggly-FormData) | repeated | data from form submissions or could be used to send generic key value pairs |
| server | [string](#string) |  | the intended server for the request |
| port | [string](#string) |  | the intended port for the request |
| secure | [bool](#bool) |  | whether or not the connection should be secure (TLS) |
| sendCookies | [Cookie](#uggly-Cookie) | repeated | Cookies that are intended to be sent from client to server |
| stream | [bool](#bool) |  | whether or not the request is for a page stream |






<a name="uggly-PageResponse"></a>

### PageResponse
The PageResponse contains modular content
that the server wishes the client to display
in the form of DivBoxes, Elements, and Links.


| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| divBoxes | [DivBoxes](#uggly-DivBoxes) |  | divBoxes contains all of the divBoxes to be rendered for this page |
| elements | [Elements](#uggly-Elements) |  | elements contains all of the non divBox elements to be rendered for this page |
| name | [string](#string) |  | the name of the page to be rendered |
| keyStrokes | [KeyStroke](#uggly-KeyStroke) | repeated | a list of keystrokes that the client should honor, these could be of type link, formActivation, or divScroll |
| setCookies | [Cookie](#uggly-Cookie) | repeated | any cookies that the server is requesting the client to set for future requests |
| streamDelayMs | [int32](#int32) |  | if the response is part of a stream then this is the time in milliseconds the client should wait before drawing the next request |






<a name="uggly-Style"></a>

### Style
Style is a base property used in divBox fill, border fill, and textboxes
with fg being foreground color, bg being background color, and attr
being text attributes like strikethrough and underline.

It&#39;s essentially a passthrough of the capabilities of tcell&#39;s style
https://github.com/gdamore/tcell/blob/master/style.go


| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| fg | [string](#string) |  | a string representation of the color for the foreground (i.e., text) |
| bg | [string](#string) |  | a string representation of the color for the background |
| attr | [string](#string) |  | attr would be things like underline or bold if the client terminal supports it. Experimentation with this has proven that &#39;4&#39; is the only dependable value |






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
| content | [string](#string) |  | The actual content. Could be almost any length but be aware of the size of the containing div. |
| wrap | [bool](#bool) |  | whether or not the text should wrap if it exceeds the width of it&#39;s divbox |
| style | [Style](#uggly-Style) |  |  |
| divNames | [string](#string) | repeated | the divs this text should be attached to. Generally it&#39;s just one. |






<a name="uggly-TextBox"></a>

### TextBox
TextBox contains the properties sent by the server
for the client to render.


| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| name | [string](#string) |  | the name of this textBox. Will be used as the key in the key:value during submission |
| tabOrder | [int32](#int32) |  | the order in which this field will activate when user is tabbing through form fields |
| defaultValue | [string](#string) |  | the default value that will be placed in the box |
| description | [string](#string) |  | a description of the text box (e.g., &#34;passwords should include special chars&#34;) which can optionally be drawn to the left of the textbox |
| positionX | [int32](#int32) |  | relative within DivBox |
| positionY | [int32](#int32) |  | relative within DivBox |
| height | [int32](#int32) |  | currently textBoxes only utilize a single line |
| width | [int32](#int32) |  | text that goes beyond the width will horozontially scroll to fit |
| styleCursor | [Style](#uggly-Style) |  | style for the cursor within the box. ForeGround color is meaningless |
| styleFill | [Style](#uggly-Style) |  | style for the box fill or background. Foreground and Background should probably match styleText so as not to clash |
| styleText | [Style](#uggly-Style) |  | style of the text that is being typed into box. |
| styleDescription | [Style](#uggly-Style) |  | style for the description that is rendered to the left of the box |
| showDescription | [bool](#bool) |  | whether or not to render the description. Design consideration: This will be rendered as far to the left of the textBox&#39;s positionX attribute as to fit the description. |
| password | [bool](#bool) |  | whether or not this field is a password, e.g, it&#39;s contents will be hidden while typing |






<a name="uggly-TextBoxData"></a>

### TextBoxData
TextBoxData contains the text box&#39;s field
name and whatever contents were in it
when the PageRequest was sent with FormData


| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| name | [string](#string) |  |  |
| contents | [string](#string) |  |  |





 


<a name="uggly-Cookie-SameSite"></a>

### Cookie.SameSite


| Name | Number | Description |
| ---- | ------ | ----------- |
| STRICT | 0 | cookie only sent to same site that set it |
| NONE | 1 | cookie can be sent cross site but only if Secure is set |


 

 


<a name="uggly-Feed"></a>

### Feed
Feed service can be implemented by the server
and must provide a FeedResponse for a given FeedRequest.
This is to be used as somewhat of a server index of 
available Pages when the server chooses to implement.
It is strongly encouraged to implement a Feed because
it makes for quality of life improvements for the client&#39;s
user

| Method Name | Request Type | Response Type | Description |
| ----------- | ------------ | ------------- | ------------|
| GetFeed | [FeedRequest](#uggly-FeedRequest) | [FeedResponse](#uggly-FeedResponse) |  |


<a name="uggly-Page"></a>

### Page
In order for a server to serve any content it must 
implement the Page service which returns PageResponse
for a given PageRequest

| Method Name | Request Type | Response Type | Description |
| ----------- | ------------ | ------------- | ------------|
| GetPage | [PageRequest](#uggly-PageRequest) | [PageResponse](#uggly-PageResponse) |  |
| GetPageStream | [PageRequest](#uggly-PageRequest) | [PageResponse](#uggly-PageResponse) stream |  |

 



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

