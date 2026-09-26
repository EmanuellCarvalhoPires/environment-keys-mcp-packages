---
tags:
  - api/request
  - api/service/atlassian
  - api/app/csm
  - api/resource/organization
  - api/operation/create
  - api/effect/write
  - api/permission/global-admin
up: "[[MCP - CSM]]"
app: "CSM"
method: POST
path: "/api/v1/organization"
category: "Organization"
writes_data: true
---
# CSM - Create organization

**Create organization** — `POST /api/v1/organization`

- No dedicated tool: run it with `atlassian_request_write` passing `request:"CSM - Create organization"`.
- Official documentation: https://developer.atlassian.com/cloud/customer-service-management/rest/v1/

```http
POST https://api.atlassian.com/jsm/csm/cloudid/{{service.cloud_id}}/api/v1/organization
Authorization: {{service.auth_token}}
Accept: application/json
Content-Type: application/json

{{param:body}}
```

## Parameters

- `body` (body, object, required) — JSON request body. See the example in the request note.

## Original description

Creates an organization.
**Permissions required:** Customer Service Management or Jira Service Management user. Note: Permission to create organizations can be switched to users with the Administer Jira [global permission](https://support.atlassian.com/jira-cloud-administration/docs/manage-global-permissions/) permission using the [Organization management](https://support.atlassian.com/jira-service-management-cloud/docs/manage-customer-organizations-using-jira-product-settings/) feature available in Jira Service Management product settings.
