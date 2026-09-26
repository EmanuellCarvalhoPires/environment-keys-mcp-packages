---
tags:
  - api/request
  - api/service/atlassian
  - api/app/jira
  - api/resource/issue-properties
  - api/operation/action
  - api/effect/write
up: "[[MCP - Jira v3]]"
app: "Jira v3"
method: POST
path: "/rest/api/3/issue/properties/multi"
category: "Issue properties"
writes_data: true
tool_note: "[[jira_bulk_set_issue_properties_by_issue]]"
---
# Jira v3 - Bulk set issue properties by issue

**Bulk set issue properties by issue** — `POST /rest/api/3/issue/properties/multi`

- Run by the tool [[jira_bulk_set_issue_properties_by_issue]].
- Official documentation: https://developer.atlassian.com/cloud/jira/platform/rest/v3/

```http
POST {{service.url}}/rest/api/3/issue/properties/multi
Authorization: {{service.auth_token}}
Content-Type: application/json

{{param:body}}
```

## Parameters

- `body` (body, object, required) — JSON request body. See the example in the request note.

## Body (example)

```json
{
  "issues": [
    {
      "issueID": 1000,
      "properties": {
        "myProperty": {
          "owner": "admin",
          "weight": 100
        }
      }
    },
    {
      "issueID": 1001,
      "properties": {
        "myOtherProperty": {
          "cost": 150,
          "transportation": "car"
        }
      }
    }
  ]
}
```

## Original description

Sets or updates entity property values on issues. Up to 10 entity properties can be specified for each issue and up to 100 issues included in the request.

The value of the request body must be a [valid](http://tools.ietf.org/html/rfc4627), non-empty JSON.

This operation is:

 *  [asynchronous](#async). Follow the `location` link in the response to determine the status of the task and use [Get task](#api-rest-api-3-task-taskId-get) to obtain subsequent updates.
 *  non-transactional. Updating some entities may fail. Such information will available in the task result.

**[Permissions](#permissions) required:**

 *  *Browse projects* and *Edit issues* [project permissions](https://confluence.atlassian.com/x/yodKLg) for the project containing the issue.
 *  If [issue-level security](https://confluence.atlassian.com/x/J4lKLg) is configured, issue-level security permission to view the issue.
