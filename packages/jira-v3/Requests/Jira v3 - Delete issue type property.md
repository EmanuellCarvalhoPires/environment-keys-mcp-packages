---
tags:
  - api/request
  - api/service/atlassian
  - api/app/jira
  - api/resource/issue-type-properties
  - api/operation/delete
  - api/effect/write
  - api/permission/global-admin
up: "[[MCP - Jira v3]]"
app: "Jira v3"
method: DELETE
path: "/rest/api/3/issuetype/{issueTypeId}/properties/{propertyKey}"
category: "Issue type properties"
writes_data: true
tool_note: "[[jira_delete_issue_type_property]]"
---
# Jira v3 - Delete issue type property

**Delete issue type property** — `DELETE /rest/api/3/issuetype/{issueTypeId}/properties/{propertyKey}`

- Run by the tool [[jira_delete_issue_type_property]].
- Official documentation: https://developer.atlassian.com/cloud/jira/platform/rest/v3/

```http
DELETE {{service.url}}/rest/api/3/issuetype/{{param:issueTypeId}}/properties/{{param:propertyKey}}
Authorization: {{service.auth_token}}
```

## Parameters

- `issueTypeId` (path, string, required) — The ID of the issue type.
- `propertyKey` (path, string, required) — The key of the property. Use Get issue type property keys to get a list of all issue type property keys.

## Original description

Deletes the [issue type property](https://developer.atlassian.com/cloud/jira/platform/storing-data-without-a-database/#a-id-jira-entity-properties-a-jira-entity-properties).

**[Permissions](#permissions) required:** *Administer Jira* [global permission](https://confluence.atlassian.com/x/x4dKLg).
