---
tags:
  - api/request
  - api/service/atlassian
  - api/app/jira
  - api/resource/issue-link-types
  - api/operation/get
  - api/effect/read
up: "[[MCP - Jira v3]]"
app: "Jira v3"
method: GET
path: "/rest/api/3/issueLinkType/{issueLinkTypeId}"
category: "Issue link types"
writes_data: false
tool_note: "[[jira_get_issue_link_type]]"
---
# Jira v3 - Get issue link type

**Get issue link type** — `GET /rest/api/3/issueLinkType/{issueLinkTypeId}`

- Run by the tool [[jira_get_issue_link_type]].
- Official documentation: https://developer.atlassian.com/cloud/jira/platform/rest/v3/

```http
GET {{service.url}}/rest/api/3/issueLinkType/{{param:issueLinkTypeId}}
Authorization: {{service.auth_token}}
Accept: application/json
```

## Parameters

- `issueLinkTypeId` (path, string, required) — The ID of the issue link type.

## Original description

Returns an issue link type.

To use this operation, the site must have [issue linking](https://confluence.atlassian.com/x/yoXKM) enabled.

This operation can be accessed anonymously.

**[Permissions](#permissions) required:** *Browse projects* [project permission](https://confluence.atlassian.com/x/yodKLg) for a project in the site.
