---
tags:
  - api/request
  - api/service/atlassian
  - api/app/jira
  - api/resource/issue-custom-field-contexts
  - api/operation/search
  - api/effect/read
  - api/permission/global-admin
up: "[[MCP - Jira v3]]"
app: "Jira v3"
method: POST
path: "/rest/api/3/field/{fieldId}/context/mapping"
category: "Issue custom field contexts"
writes_data: false
tool_note: "[[jira_get_custom_field_contexts_for_projects_and_issue_types]]"
---
# Jira v3 - Get custom field contexts for projects and issue types

**Get custom field contexts for projects and issue types** — `POST /rest/api/3/field/{fieldId}/context/mapping`

- Run by the tool [[jira_get_custom_field_contexts_for_projects_and_issue_types]].
- Official documentation: https://developer.atlassian.com/cloud/jira/platform/rest/v3/

```http
POST {{service.url}}/rest/api/3/field/{{param:fieldId}}/context/mapping?startAt={{param:startAt}}&maxResults={{param:maxResults}}
Authorization: {{service.auth_token}}
Accept: application/json
Content-Type: application/json

{{param:body}}
```

## Parameters

- `fieldId` (path, string, required) — The ID of the custom field.
- `startAt` (query, string, optional) — The index of the first item to return in a page of results (page offset).
- `maxResults` (query, string, optional) — The maximum number of items to return per page.
- `body` (body, object, required) — JSON request body. See the example in the request note.

## Body (example)

```json
{
  "mappings": [
    {
      "issueTypeId": "10000",
      "projectId": "10000"
    },
    {
      "issueTypeId": "10001",
      "projectId": "10000"
    },
    {
      "issueTypeId": "10002",
      "projectId": "10001"
    }
  ]
}
```

## Original description

Returns a [paginated](#pagination) list of project and issue type mappings and, for each mapping, the ID of a [custom field context](https://confluence.atlassian.com/x/k44fOw) that applies to the project and issue type.

If there is no custom field context assigned to the project then, if present, the custom field context that applies to all projects is returned if it also applies to the issue type or all issue types. If a custom field context is not found, the returned custom field context ID is `null`.

Duplicate project and issue type mappings cannot be provided in the request.

The order of the returned values is the same as provided in the request.

**[Permissions](#permissions) required:** *Administer Jira* [global permission](https://confluence.atlassian.com/x/x4dKLg).
