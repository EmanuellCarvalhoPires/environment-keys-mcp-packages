---
tags:
  - api/request
  - api/service/atlassian
  - api/app/jira
  - api/resource/migration-of-connect-modules-to-forge
  - api/operation/action
  - api/effect/write
  - api/restriction/app-connect
up: "[[MCP - Jira v3]]"
app: "Jira v3"
method: POST
path: "/rest/atlassian-connect/1/migration/{connectKey}/{jiraIssueFieldsKey}/task"
category: "Migration of Connect modules to Forge"
writes_data: true
---
# Jira v3 - Submit Connect issue field migration task

**Submit Connect issue field migration task** — `POST /rest/atlassian-connect/1/migration/{connectKey}/{jiraIssueFieldsKey}/task`

- No dedicated tool: run it with `atlassian_request_write` passing `request:"Jira v3 - Submit Connect issue field migration task"`.
- **Restriction:** the documentation says only Connect/Forge apps can call this endpoint; a user token is expected to be rejected.
- Official documentation: https://developer.atlassian.com/cloud/jira/platform/rest/v3/

```http
POST {{service.url}}/rest/atlassian-connect/1/migration/{{param:connectKey}}/{{param:jiraIssueFieldsKey}}/task?retriggerCompletedMigration={{param:retriggerCompletedMigration}}
Authorization: {{service.auth_token}}
```

## Parameters

- `connectKey` (path, string, required) — The key of the Connect app that contains the Jira issue field being migrated.
- `jiraIssueFieldsKey` (path, string, required) — The module key of the Connect issue field being migrated.
- `retriggerCompletedMigration` (query, string, optional) — Whether to retrigger the migration if it has already completed.

## Original description

Submits a request to trigger migration of connect issue field to its Forge custom field counterpart.

When migrating a Connect app to Forge, [Issue Field](https://developer.atlassian.com/cloud/jira/software/modules/issue-field/) modules
must be converted to [Custom field](https://developer.atlassian.com/platform/forge/manifest-reference/modules/jira-custom-field/) modules.
This endpoint triggers the background migration of field data. Use the GET endpoint to retrieve
the status and progress of the task.

For more details, see
[Jira modules > Jira Custom Fields](https://developer.atlassian.com/platform/adopting-forge-from-connect/migrate-jira-custom-fields/).

**[Permissions](#permissions) required:** Only Connect and Forge apps can make this request.
