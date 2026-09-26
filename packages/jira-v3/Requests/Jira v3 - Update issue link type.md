---
tags:
  - api/request
  - api/service/atlassian
  - api/app/jira
  - api/resource/issue-link-types
  - api/operation/update
  - api/effect/write
  - api/permission/global-admin
up: "[[MCP - Jira v3]]"
app: "Jira v3"
method: PUT
path: "/rest/api/3/issueLinkType/{issueLinkTypeId}"
category: "Issue link types"
writes_data: true
tool_note: "[[jira_update_issue_link_type]]"
---
# Jira v3 - Update issue link type

**Update issue link type** — `PUT /rest/api/3/issueLinkType/{issueLinkTypeId}`

- Run by the tool [[jira_update_issue_link_type]].
- Official documentation: https://developer.atlassian.com/cloud/jira/platform/rest/v3/

```http
PUT {{service.url}}/rest/api/3/issueLinkType/{{param:issueLinkTypeId}}
Authorization: {{service.auth_token}}
Accept: application/json
Content-Type: application/json

{{param:body}}
```

## Parameters

- `issueLinkTypeId` (path, string, required) — The ID of the issue link type.
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

Updates an issue link type.

To use this operation, the site must have [issue linking](https://confluence.atlassian.com/x/yoXKM) enabled.

**[Permissions](#permissions) required:** *Administer Jira* [global permission](https://confluence.atlassian.com/x/x4dKLg).
