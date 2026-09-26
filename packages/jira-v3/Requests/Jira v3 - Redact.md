---
tags:
  - api/request
  - api/service/atlassian
  - api/app/jira
  - api/resource/issue-redaction
  - api/operation/action
  - api/effect/write
up: "[[MCP - Jira v3]]"
app: "Jira v3"
method: POST
path: "/rest/api/3/redact"
category: "Issue redaction"
writes_data: true
tool_note: "[[jira_redact]]"
---
# Jira v3 - Redact

**Redact** — `POST /rest/api/3/redact`

- Run by the tool [[jira_redact]].
- Official documentation: https://developer.atlassian.com/cloud/jira/platform/rest/v3/

```http
POST {{service.url}}/rest/api/3/redact
Authorization: {{service.auth_token}}
Content-Type: application/json

{{param:body}}
```

## Parameters

- `body` (body, object, required) — JSON request body. See the example in the request note.

## Original description

Submit a job to redact issue field data. This will trigger the redaction of the data in the specified fields asynchronously.

The redaction status can be polled using the job id.
