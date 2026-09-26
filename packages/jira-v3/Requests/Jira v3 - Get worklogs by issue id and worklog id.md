---
tags:
  - api/request
  - api/service/atlassian
  - api/app/jira
  - api/resource/other-operations
  - api/operation/search
  - api/effect/read
up: "[[MCP - Jira v3]]"
app: "Jira v3"
method: POST
path: "/rest/internal/api/latest/worklog/bulk"
category: "Other operations"
writes_data: false
tool_note: "[[jira_get_worklogs_by_issue_id_and_worklog_id]]"
---
# Jira v3 - Get worklogs by issue id and worklog id

**Get worklogs by issue id and worklog id** — `POST /rest/internal/api/latest/worklog/bulk`

- Run by the tool [[jira_get_worklogs_by_issue_id_and_worklog_id]].
- Official documentation: https://developer.atlassian.com/cloud/jira/platform/rest/v3/

```http
POST {{service.url}}/rest/internal/api/latest/worklog/bulk
Authorization: {{service.auth_token}}
Accept: application/json
Content-Type: application/json

{{param:body}}
```

## Parameters

- `body` (body, object, required) — JSON request body. See the example in the request note.

## Original description

Returns worklog details for a list of issue ID and worklog ID pairs.

This is an internal API for bulk fetching worklogs by their issue and worklog IDs. Worklogs that don't exist will be filtered out from the response.

The returned list of worklogs is limited to 1000 items.

**[Permissions](#permissions) required:** This is an internal service-to-service API that requires ASAP authentication. No user permission checks are performed as this bypasses normal user context.
