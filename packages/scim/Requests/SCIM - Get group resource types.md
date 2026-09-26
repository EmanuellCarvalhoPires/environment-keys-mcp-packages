---
tags:
  - api/request
  - api/service/atlassian
  - api/app/scim
  - api/resource/service-provider-configuration
  - api/operation/list
  - api/effect/read
up: "[[MCP - SCIM]]"
app: "SCIM"
method: GET
path: "/scim/directory/{directoryId}/ResourceTypes/Group"
category: "Service Provider Configuration"
writes_data: false
---
# SCIM - Get group resource types

**Get group resource types** — `GET /scim/directory/{directoryId}/ResourceTypes/Group`

- No dedicated tool: run it with `atlassian_request_read` passing `request:"SCIM - Get group resource types"`.
- Official documentation: https://developer.atlassian.com/cloud/admin/user-provisioning/rest/

```http
GET https://api.atlassian.com/scim/directory/{{param:directoryId}}/ResourceTypes/Group
Authorization: {{service.scim_auth_token}}
Accept: application/json
```

## Parameters

- `directoryId` (path, string, required) — The SCIM base URL that is generated when conecting an identity provider with SCIM provisioning.

## Original description

Retrieves group resource type of this SCIM service provider. 

**Note:** This API does not support filtering, pagination, or sorting.
