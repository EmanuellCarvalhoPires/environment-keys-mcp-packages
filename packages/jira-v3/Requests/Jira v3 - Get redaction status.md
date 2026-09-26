---
tags:
  - api/request
  - api/service/atlassian
  - api/app/jira
  - api/resource/issue-redaction
  - api/operation/get
  - api/effect/read
up: "[[MCP - Jira v3]]"
app: "Jira v3"
method: GET
path: "/rest/api/3/redact/status/{jobId}"
category: "Issue redaction"
writes_data: false
tool_note: "[[jira_get_redaction_status]]"
---
# Jira v3 - Get redaction status

**Get redaction status** — `GET /rest/api/3/redact/status/{jobId}`

- Run by the tool [[jira_get_redaction_status]].
- Official documentation: https://developer.atlassian.com/cloud/jira/platform/rest/v3/

```http
GET {{service.url}}/rest/api/3/redact/status/{{param:jobId}}
Authorization: {{service.auth_token}}
Accept: application/json
```

## Parameters

- `jobId` (path, string, required) — Redaction job id

## Original description

Retrieves the current status of a redaction job ID.

The jobStatus will be one of the following:

 *  IN\_PROGRESS - The redaction job is currently in progress
 *  COMPLETED - The redaction job has completed successfully.
 *  PENDING - The redaction job has not started yet
