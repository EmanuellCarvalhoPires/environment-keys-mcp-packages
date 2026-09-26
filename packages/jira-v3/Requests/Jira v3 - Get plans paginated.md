---
tags:
  - api/request
  - api/service/atlassian
  - api/app/jira
  - api/resource/plans
  - api/operation/list
  - api/effect/read
  - api/permission/global-admin
up: "[[MCP - Jira v3]]"
app: "Jira v3"
method: GET
path: "/rest/api/3/plans/plan"
category: "Plans"
writes_data: false
tool_note: "[[jira_get_plans_paginated]]"
---
# Jira v3 - Get plans paginated

**Get plans paginated** — `GET /rest/api/3/plans/plan`

- Run by the tool [[jira_get_plans_paginated]].
- Official documentation: https://developer.atlassian.com/cloud/jira/platform/rest/v3/

```http
GET {{service.url}}/rest/api/3/plans/plan?includeTrashed={{param:includeTrashed}}&includeArchived={{param:includeArchived}}&cursor={{param:cursor}}&maxResults={{param:maxResults}}
Authorization: {{service.auth_token}}
Accept: application/json
```

## Parameters

- `includeTrashed` (query, string, optional) — Whether to include trashed plans in the results.
- `includeArchived` (query, string, optional) — Whether to include archived plans in the results.
- `cursor` (query, string, optional) — The cursor to start from. If not provided, the first page will be returned.
- `maxResults` (query, string, optional) — The maximum number of plans to return per page. The maximum value is 50. The default value is 50.

## Original description

Returns a [paginated](#pagination) list of plans.

**[Permissions](#permissions) required:** *Administer Jira* [global permission](https://confluence.atlassian.com/x/x4dKLg).
