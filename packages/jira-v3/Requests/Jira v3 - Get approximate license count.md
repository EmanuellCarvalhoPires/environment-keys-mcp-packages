---
tags:
  - api/request
  - api/service/atlassian
  - api/app/jira
  - api/resource/license-metrics
  - api/operation/list
  - api/effect/read
  - api/permission/global-admin
up: "[[MCP - Jira v3]]"
app: "Jira v3"
method: GET
path: "/rest/api/3/license/approximateLicenseCount"
category: "License metrics"
writes_data: false
tool_note: "[[jira_get_approximate_license_count]]"
---
# Jira v3 - Get approximate license count

**Get approximate license count** — `GET /rest/api/3/license/approximateLicenseCount`

- Run by the tool [[jira_get_approximate_license_count]].
- Official documentation: https://developer.atlassian.com/cloud/jira/platform/rest/v3/

```http
GET {{service.url}}/rest/api/3/license/approximateLicenseCount
Authorization: {{service.auth_token}}
Accept: application/json
```

## Original description

Returns the approximate number of user accounts across all Jira licenses. Note that this information is cached with a 7-day lifecycle and could be stale at the time of call.

**[Permissions](#permissions) required:** *Administer Jira* [global permission](https://confluence.atlassian.com/x/x4dKLg).
