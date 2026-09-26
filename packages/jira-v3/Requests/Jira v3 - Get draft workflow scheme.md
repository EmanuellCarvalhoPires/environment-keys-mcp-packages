---
tags:
  - api/request
  - api/service/atlassian
  - api/app/jira
  - api/resource/workflow-scheme-drafts
  - api/operation/list
  - api/effect/read
  - api/permission/global-admin
up: "[[MCP - Jira v3]]"
app: "Jira v3"
method: GET
path: "/rest/api/3/workflowscheme/{id}/draft"
category: "Workflow scheme drafts"
writes_data: false
tool_note: "[[jira_get_draft_workflow_scheme]]"
---
# Jira v3 - Get draft workflow scheme

**Get draft workflow scheme** — `GET /rest/api/3/workflowscheme/{id}/draft`

- Run by the tool [[jira_get_draft_workflow_scheme]].
- Official documentation: https://developer.atlassian.com/cloud/jira/platform/rest/v3/

```http
GET {{service.url}}/rest/api/3/workflowscheme/{{param:id}}/draft
Authorization: {{service.auth_token}}
Accept: application/json
```

## Parameters

- `id` (path, string, required) — The ID of the active workflow scheme that the draft was created from.

## Original description

Returns the draft workflow scheme for an active workflow scheme. Draft workflow schemes allow changes to be made to the active workflow schemes: When an active workflow scheme is updated, a draft copy is created. The draft is modified, then the changes in the draft are copied back to the active workflow scheme. See [Configuring workflow schemes](https://confluence.atlassian.com/x/tohKLg) for more information.  
Note that:

 *  Only active workflow schemes can have draft workflow schemes.
 *  An active workflow scheme can only have one draft workflow scheme.

**[Permissions](#permissions) required:** *Administer Jira* [global permission](https://confluence.atlassian.com/x/x4dKLg).
