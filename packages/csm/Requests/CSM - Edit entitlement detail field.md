---
tags:
  - api/request
  - api/service/atlassian
  - api/app/csm
  - api/resource/entitlement
  - api/operation/update
  - api/effect/write
  - api/permission/global-admin
up: "[[MCP - CSM]]"
app: "CSM"
method: PUT
path: "/api/v1/entitlement/details/{fieldName}"
category: "Entitlement"
writes_data: true
---
# CSM - Edit entitlement detail field

**Edit entitlement detail field** — `PUT /api/v1/entitlement/details/{fieldName}`

- No dedicated tool: run it with `atlassian_request_write` passing `request:"CSM - Edit entitlement detail field"`.
- Official documentation: https://developer.atlassian.com/cloud/customer-service-management/rest/v1/

```http
PUT https://api.atlassian.com/jsm/csm/cloudid/{{service.cloud_id}}/api/v1/entitlement/details/{{param:fieldName}}
Authorization: {{service.auth_token}}
Accept: application/json
Content-Type: application/json

{{param:body}}
```

## Parameters

- `fieldName` (path, string, required) — Value of fieldName in the path.
- `body` (body, object, required) — JSON request body. See the example in the request note.

## Original description

Renames an entitlement detail field and/or changes the available options for SELECT or MULTISELECT fields.
**Permissions required:** Administer Jira [global permission](https://support.atlassian.com/jira-cloud-administration/docs/manage-global-permissions/).
