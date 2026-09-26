---
tags:
  - api/request
  - api/service/atlassian
  - api/app/jira
  - api/resource/workflow-transition-rules
  - api/operation/update
  - api/effect/write
  - api/restriction/app-connect
up: "[[MCP - Jira v3]]"
app: "Jira v3"
method: PUT
path: "/rest/api/3/workflow/rule/config/delete"
category: "Workflow transition rules"
writes_data: true
---
# Jira v3 - Delete workflow transition rule configurations

**Delete workflow transition rule configurations** — `PUT /rest/api/3/workflow/rule/config/delete`

- No dedicated tool: run it with `atlassian_request_write` passing `request:"Jira v3 - Delete workflow transition rule configurations"`.
- **Restriction:** the documentation says only Connect/Forge apps can call this endpoint; a user token is expected to be rejected.
- Official documentation: https://developer.atlassian.com/cloud/jira/platform/rest/v3/

```http
PUT {{service.url}}/rest/api/3/workflow/rule/config/delete
Authorization: {{service.auth_token}}
Accept: application/json
Content-Type: application/json

{{param:body}}
```

## Parameters

- `body` (body, object, required) — JSON request body. See the example in the request note.

## Body (example)

```json
{
  "workflows": [
    {
      "workflowId": {
        "draft": false,
        "name": "Internal support workflow"
      },
      "workflowRuleIds": [
        "b4d6cbdc-59f5-11e9-8647-d663bd873d93",
        "d663bd873d93-59f5-11e9-8647-b4d6cbdc",
        "11e9-59f5-b4d6cbdc-8647-d663bd873d93"
      ]
    }
  ]
}
```

## Original description

Deletes workflow transition rules from one or more workflows. These rule types are supported:

 *  [post functions](https://developer.atlassian.com/cloud/jira/platform/modules/workflow-post-function/)
 *  [conditions](https://developer.atlassian.com/cloud/jira/platform/modules/workflow-condition/)
 *  [validators](https://developer.atlassian.com/cloud/jira/platform/modules/workflow-validator/)

Only rules created by the calling Connect app can be deleted.

**Note:** The `draft` parameter in the request body WorkflowId is deprecated and will be removed from this API on [November 2, 2026](https://developer.atlassian.com/cloud/jira/platform/changelog/#CHANGE-3147).

**[Permissions](#permissions) required:** Only Connect apps can use this operation.
