---
tags:
  - api/request
  - api/service/atlassian
  - api/app/admin
  - api/resource/users
  - api/operation/list
  - api/effect/read
up: "[[MCP - Admin Orgs]]"
app: "Admin Orgs"
method: GET
path: "/v1/orgs/{orgId}/directory/users/{accountId}/last-active-dates"
category: "Users"
writes_data: false
---
# Admin Orgs - User’s last active dates

**User’s last active dates** — `GET /v1/orgs/{orgId}/directory/users/{accountId}/last-active-dates`

- No dedicated tool: run it with `atlassian_request_read` passing `request:"Admin Orgs - User’s last active dates"`.
- Official documentation: https://developer.atlassian.com/cloud/admin/organization/rest/

```http
GET https://api.atlassian.com/admin/v1/orgs/{{service.org_id}}/directory/users/{{param:accountId}}/last-active-dates?cursor={{param:cursor}}
Authorization: {{service.admin_auth_token}}
Accept: application/json
```

## Parameters

- `accountId` (path, string, required) — Unique ID of the user's account. Use the Jira User Search API to get the accountId (if Jira is available for your Organization). Jira APIs use a different authentication method .
- `cursor` (query, string, optional) — Cursor to fetch the next page

## Original description

**Additional response parameters of the API (for e.g., `added_to_org`) are available only to customers using the new user management experience.** Learn more about the [new user management experience](https://community.atlassian.com/t5/Atlassian-Access-articles/User-management-for-cloud-admins-just-got-easier/ba-p/1576592).

Specifications:
- Return a user’s last active date for each product listed in Atlassian Administration.
- Active is defined as viewing a product's page for a minimum of 2 seconds. 
- The data for the last activity may be delayed by up to 24 hours.
- If the user has not accessed a product, the `product_access` response field will be empty. 

Learn the fastest way to call the API with a detailed [tutorial](https://developer.atlassian.com/cloud/admin/organization/user-last-active-dates/).
