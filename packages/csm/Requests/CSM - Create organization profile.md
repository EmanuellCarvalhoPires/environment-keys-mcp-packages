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
path: "/api/v1/organization/profile"
category: "Organization"
writes_data: true
---
# CSM - Create organization profile

**Create organization profile** — `POST /api/v1/organization/profile`

- No dedicated tool: run it with `atlassian_request_write` passing `request:"CSM - Create organization profile"`.
- Official documentation: https://developer.atlassian.com/cloud/customer-service-management/rest/v1/

```http
POST https://api.atlassian.com/jsm/csm/cloudid/{{service.cloud_id}}/api/v1/organization/profile
Authorization: {{service.auth_token}}
Accept: application/json
Content-Type: application/json

{{param:body}}
```

## Parameters

- `body` (body, object, required) — JSON request body. See the example in the request note.

## Original description

Creates an organization's profile, including adding the organization's detail fields, customers belonging to the organization and any product entitlements.
**Permissions required:** Customer Service Management or Jira Service Management user. Note: Permission to create organizations can be switched to users with the Administer Jira [global permission](https://support.atlassian.com/jira-cloud-administration/docs/manage-global-permissions/) permission using the [Organization management](https://support.atlassian.com/jira-service-management-cloud/docs/manage-customer-organizations-using-jira-product-settings/) feature available in Jira Service Management product settings.
