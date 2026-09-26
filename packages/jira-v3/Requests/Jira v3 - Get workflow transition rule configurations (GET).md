---
tags:
  - api/request
  - api/service/atlassian
  - api/app/jira
  - api/resource/workflow-transition-rules
  - api/operation/list
  - api/effect/read
up: "[[MCP - Jira v3]]"
app: "Jira v3"
method: GET
path: "/rest/api/3/workflow/rule/config"
category: "Workflow transition rules"
writes_data: false
tool_note: "[[jira_get_workflow_transition_rule_configurations]]"
---
# Jira v3 - Get workflow transition rule configurations (GET)

**Get workflow transition rule configurations** — `GET /rest/api/3/workflow/rule/config`

- Run by the tool [[jira_get_workflow_transition_rule_configurations]].
- Official documentation: https://developer.atlassian.com/cloud/jira/platform/rest/v3/

```http
GET {{service.url}}/rest/api/3/workflow/rule/config?startAt={{param:startAt}}&maxResults={{param:maxResults}}&types={{param:types}}&keys={{param:keys}}&workflowNames={{param:workflowNames}}&withTags={{param:withTags}}&draft={{param:draft}}&expand={{param:expand}}
Authorization: {{service.auth_token}}
Accept: application/json
```

## Parameters

- `startAt` (query, string, optional) — The index of the first item to return in a page of results (page offset).
- `maxResults` (query, string, optional) — The maximum number of items to return per page.
- `types` (query, string, required) — The types of the transition rules to return.
- `keys` (query, string, optional) — The transition rule class keys, as defined in the Connect or the Forge app descriptor, of the transition rules to return.
- `workflowNames` (query, string, optional) — The list of workflow names to filter by.
- `withTags` (query, string, optional) — The list of tags to filter by.
- `draft` (query, string, optional) — Deprecated: Whether draft or published workflows are returned. If not provided, both workflow types are returned. The 'draft' parameter will be removed from this API on November 2, 2026.
- `expand` (query, string, optional) — Use expand to include additional information in the response. This parameter accepts transition, which, for each rule, returns information about the transition the rule is assigned to.

## Original description

Returns a [paginated](#pagination) list of workflows with transition rules. The workflows can be filtered to return only those containing workflow transition rules:

 *  of one or more transition rule types, such as [workflow post functions](https://developer.atlassian.com/cloud/jira/platform/modules/workflow-post-function/).
 *  matching one or more transition rule keys.

Only workflows containing transition rules created by the calling [Connect](https://developer.atlassian.com/cloud/jira/platform/index/#connect-apps) or [Forge](https://developer.atlassian.com/cloud/jira/platform/index/#forge-apps) app are returned.

Due to server-side optimizations, workflows with an empty list of rules may be returned; these workflows can be ignored.

**[Permissions](#permissions) required:** Only [Connect](https://developer.atlassian.com/cloud/jira/platform/index/#connect-apps) or [Forge](https://developer.atlassian.com/cloud/jira/platform/index/#forge-apps) apps can use this operation.
