---
tags:
  - api/request
  - api/service/atlassian
  - api/app/jira
  - api/resource/workflow-transition-rules
  - api/operation/update
  - api/effect/write
up: "[[MCP - Jira v3]]"
app: "Jira v3"
method: PUT
path: "/rest/api/3/workflow/rule/config"
category: "Workflow transition rules"
writes_data: true
tool_note: "[[jira_update_workflow_transition_rule_configurations]]"
---
# Jira v3 - Update workflow transition rule configurations

**Update workflow transition rule configurations** — `PUT /rest/api/3/workflow/rule/config`

- Run by the tool [[jira_update_workflow_transition_rule_configurations]].
- Official documentation: https://developer.atlassian.com/cloud/jira/platform/rest/v3/

```http
PUT {{service.url}}/rest/api/3/workflow/rule/config
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
      "conditions": [
        {
          "configuration": {
            "disabled": false,
            "tag": "Another tag",
            "value": "{ \"size\": \"medium\" }"
          },
          "id": "d663bd873d93-59f5-11e9-8647-b4d6cbdc"
        }
      ],
      "postFunctions": [
        {
          "configuration": {
            "disabled": false,
            "tag": "Sample tag",
            "value": "{ \"color\": \"red\" }"
          },
          "id": "b4d6cbdc-59f5-11e9-8647-d663bd873d93"
        }
      ],
      "validators": [
        {
          "configuration": {
            "disabled": false,
            "value": "{ \"shape\": \"square\" }"
          },
          "id": "11e9-59f5-b4d6cbdc-8647-d663bd873d93"
        }
      ],
      "workflowId": {
        "draft": false,
        "name": "My Workflow name"
      }
    }
  ]
}
```

## Original description

Updates configuration of workflow transition rules. The following rule types are supported:

 *  [post functions](https://developer.atlassian.com/cloud/jira/platform/modules/workflow-post-function/)
 *  [conditions](https://developer.atlassian.com/cloud/jira/platform/modules/workflow-condition/)
 *  [validators](https://developer.atlassian.com/cloud/jira/platform/modules/workflow-validator/)

Only rules created by the calling [Connect](https://developer.atlassian.com/cloud/jira/platform/index/#connect-apps) or [Forge](https://developer.atlassian.com/cloud/jira/platform/index/#forge-apps) app can be updated.

To assist with app migration, this operation can be used to:

 *  Disable a rule.
 *  Add a `tag`. Use this to filter rules in the [Get workflow transition rule configurations](https://developer.atlassian.com/cloud/jira/platform/rest/v3/api-group-workflow-transition-rules/#api-rest-api-3-workflow-rule-config-get).

Rules are enabled if the `disabled` parameter is not provided.

**Note:** The `draft` parameter in the request body WorkflowId is deprecated and will be removed from this API on [November 2, 2026](https://developer.atlassian.com/cloud/jira/platform/changelog/#CHANGE-3147).

**[Permissions](#permissions) required:** Only [Connect](https://developer.atlassian.com/cloud/jira/platform/index/#connect-apps) or [Forge](https://developer.atlassian.com/cloud/jira/platform/index/#forge-apps) apps can use this operation.
