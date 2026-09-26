---
tags:
  - api/request
  - api/service/atlassian
  - api/app/scim
  - api/resource/schemas
  - api/operation/list
  - api/effect/read
up: "[[MCP - SCIM]]"
app: "SCIM"
method: GET
path: "/scim/directory/{directoryId}/ServiceProviderConfig"
category: "Schemas"
writes_data: false
---
# SCIM - Get feature metadata

**Get feature metadata** — `GET /scim/directory/{directoryId}/ServiceProviderConfig`

- No dedicated tool: run it with `atlassian_request_read` passing `request:"SCIM - Get feature metadata"`.
- Official documentation: https://developer.atlassian.com/cloud/admin/user-provisioning/rest/

```http
GET https://api.atlassian.com/scim/directory/{{param:directoryId}}/ServiceProviderConfig
Authorization: {{service.scim_auth_token}}
Accept: application/json
```

## Parameters

- `directoryId` (path, string, required) — The SCIM base URL that is generated when conecting an identity provider with SCIM provisioning.

## Original description

Get metadata about the supported SCIM features. This is a service provider configuration  endpoint providing supported SCIM features. 

**Note:** This API does not support filtering, pagination, or sorting.
