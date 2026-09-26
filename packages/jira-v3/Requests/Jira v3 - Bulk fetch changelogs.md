---
tags:
  - api/request
  - api/service/atlassian
  - api/app/jira
  - api/resource/issues
  - api/operation/search
  - api/effect/read
up: "[[MCP - Jira v3]]"
app: "Jira v3"
method: POST
path: "/rest/api/3/changelog/bulkfetch"
category: "Issues"
writes_data: false
tool_note: "[[jira_bulk_fetch_changelogs]]"
---
# Jira v3 - Bulk fetch changelogs

**Bulk fetch changelogs** — `POST /rest/api/3/changelog/bulkfetch`

- Run by the tool [[jira_bulk_fetch_changelogs]].
- Official documentation: https://developer.atlassian.com/cloud/jira/platform/rest/v3/

```http
POST {{service.url}}/rest/api/3/changelog/bulkfetch
Authorization: {{service.auth_token}}
Accept: application/json
Content-Type: application/json

{{param:body}}
```

## Parameters

- `body` (body, object, required) — JSON request body. See the example in the request note.

## Original description

Bulk fetch changelogs for multiple issues and filter by fields

Returns a paginated list of all changelogs for given issues sorted by changelog date and issue IDs, starting from the oldest changelog and smallest issue ID.

Issues are identified by their ID or key, and optionally changelogs can be filtered by their field IDs. You can request the changelogs of up to 1000 issues and can filter them by up to 10 field IDs.

**[Permissions](#permissions) required:**

 *  *Browse projects* [project permission](https://confluence.atlassian.com/x/yodKLg) for the projects that the issues are in.
 *  If [issue-level security](https://confluence.atlassian.com/x/J4lKLg) is configured, issue-level security permission to view the issues.
