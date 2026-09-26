---
tags:
  - api/request
  - api/service/atlassian
  - api/app/jira
  - api/resource/issue-custom-field-contexts
  - api/operation/action
  - api/effect/write
  - api/permission/global-admin
up: "[[MCP - Jira v3]]"
app: "Jira v3"
method: POST
path: "/rest/api/3/field/{fieldId}/context/{contextId}/issuetype/remove"
category: "Issue custom field contexts"
writes_data: true
tool_note: "[[jira_remove_issue_types_from_context]]"
---
# Jira v3 - Remove issue types from context

**Remove issue types from context** — `POST /rest/api/3/field/{fieldId}/context/{contextId}/issuetype/remove`

- Run by the tool [[jira_remove_issue_types_from_context]].
- Official documentation: https://developer.atlassian.com/cloud/jira/platform/rest/v3/

```http
POST {{service.url}}/rest/api/3/field/{{param:fieldId}}/context/{{param:contextId}}/issuetype/remove
Authorization: {{service.auth_token}}
Content-Type: application/json

{{param:body}}
```

## Parameters

- `fieldId` (path, string, required) — The ID of the custom field.
- `contextId` (path, string, required) — The ID of the context.
- `body` (body, object, required) — JSON request body. See the example in the request note.

## Body (example)

```json
{
  "issueTypeIds": [
    "10001",
    "10005",
    "10006"
  ]
}
```

## Original description

Removes issue types from a custom field context.

A custom field context without any issue types applies to all issue types.

**[Permissions](#permissions) required:** *Administer Jira* [global permission](https://confluence.atlassian.com/x/x4dKLg).
