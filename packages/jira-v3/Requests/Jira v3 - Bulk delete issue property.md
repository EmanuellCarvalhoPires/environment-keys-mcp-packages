---
tags:
  - api/request
  - api/service/atlassian
  - api/app/jira
  - api/resource/issue-properties
  - api/operation/delete
  - api/effect/write
up: "[[MCP - Jira v3]]"
app: "Jira v3"
method: DELETE
path: "/rest/api/3/issue/properties/{propertyKey}"
category: "Issue properties"
writes_data: true
tool_note: "[[jira_bulk_delete_issue_property]]"
---
# Jira v3 - Bulk delete issue property

**Bulk delete issue property** — `DELETE /rest/api/3/issue/properties/{propertyKey}`

- Run by the tool [[jira_bulk_delete_issue_property]].
- Official documentation: https://developer.atlassian.com/cloud/jira/platform/rest/v3/

```http
DELETE {{service.url}}/rest/api/3/issue/properties/{{param:propertyKey}}
Authorization: {{service.auth_token}}
Content-Type: application/json

{{param:body}}
```

## Parameters

- `propertyKey` (path, string, required) — The key of the property.
- `body` (body, object, required) — JSON request body. See the example in the request note.

## Body (example)

```json
{
  "currentValue": "deprecated value",
  "entityIds": [
    10100,
    100010
  ]
}
```

## Original description

Deletes a property value from multiple issues. The issues to be updated can be specified by filter criteria.

The criteria the filter used to identify eligible issues are:

 *  `entityIds` Only issues from this list are eligible.
 *  `currentValue` Only issues with the property set to this value are eligible.

If both criteria is specified, they are joined with the logical *AND*: only issues that satisfy both criteria are considered eligible.

If no filter criteria are specified, all the issues visible to the user and where the user has the EDIT\_ISSUES permission for the issue are considered eligible.

This operation is:

 *  transactional, either the property is deleted from all eligible issues or, when errors occur, no properties are deleted.
 *  [asynchronous](#async). Follow the `location` link in the response to determine the status of the task and use [Get task](#api-rest-api-3-task-taskId-get) to obtain subsequent updates.

**[Permissions](#permissions) required:**

 *  *Browse projects* [ project permission](https://confluence.atlassian.com/x/yodKLg) for each project containing issues.
 *  If [issue-level security](https://confluence.atlassian.com/x/J4lKLg) is configured, issue-level security permission to view the issue.
 *  *Edit issues* [project permission](https://confluence.atlassian.com/x/yodKLg) for each issue.
