---
tags:
  - api/request
  - api/service/atlassian
  - api/app/scim
  - api/resource/groups
  - api/operation/list
  - api/effect/read
up: "[[MCP - SCIM]]"
app: "SCIM"
method: GET
path: "/scim/directory/{directoryId}/Groups"
category: "Groups"
writes_data: false
---
# SCIM - Get groups

**Get groups** — `GET /scim/directory/{directoryId}/Groups`

- No dedicated tool: run it with `atlassian_request_read` passing `request:"SCIM - Get groups"`.
- Official documentation: https://developer.atlassian.com/cloud/admin/user-provisioning/rest/

```http
GET https://api.atlassian.com/scim/directory/{{param:directoryId}}/Groups?filter={{param:filter}}&startIndex={{param:startIndex}}&count={{param:count}}
Authorization: {{service.scim_auth_token}}
Accept: application/json
```

## Parameters

- `directoryId` (path, string, required) — The SCIM base URL that is generated when conecting an identity provider with SCIM provisioning.
- `filter` (query, string, optional) — Filter for displayName. Example: displayName eq "SCIMGROUP"
- `startIndex` (query, string, optional) — A 1-based index of the first query result.
- `count` (query, string, optional) — Desired maximum number of query results in the list response page.

## Original description

Get groups from the directory. Filter the groups by name supported with a single exact match (`eq`) against the `displayName` attribute. 

**Note**: While this API enables pagination, sorting functionality is not supported.
