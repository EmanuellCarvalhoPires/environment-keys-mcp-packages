---
tags:
  - api/request
  - api/service/atlassian
  - api/app/confluence
  - api/resource/content-body
  - api/operation/list
  - api/effect/read
  - api/version/v1
up: "[[MCP - Confluence v1]]"
app: "Confluence v1"
method: GET
path: "/wiki/rest/api/contentbody/convert/async/bulk/tasks"
category: "Content body"
writes_data: false
tool_note: "[[confluence_v1_get_asynchronous_content_body_conversion_task_resu]]"
---
# Confluence v1 - Get asynchronous content body conversion task result in bulk

**Get asynchronous content body conversion task result in bulk** — `GET /wiki/rest/api/contentbody/convert/async/bulk/tasks`

- Run by the tool [[confluence_v1_get_asynchronous_content_body_conversion_task_resu]].
- Official documentation: https://developer.atlassian.com/cloud/confluence/rest/v1/

```http
GET {{service.url}}/wiki/rest/api/contentbody/convert/async/bulk/tasks?ids={{param:ids}}
Authorization: {{service.auth_token}}
Accept: application/json
```

## Parameters

- `ids` (query, string, required) — The asyncIds of the conversion tasks.

## Original description

Returns the content body for the corresponding `asyncId` of a completed conversion task. If
the task is not completed, the task status is returned instead.

Once a conversion task is completed, the result can be obtained for up to 5 minutes, or
until an identical conversion request is made again with the `allowCache` parameter set to
false.

Note that there is a maximum limit of 50 task results per request to this endpoint.

**[Permissions](https://confluence.atlassian.com/x/_AozKw) required**:
Permission to access the Confluence site ('Can use' global permission).
