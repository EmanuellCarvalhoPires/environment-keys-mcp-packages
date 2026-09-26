---
tags:
  - api/request
  - api/service/atlassian
  - api/app/assets
  - api/resource/icon
  - api/operation/list
  - api/effect/read
  - api/format/binary
up: "[[MCP - Assets]]"
app: "Assets"
method: GET
path: "/icon/{id}/icon.png"
category: "Icon"
writes_data: false
---
# Assets - GET icon {id} icon.png

**/icon/{id}/icon.png** — `GET /icon/{id}/icon.png`

- No dedicated tool: run it with `atlassian_request_read` passing `request:"Assets - GET icon {id} icon.png"`.
- **Format:** the response is binary (file/image); the plugin returns the body as text.
- Official documentation: https://developer.atlassian.com/cloud/assets/rest/

```http
GET https://api.atlassian.com/ex/jira/{{service.cloud_id}}/jsm/assets/workspace/{{service.assets_workspace_id}}/v1/icon/{{param:id}}/icon.png
Authorization: {{service.auth_token}}
Accept: image/png
```

## Parameters

- `id` (path, string, required) — Value of id in the path.

## Original description

Load a single icon PNG by id
