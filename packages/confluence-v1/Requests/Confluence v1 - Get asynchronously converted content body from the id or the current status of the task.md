---
tags:
  - api/request
  - api/service/atlassian
  - api/app/confluence
  - api/resource/content-body
  - api/operation/get
  - api/effect/read
  - api/version/v1
up: "[[MCP - Confluence v1]]"
app: "Confluence v1"
method: GET
path: "/wiki/rest/api/contentbody/convert/async/{id}"
category: "Content body"
writes_data: false
tool_note: "[[confluence_v1_get_asynchronously_converted_content_body_from_the]]"
---
# Confluence v1 - Get asynchronously converted content body from the id or the current status of the task

**Get asynchronously converted content body from the id or the current status of the task.** — `GET /wiki/rest/api/contentbody/convert/async/{id}`

- Run by the tool [[confluence_v1_get_asynchronously_converted_content_body_from_the]].
- Official documentation: https://developer.atlassian.com/cloud/confluence/rest/v1/

```http
GET {{service.url}}/wiki/rest/api/contentbody/convert/async/{{param:id}}
Authorization: {{service.auth_token}}
Accept: application/json
```

## Parameters

- `id` (path, string, required) — The asyncId of the macro task to get the converted body.

## Original description

Returns the content body for the corresponding `asyncId` of a completed conversion task. If
the task is not completed, the task status is returned instead.

Once a conversion task is completed, the result can be obtained for up to 5 minutes, or
until an identical conversion request is made again with the `allowCache` parameter set to
false.

**[Permissions](https://confluence.atlassian.com/x/_AozKw) required**:
If request specifies 'contentIdContext', 'View' permission for the space, and permission to view the content.
