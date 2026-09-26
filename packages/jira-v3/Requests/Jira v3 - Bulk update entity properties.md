---
tags:
  - api/request
  - api/service/atlassian
  - api/app/jira
  - api/resource/app-migration
  - api/operation/update
  - api/effect/write
  - api/restriction/app-connect
up: "[[MCP - Jira v3]]"
app: "Jira v3"
method: PUT
path: "/rest/atlassian-connect/1/migration/properties/{entityType}"
category: "App migration"
writes_data: true
---
# Jira v3 - Bulk update entity properties

**Bulk update entity properties** — `PUT /rest/atlassian-connect/1/migration/properties/{entityType}`

- No dedicated tool: run it with `atlassian_request_write` passing `request:"Jira v3 - Bulk update entity properties"`.
- **Restriction:** the documentation says only Connect/Forge apps can call this endpoint; a user token is expected to be rejected.
- Official documentation: https://developer.atlassian.com/cloud/jira/platform/rest/v3/

```http
PUT {{service.url}}/rest/atlassian-connect/1/migration/properties/{{param:entityType}}
Authorization: {{service.auth_token}}
Atlassian-Transfer-Id: {{param:atlassian_transfer_id}}
Content-Type: application/json

{{param:body}}
```

## Parameters

- `entityType` (path, string, required) — The type indicating the object that contains the entity properties.
- `atlassian_transfer_id` (header, string, required) — Value of the `Atlassian-Transfer-Id` header.
- `body` (body, object, required) — JSON request body. See the example in the request note.

## Original description

Updates the values of multiple entity properties for an object, up to 50 updates per request. This operation is for use by Connect apps during app migration.
