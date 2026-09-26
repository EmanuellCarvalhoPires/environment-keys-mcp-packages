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
path: "/rest/api/3/workflows/search"
category: "Workflows"
writes_data: false
tool_note: "[[jira_search_workflows]]"
---
# Jira v3 - Search workflows

**Search workflows** — `GET /rest/api/3/workflows/search`

- Run by the tool [[jira_search_workflows]].
- Official documentation: https://developer.atlassian.com/cloud/jira/platform/rest/v3/

```http
GET {{service.url}}/rest/api/3/workflows/search?startAt={{param:startAt}}&maxResults={{param:maxResults}}&expand={{param:expand}}&queryString={{param:queryString}}&orderBy={{param:orderBy}}&scope={{param:scope}}&isActive={{param:isActive}}&projectId={{param:projectId}}
Authorization: {{service.auth_token}}
Accept: application/json
```

## Parameters

- `startAt` (query, string, optional) — The index of the first item to return in a page of results (page offset).
- `maxResults` (query, string, optional) — The maximum number of items to return per page.
- `expand` (query, string, optional) — Use expand to include additional information in the response. This parameter accepts a comma-separated list.
- `queryString` (query, string, optional) — String used to perform a case-insensitive partial match with workflow name.
- `orderBy` (query, string, optional) — Order the results by a field: name Sorts by workflow name. created Sorts by create time. updated Sorts by update time.
- `scope` (query, string, optional) — The scope of the workflow. Global for company-managed projects and Project for team-managed projects.
- `isActive` (query, string, optional) — Filters active and inactive workflows.
- `projectId` (query, string, optional) — The ID of the project to filter the workflows by. Only workflows associated with the given project are returned.

## Original description

Returns a [paginated](#pagination) list of global and project workflows. If workflow names are specified in the query string, details of those workflows are returned. Otherwise, all workflows are returned.

**[Permissions](#permissions) required:**

 *  *Administer Jira* global permission to access all, including project-scoped, workflows
 *  At least one of the *Administer projects* and *View (read-only) workflow* project permissions to access project-scoped workflows
