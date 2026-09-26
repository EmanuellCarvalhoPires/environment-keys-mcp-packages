---
tags:
  - api/request
  - api/service/atlassian
  - api/app/csm
  - api/resource/organization
  - api/operation/list
  - api/effect/read
  - api/permission/global-admin
up: "[[MCP - CSM]]"
app: "CSM"
method: GET
path: "/api/v1/organization/details"
category: "Organization"
writes_data: false
---
# CSM - Get organization detail fields

**Get organization detail fields** — `GET /api/v1/organization/details`

- No dedicated tool: run it with `atlassian_request_read` passing `request:"CSM - Get organization detail fields"`.
- Official documentation: https://developer.atlassian.com/cloud/customer-service-management/rest/v1/

```http
GET https://api.atlassian.com/jsm/csm/cloudid/{{service.cloud_id}}/api/v1/organization/details
Authorization: {{service.auth_token}}
Accept: application/json
```

## Original description

Returns all organization detail fields, including their configuration. You can use the [get organization profile](./#api-api-v1-organization-profile-organizationid-get) API to get details for a particular organization.
**Permissions required:** Administer Jira [global permission](https://support.atlassian.com/jira-cloud-administration/docs/manage-global-permissions/).
