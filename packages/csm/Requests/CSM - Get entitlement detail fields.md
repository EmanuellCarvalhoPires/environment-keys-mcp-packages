---
tags:
  - api/request
  - api/service/atlassian
  - api/app/csm
  - api/resource/entitlement
  - api/operation/list
  - api/effect/read
  - api/permission/global-admin
up: "[[MCP - CSM]]"
app: "CSM"
method: GET
path: "/api/v1/entitlement/details"
category: "Entitlement"
writes_data: false
---
# CSM - Get entitlement detail fields

**Get entitlement detail fields** — `GET /api/v1/entitlement/details`

- No dedicated tool: run it with `atlassian_request_read` passing `request:"CSM - Get entitlement detail fields"`.
- Official documentation: https://developer.atlassian.com/cloud/customer-service-management/rest/v1/

```http
GET https://api.atlassian.com/jsm/csm/cloudid/{{service.cloud_id}}/api/v1/entitlement/details
Authorization: {{service.auth_token}}
Accept: application/json
```

## Original description

Returns all entitlement detail fields, including their configuration. You can use the [get entitlement](./#api-api-v1-entitlement-entitlementid-get)
API to get details for a particular entitlement.
**Permissions required:** Administer Jira [global permission](https://support.atlassian.com/jira-cloud-administration/docs/manage-global-permissions/).
