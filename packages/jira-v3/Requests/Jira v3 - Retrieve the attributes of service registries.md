---
tags:
  - api/request
  - api/service/atlassian
  - api/app/jira
  - api/resource/service-registry
  - api/operation/list
  - api/effect/read
  - api/restriction/app-connect
up: "[[MCP - Jira v3]]"
app: "Jira v3"
method: GET
path: "/rest/atlassian-connect/1/service-registry"
category: "Service Registry"
writes_data: false
---
# Jira v3 - Retrieve the attributes of service registries

**Retrieve the attributes of service registries** — `GET /rest/atlassian-connect/1/service-registry`

- No dedicated tool: run it with `atlassian_request_read` passing `request:"Jira v3 - Retrieve the attributes of service registries"`.
- **Restriction:** the documentation says only Connect/Forge apps can call this endpoint; a user token is expected to be rejected.
- Official documentation: https://developer.atlassian.com/cloud/jira/platform/rest/v3/

```http
GET {{service.url}}/rest/atlassian-connect/1/service-registry?serviceIds={{param:serviceIds}}
Authorization: {{service.auth_token}}
Accept: application/json
```

## Parameters

- `serviceIds` (query, string, required) — The ID of the services (the strings starting with "b:" need to be decoded in Base64).

## Original description

Retrieve the attributes of given service registries.

**[Permissions](#permissions) required:** Only Connect apps can make this request and the servicesIds belong to the tenant you are requesting
