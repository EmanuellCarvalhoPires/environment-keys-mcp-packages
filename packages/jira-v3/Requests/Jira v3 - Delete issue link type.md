---
tags:
  - api/request
  - api/service/atlassian
  - api/app/jira
  - api/resource/issue-link-types
  - api/operation/delete
  - api/effect/write
  - api/permission/global-admin
up: "[[MCP - Jira v3]]"
app: "Jira v3"
method: DELETE
path: "/rest/api/3/issueLinkType/{issueLinkTypeId}"
category: "Issue link types"
writes_data: true
tool_note: "[[jira_delete_issue_link_type]]"
---
# Jira v3 - Delete issue link type

**Delete issue link type** — `DELETE /rest/api/3/issueLinkType/{issueLinkTypeId}`

- Run by the tool [[jira_delete_issue_link_type]].
- Official documentation: https://developer.atlassian.com/cloud/jira/platform/rest/v3/

```http
DELETE {{service.url}}/rest/api/3/issueLinkType/{{param:issueLinkTypeId}}
Authorization: {{service.auth_token}}
```

## Parameters

- `issueLinkTypeId` (path, string, required) — The ID of the issue link type.

## Original description

Deletes an issue link type.

To use this operation, the site must have [issue linking](https://confluence.atlassian.com/x/yoXKM) enabled.

**[Permissions](#permissions) required:** *Administer Jira* [global permission](https://confluence.atlassian.com/x/x4dKLg).
