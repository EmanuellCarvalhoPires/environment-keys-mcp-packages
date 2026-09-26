---
tags:
  - api/request
  - api/service/atlassian
  - api/app/jira
  - api/resource/issue-bulk-operations
  - api/operation/action
  - api/effect/write
up: "[[MCP - Jira v3]]"
app: "Jira v3"
method: POST
path: "/rest/api/3/bulk/issues/unwatch"
category: "Issue bulk operations"
writes_data: true
tool_note: "[[jira_bulk_unwatch_issues]]"
---
# Jira v3 - Bulk unwatch issues

**Bulk unwatch issues** — `POST /rest/api/3/bulk/issues/unwatch`

- Run by the tool [[jira_bulk_unwatch_issues]].
- Official documentation: https://developer.atlassian.com/cloud/jira/platform/rest/v3/

```http
POST {{service.url}}/rest/api/3/bulk/issues/unwatch
Authorization: {{service.auth_token}}
Content-Type: application/json

{{param:body}}
```

## Parameters

- `body` (body, object, required) — JSON request body. See the example in the request note.

## Body (example)

```json
{
  "selectedIssueIdsOrKeys": [
    "10001",
    "10002"
  ]
}
```

## Original description

Use this API to submit a bulk unwatch request. You can unwatch up to 1,000 issues in a single operation.

**[Permissions](#permissions) required:**

 *  Global bulk change [permission](https://support.atlassian.com/jira-cloud-administration/docs/manage-global-permissions/).
 *  Browse [project permission](https://support.atlassian.com/jira-cloud-administration/docs/manage-project-permissions/) in all projects that contain the selected issues.
 *  If [issue-level security](https://confluence.atlassian.com/x/J4lKLg) is configured, issue-level security permission to view the issue.
