---
tags:
  - api/request
  - api/service/atlassian
  - api/app/jira
  - api/resource/workflows
  - api/operation/search
  - api/effect/read
  - api/permission/global-admin
up: "[[MCP - Jira v3]]"
app: "Jira v3"
method: GET
path: "/rest/api/3/workflow/search"
category: "Workflows"
writes_data: false
tool_note: "[[jira_get_workflows_paginated]]"
---
# Jira v3 - Get workflows paginated

**Get workflows paginated** — `GET /rest/api/3/workflow/search`

- Run by the tool [[jira_get_workflows_paginated]].
- Official documentation: https://developer.atlassian.com/cloud/jira/platform/rest/v3/

```http
GET {{service.url}}/rest/api/3/workflow/search?startAt={{param:startAt}}&maxResults={{param:maxResults}}&workflowName={{param:workflowName}}&expand={{param:expand}}&queryString={{param:queryString}}&orderBy={{param:orderBy}}&isActive={{param:isActive}}
Authorization: {{service.auth_token}}
Accept: application/json
```

## Parameters

- `startAt` (query, string, optional) — The index of the first item to return in a page of results (page offset).
- `maxResults` (query, string, optional) — The maximum number of items to return per page.
- `workflowName` (query, string, optional) — The name of a workflow to return. To include multiple workflows, provide an ampersand-separated list. For example, workflowName=name1&workflowName=name2.
- `expand` (query, string, optional) — Use expand to include additional information in the response. This parameter accepts a comma-separated list.
- `queryString` (query, string, optional) — String used to perform a case-insensitive partial match with workflow name.
- `orderBy` (query, string, optional) — Order the results by a field: name Sorts by workflow name. created Sorts by create time. updated Sorts by update time.
- `isActive` (query, string, optional) — Filters active and inactive workflows.

## Original description

This will be removed on [June 1, 2026](https://developer.atlassian.com/cloud/jira/platform/changelog/#CHANGE-2569); use [Search workflows](#api-rest-api-3-workflows-search-get) instead.

Returns a [paginated](#pagination) list of published classic workflows. When workflow names are specified, details of those workflows are returned. Otherwise, all published classic workflows are returned.

This operation does not return next-gen workflows.

**[Permissions](#permissions) required:** *Administer Jira* [global permission](https://confluence.atlassian.com/x/x4dKLg).
