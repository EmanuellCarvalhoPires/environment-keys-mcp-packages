---
tags:
  - api/request
  - api/service/atlassian
  - api/app/jira
  - api/resource/issue-link-types
  - api/operation/create
  - api/effect/write
  - api/permission/global-admin
up: "[[MCP - Jira v3]]"
app: "Jira v3"
method: POST
path: "/rest/api/3/issueLinkType"
category: "Issue link types"
writes_data: true
tool_note: "[[jira_create_issue_link_type]]"
---
# Jira v3 - Create issue link type

**Create issue link type** — `POST /rest/api/3/issueLinkType`

- Run by the tool [[jira_create_issue_link_type]].
- Official documentation: https://developer.atlassian.com/cloud/jira/platform/rest/v3/

```http
POST {{service.url}}/rest/api/3/issueLinkType
Authorization: {{service.auth_token}}
Content-Type: application/json

{{param:body}}
```

## Parameters

- `body` (body, object, required) — JSON request body. See the example in the request note.

## Body (example)

```json
{
  "inward": "Duplicated by",
  "name": "Duplicate",
  "outward": "Duplicates"
}
```

## Original description

Creates an issue link type. Use this operation to create descriptions of the reasons why issues are linked. The issue link type consists of a name and descriptions for a link's inward and outward relationships.

To use this operation, the site must have [issue linking](https://confluence.atlassian.com/x/yoXKM) enabled.

**[Permissions](#permissions) required:** *Administer Jira* [global permission](https://confluence.atlassian.com/x/x4dKLg).
