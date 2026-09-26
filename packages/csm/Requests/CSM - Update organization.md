---
tags:
  - api/request
  - api/service/atlassian
  - api/app/csm
  - api/resource/organization
  - api/operation/update
  - api/effect/write
  - api/permission/global-admin
up: "[[MCP - CSM]]"
app: "CSM"
method: PUT
path: "/api/v1/organization/{organizationId}"
category: "Organization"
writes_data: true
---
# CSM - Update organization

**Update organization** — `PUT /api/v1/organization/{organizationId}`

- No dedicated tool: run it with `atlassian_request_write` passing `request:"CSM - Update organization"`.
- Official documentation: https://developer.atlassian.com/cloud/customer-service-management/rest/v1/

```http
PUT https://api.atlassian.com/jsm/csm/cloudid/{{service.cloud_id}}/api/v1/organization/{{param:organizationId}}
Authorization: {{service.auth_token}}
Accept: application/json
Content-Type: application/json

{{param:body}}
```

## Parameters

- `organizationId` (path, string, required) — Value of organizationId in the path.
- `body` (body, object, required) — JSON request body. See the example in the request note.

## Original description

Updates an organization's name.
**Permissions required:** Customer Service Management or Jira Service Management user. Note: Permission to update organizations can be switched to users with the Administer Jira [global permission](https://support.atlassian.com/jira-cloud-administration/docs/manage-global-permissions/) permission using the [Organization management](https://support.atlassian.com/jira-service-management-cloud/docs/manage-customer-organizations-using-jira-product-settings/) feature available in Jira Service Management product settings.
