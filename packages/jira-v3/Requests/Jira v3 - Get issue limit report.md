---
tags:
  - api/request
  - api/service/atlassian
  - api/app/jira
  - api/resource/issues
  - api/operation/list
  - api/effect/read
  - api/permission/global-admin
up: "[[MCP - Jira v3]]"
app: "Jira v3"
method: GET
path: "/rest/api/3/issue/limit/report"
category: "Issues"
writes_data: false
tool_note: "[[jira_get_issue_limit_report]]"
---
# Jira v3 - Get issue limit report

**Get issue limit report** — `GET /rest/api/3/issue/limit/report`

- Run by the tool [[jira_get_issue_limit_report]].
- Official documentation: https://developer.atlassian.com/cloud/jira/platform/rest/v3/

```http
GET {{service.url}}/rest/api/3/issue/limit/report?isReturningKeys={{param:isReturningKeys}}
Authorization: {{service.auth_token}}
Accept: application/json
```

## Parameters

- `isReturningKeys` (query, string, optional) — Return issue keys instead of issue ids in the response. Usage: Add ?isReturningKeys=true to the end of the path to request issue keys.

## Original description

Returns all issues breaching and approaching per-issue limits.

**[Permissions](#permissions) required:**

 *  *Browse projects* [project permission](https://confluence.atlassian.com/x/yodKLg) is required for the project the issues are in. Results may be incomplete otherwise
 *  *Administer Jira* [global permission](https://confluence.atlassian.com/x/x4dKLg).
