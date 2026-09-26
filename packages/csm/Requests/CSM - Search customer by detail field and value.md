---
tags:
  - api/request
  - api/service/atlassian
  - api/app/csm
  - api/resource/customer
  - api/operation/search
  - api/effect/read
up: "[[MCP - CSM]]"
app: "CSM"
method: POST
path: "/api/v1/customer/search-by-detail-field"
category: "Customer"
writes_data: false
---
# CSM - Search customer by detail field and value

**Search customer by detail field and value** — `POST /api/v1/customer/search-by-detail-field`

- No dedicated tool: run it with `atlassian_request_read` passing `request:"CSM - Search customer by detail field and value"`.
- Official documentation: https://developer.atlassian.com/cloud/customer-service-management/rest/v1/

```http
POST https://api.atlassian.com/jsm/csm/cloudid/{{service.cloud_id}}/api/v1/customer/search-by-detail-field?page={{param:page}}&maxResults={{param:maxResults}}
Authorization: {{service.auth_token}}
Accept: application/json
Content-Type: application/json

{{param:body}}
```

## Parameters

- `page` (query, string, optional) — Query parameter page.
- `maxResults` (query, string, optional) — Query parameter maxResults.
- `body` (body, object, required) — JSON request body. See the example in the request note.

## Original description

Returns the list of customers. You can get details and entitlements for a customer using [get customer profile](./#api-api-v1-customer-profile-customerid-get) API.
**Permissions required:** Jira Service Management agent.
To retrieve restricted information such as email address of the user, **Administer Jira** [global permission](https://support.atlassian.com/jira-cloud-administration/docs/manage-global-permissions/).
