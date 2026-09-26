---
tags:
  - api/request
  - api/service/atlassian
  - api/app/jira
  - api/resource/issue-link-types
  - api/operation/list
  - api/effect/read
up: "[[MCP - Jira v3]]"
app: "Jira v3"
method: GET
path: "/rest/api/3/issueLinkType"
category: "Issue link types"
writes_data: false
tool_note: "[[jira_get_issue_link_types]]"
---
# Jira v3 - Get issue link types

**Get issue link types** — `GET /rest/api/3/issueLinkType`

- Run by the tool [[jira_get_issue_link_types]].
- Official documentation: https://developer.atlassian.com/cloud/jira/platform/rest/v3/

```http
GET {{service.url}}/rest/api/3/issueLinkType
Authorization: {{service.auth_token}}
Accept: application/json
```

## Original description

Returns a list of all issue link types.

To use this operation, the site must have [issue linking](https://confluence.atlassian.com/x/yoXKM) enabled.

This operation can be accessed anonymously.

**[Permissions](#permissions) required:** *Browse projects* [project permission](https://confluence.atlassian.com/x/yodKLg) for a project in the site.
