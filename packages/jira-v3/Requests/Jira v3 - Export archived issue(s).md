---
tags:
  - api/request
  - api/service/atlassian
  - api/app/jira
  - api/resource/issues
  - api/operation/update
  - api/effect/write
  - api/permission/global-admin
up: "[[MCP - Jira v3]]"
app: "Jira v3"
method: PUT
path: "/rest/api/3/issues/archive/export"
category: "Issues"
writes_data: true
tool_note: "[[jira_export_archived_issue_s]]"
---
# Jira v3 - Export archived issue(s)

**Export archived issue(s)** — `PUT /rest/api/3/issues/archive/export`

- Run by the tool [[jira_export_archived_issue_s]].
- Official documentation: https://developer.atlassian.com/cloud/jira/platform/rest/v3/

```http
PUT {{service.url}}/rest/api/3/issues/archive/export
Authorization: {{service.auth_token}}
Content-Type: application/json

{{param:body}}
```

## Parameters

- `body` (body, object, required) — JSON request body. See the example in the request note.

## Body (example)

```json
{
  "archivedBy": [
    "uuid-rep-001",
    "uuid-rep-002"
  ],
  "archivedDate": {
    "dateAfter": "2023-01-01",
    "dateBefore": "2023-01-12"
  },
  "archivedDateRange": {
    "dateAfter": "2023-01-01",
    "dateBefore": "2023-01-12"
  },
  "issueTypes": [
    "10001",
    "10002"
  ],
  "projects": [
    "FOO",
    "BAR"
  ],
  "reporters": [
    "uuid-rep-001",
    "uuid-rep-002"
  ]
}
```

## Original description

Enables admins to retrieve details of all archived issues. Upon a successful request, the admin who submitted it will receive an email with a link to download a CSV file with the issue details.

Note that this API only exports the values of system fields and archival-specific fields (`ArchivedBy` and `ArchivedDate`). Custom fields aren't supported.

**[Permissions](#permissions) required:** Jira admin or site admin: [global permission](https://confluence.atlassian.com/x/x4dKLg)

**License required:** Premium or Enterprise

**Signed-in users only:** This API can't be accessed anonymously.

**Rate limiting:** Only a single request can be active at any given time.
