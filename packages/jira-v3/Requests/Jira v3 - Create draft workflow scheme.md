---
tags:
  - api/request
  - api/service/atlassian
  - api/app/jira
  - api/resource/workflow-scheme-drafts
  - api/operation/create
  - api/effect/write
  - api/permission/global-admin
up: "[[MCP - Jira v3]]"
app: "Jira v3"
method: POST
path: "/rest/api/3/workflowscheme/{id}/createdraft"
category: "Workflow scheme drafts"
writes_data: true
tool_note: "[[jira_create_draft_workflow_scheme]]"
---
# Jira v3 - Create draft workflow scheme

**Create draft workflow scheme** — `POST /rest/api/3/workflowscheme/{id}/createdraft`

- Run by the tool [[jira_create_draft_workflow_scheme]].
- Official documentation: https://developer.atlassian.com/cloud/jira/platform/rest/v3/

```http
POST {{service.url}}/rest/api/3/workflowscheme/{{param:id}}/createdraft
Authorization: {{service.auth_token}}
```

## Parameters

- `id` (path, string, required) — The ID of the active workflow scheme that the draft is created from.

## Original description

Create a draft workflow scheme from an active workflow scheme, by copying the active workflow scheme. Note that an active workflow scheme can only have one draft workflow scheme.

**[Permissions](#permissions) required:** *Administer Jira* [global permission](https://confluence.atlassian.com/x/x4dKLg).
