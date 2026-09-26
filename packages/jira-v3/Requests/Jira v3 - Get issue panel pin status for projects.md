---
tags:
  - api/request
  - api/service/atlassian
  - api/app/jira
  - api/resource/issue-panels
  - api/operation/search
  - api/effect/read
  - api/permission/global-admin
up: "[[MCP - Jira v3]]"
app: "Jira v3"
method: POST
path: "/rest/api/3/forge/panel/action/bulk/status"
category: "Issue panels"
writes_data: false
tool_note: "[[jira_get_issue_panel_pin_status_for_projects]]"
---
# Jira v3 - Get issue panel pin status for projects

**Get issue panel pin status for projects** — `POST /rest/api/3/forge/panel/action/bulk/status`

- Run by the tool [[jira_get_issue_panel_pin_status_for_projects]].
- Official documentation: https://developer.atlassian.com/cloud/jira/platform/rest/v3/

```http
POST {{service.url}}/rest/api/3/forge/panel/action/bulk/status
Authorization: {{service.auth_token}}
Accept: application/json
Content-Type: application/json

{{param:body}}
```

## Parameters

- `body` (body, object, required) — JSON request body. See the example in the request note.

## Original description

Get the pin status of an issue panel (added by a Forge app) for multiple projects.

The operation is read-only and runs synchronously. Projects that do not exist, or that you do not have permission to access, are returned in the response with the panel reported as not pinned and the reason in the `error` field; the request itself still succeeds.

**[Permissions](#permissions) required:** *Administer Jira* [global permission](https://confluence.atlassian.com/x/x4dKLg).
