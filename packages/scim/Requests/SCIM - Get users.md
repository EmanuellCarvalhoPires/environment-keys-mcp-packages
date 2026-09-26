---
tags:
  - api/request
  - api/service/atlassian
  - api/app/scim
  - api/resource/users
  - api/operation/list
  - api/effect/read
up: "[[MCP - SCIM]]"
app: "SCIM"
method: GET
path: "/scim/directory/{directoryId}/Users"
category: "Users"
writes_data: false
---
# SCIM - Get users

**Get users** — `GET /scim/directory/{directoryId}/Users`

- No dedicated tool: run it with `atlassian_request_read` passing `request:"SCIM - Get users"`.
- Official documentation: https://developer.atlassian.com/cloud/admin/user-provisioning/rest/

```http
GET https://api.atlassian.com/scim/directory/{{param:directoryId}}/Users?attributes={{param:attributes}}&excludedAttributes={{param:excludedAttributes}}&filter={{param:filter}}&startIndex={{param:startIndex}}&count={{param:count}}
Authorization: {{service.scim_auth_token}}
Accept: application/json
```

## Parameters

- `directoryId` (path, string, required) — The SCIM base URL that is generated when conecting an identity provider with SCIM provisioning.
- `attributes` (query, string, optional) — Resource attributes to be included in response. Mutually exclusive from excludedAttributes. Example: userName,emails.value
- `excludedAttributes` (query, string, optional) — Resource attributes to be excluded from response. Mutually exclusive from attributes. Example: timezone,emails.type,department
- `filter` (query, string, optional) — Filter for userName or externalId. Example: userName eq "Atlassian"
- `startIndex` (query, string, optional) — A 1-based index of the first query result.
- `count` (query, string, optional) — Desired maximum number of query results in the list response page.

## Original description

Get users from the specified directory. Filtering is supported with a single exact match  (`eq`) against the `userName` and `externalId` attributes.

 **Note**: While this API enables pagination, sorting functionality is not supported.
