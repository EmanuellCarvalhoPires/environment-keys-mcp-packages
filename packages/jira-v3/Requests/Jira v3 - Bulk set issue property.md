---
tags:
  - api/request
  - api/service/atlassian
  - api/app/jira
  - api/resource/issue-properties
  - api/operation/update
  - api/effect/write
up: "[[MCP - Jira v3]]"
app: "Jira v3"
method: PUT
path: "/rest/api/3/issue/properties/{propertyKey}"
category: "Issue properties"
writes_data: true
tool_note: "[[jira_bulk_set_issue_property]]"
---
# Jira v3 - Bulk set issue property

**Bulk set issue property** — `PUT /rest/api/3/issue/properties/{propertyKey}`

- Run by the tool [[jira_bulk_set_issue_property]].
- Official documentation: https://developer.atlassian.com/cloud/jira/platform/rest/v3/

```http
PUT {{service.url}}/rest/api/3/issue/properties/{{param:propertyKey}}
Authorization: {{service.auth_token}}
Content-Type: application/json

{{param:body}}
```

## Parameters

- `propertyKey` (path, string, required) — The key of the property. The maximum length is 255 characters.
- `body` (body, object, required) — JSON request body. See the example in the request note.

## Body (example)

```json
{
  "filter": {
    "currentValue": {
      "owner": "admin",
      "weight": 50
    },
    "entityIds": [
      10100,
      100010
    ],
    "hasProperty": true
  },
  "value": {
    "owner": "admin",
    "weight": 100
  }
}
```

## Original description

Sets a property value on multiple issues.

The value set can be a constant or determined by a [Jira expression](https://developer.atlassian.com/cloud/jira/platform/jira-expressions/). Expressions must be computable with constant complexity when applied to a set of issues. Expressions must also comply with the [restrictions](https://developer.atlassian.com/cloud/jira/platform/jira-expressions/#restrictions) that apply to all Jira expressions.

The issues to be updated can be specified by a filter.

The filter identifies issues eligible for update using these criteria:

 *  `entityIds` Only issues from this list are eligible.
 *  `currentValue` Only issues with the property set to this value are eligible.
 *  `hasProperty`:
    
     *  If *true*, only issues with the property are eligible.
     *  If *false*, only issues without the property are eligible.

If more than one criteria is specified, they are joined with the logical *AND*: only issues that satisfy all criteria are eligible.

If an invalid combination of criteria is provided, an error is returned. For example, specifying a `currentValue` and `hasProperty` as *false* would not match any issues (because without the property the property cannot have a value).

The filter is optional. Without the filter all the issues visible to the user and where the user has the EDIT\_ISSUES permission for the issue are considered eligible.

This operation is:

 *  transactional, either all eligible issues are updated or, when errors occur, none are updated.
 *  [asynchronous](#async). Follow the `location` link in the response to determine the status of the task and use [Get task](#api-rest-api-3-task-taskId-get) to obtain subsequent updates.

**[Permissions](#permissions) required:**

 *  *Browse projects* [project permission](https://confluence.atlassian.com/x/yodKLg) for each project containing issues.
 *  If [issue-level security](https://confluence.atlassian.com/x/J4lKLg) is configured, issue-level security permission to view the issue.
 *  *Edit issues* [project permission](https://confluence.atlassian.com/x/yodKLg) for each issue.
