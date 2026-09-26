---
tags:
  - api/request
  - api/service/atlassian
  - api/app/confluence
  - api/resource/content-attachments
  - api/operation/action
  - api/effect/write
  - api/version/v1
  - api/format/multipart
up: "[[MCP - Confluence v1]]"
app: "Confluence v1"
method: POST
path: "/wiki/rest/api/content/{id}/child/attachment/{attachmentId}/data"
category: "Content - attachments"
writes_data: true
---
# Confluence v1 - Update attachment data

**Update attachment data** — `POST /wiki/rest/api/content/{id}/child/attachment/{attachmentId}/data`

- No dedicated tool: run it with `atlassian_request_write` passing `request:"Confluence v1 - Update attachment data"`.
- **Format:** the endpoint expects `multipart/form-data` (file upload), which the plugin `http` block cannot build. Kept as reference.
- Official documentation: https://developer.atlassian.com/cloud/confluence/rest/v1/

```http
POST {{service.url}}/wiki/rest/api/content/{{param:id}}/child/attachment/{{param:attachmentId}}/data
Authorization: {{service.auth_token}}
Accept: application/json
```

## Parameters

- `id` (path, string, required) — The ID of the content that the attachment is attached to.
- `attachmentId` (path, string, required) — The ID of the attachment to update.

## Original description

Updates the binary data of an attachment, given the attachment ID, and
optionally the comment and the minor edit field.

This method is essentially the same as [Create or update attachments](#api-content-id-child-attachment-put),
except that it matches the attachment ID rather than the name.

Note, you must set a `X-Atlassian-Token: nocheck` header on the request
for this method, otherwise it will be blocked. This protects against XSRF
attacks, which is necessary as this method accepts multipart/form-data.

The media type 'multipart/form-data' is defined in [RFC 7578](https://www.ietf.org/rfc/rfc7578.txt).
Most client libraries have classes that make it easier to implement
multipart posts, like the [MultipartEntityBuilder](https://hc.apache.org/httpcomponents-client-5.1.x/current/httpclient5/apidocs/)
Java class provided by Apache HTTP Components.

Note, according to [RFC 7578](https://tools.ietf.org/html/rfc7578#section-4.5),
in the case where the form data is text,
the charset parameter for the "text/plain" Content-Type may be used to
indicate the character encoding used in that part. In the case of this
API endpoint, the `comment` body parameter should be sent with `type=text/plain`
and `charset=utf-8` values. This will force the charset to be UTF-8.

Example: This curl command updates an attachment (id='att456') that is attached
to a piece of content (id='123') with a comment and `minorEdits`=true.

``` bash
curl -D- \
  -u admin:admin \
  -X POST \
  -H 'X-Atlassian-Token: nocheck' \
  -F 'file=@"example.txt"' \
  -F 'minorEdit="true"' \
  -F 'comment="Example attachment comment"; type=text/plain; charset=utf-8' \
  http://myhost/rest/api/content/123/child/attachment/att456/data
```
**[Permissions](https://confluence.atlassian.com/x/_AozKw) required**:
Permission to update the content.
