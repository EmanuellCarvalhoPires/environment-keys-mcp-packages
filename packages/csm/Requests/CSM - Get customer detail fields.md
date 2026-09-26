---
tags:
  - api/request
  - api/service/atlassian
  - api/app/csm
  - api/resource/customer
  - api/operation/list
  - api/effect/read
  - api/permission/global-admin
up: "[[MCP - CSM]]"
app: "CSM"
method: GET
path: "/api/v1/customer/details"
category: "Customer"
writes_data: false
---
# CSM - Get customer detail fields

**Get customer detail fields** — `GET /api/v1/customer/details`

- No dedicated tool: run it with `atlassian_request_read` passing `request:"CSM - Get customer detail fields"`.
- Official documentation: https://developer.atlassian.com/cloud/customer-service-management/rest/v1/

```http
GET https://api.atlassian.com/jsm/csm/cloudid/{{service.cloud_id}}/api/v1/customer/details
Authorization: {{service.auth_token}}
Accept: application/json
```

## Original description

Returns all customer detail fields, including their configuration. You can use the [get customer profile](./#api-api-v1-customer-profile-customerid-get)
API to get details for a particular customer.
**Permissions required:** Administer Jira [global permission](https://support.atlassian.com/jira-cloud-administration/docs/manage-global-permissions/).
