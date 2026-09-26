---
tags:
  - api/request
  - api/service/atlassian
  - api/app/jsm-ops
  - api/resource/contacts
  - api/operation/list
  - api/effect/read
up: "[[MCP - JSM Ops]]"
app: "JSM Ops"
method: GET
path: "/api/{cloudId}/v1/users/contacts"
category: "Contacts"
writes_data: false
---
# JSM Ops - List contacts

**List contacts** — `GET /api/{cloudId}/v1/users/contacts`

- No dedicated tool: run it with `atlassian_request_read` passing `request:"JSM Ops - List contacts"`.
- Official documentation: https://developer.atlassian.com/cloud/jira/service-desk-ops/rest/v2/

```http
GET https://api.atlassian.com/jsm/ops/api/{{service.cloud_id}}/v1/users/contacts?offset={{param:offset}}&size={{param:size}}&targetAccountId={{param:targetAccountId}}
Authorization: {{service.auth_token}}
Accept: application/json
```

## Parameters

- `offset` (query, string, optional) — Query parameter offset.
- `size` (query, string, optional) — Query parameter size.
- `targetAccountId` (query, string, optional) — This field is used by users with Jira Admin or Ops Admin privileges to retrieve the contact information of the target user.

## Original description

Returns the list of the contacts of a user.
