---
tags:
  - api/request
  - api/service/atlassian
  - api/app/jira
  - api/resource/issues
  - api/operation/list
  - api/effect/read
up: "[[MCP - Jira v3]]"
app: "Jira v3"
method: GET
path: "/rest/api/3/issue/{issueIdOrKey}/transitions"
category: "Issues"
writes_data: false
tool_note: "[[jira_get_transitions]]"
---
# Jira v3 - Get transitions

**Get transitions** — `GET /rest/api/3/issue/{issueIdOrKey}/transitions`

- Run by the tool [[jira_get_transitions]].
- Official documentation: https://developer.atlassian.com/cloud/jira/platform/rest/v3/

```http
GET {{service.url}}/rest/api/3/issue/{{param:issueIdOrKey}}/transitions?expand={{param:expand}}&transitionId={{param:transitionId}}&skipRemoteOnlyCondition={{param:skipRemoteOnlyCondition}}&includeUnavailableTransitions={{param:includeUnavailableTransitions}}&sortByOpsBarAndStatus={{param:sortByOpsBarAndStatus}}
Authorization: {{service.auth_token}}
Accept: application/json
```

## Parameters

- `issueIdOrKey` (path, string, required) — The ID or key of the issue.
- `expand` (query, string, optional) — Use expand to include additional information about transitions in the response. This parameter accepts transitions.fields, which returns information about the fields in the transition screen for each…
- `transitionId` (query, string, optional) — The ID of the transition.
- `skipRemoteOnlyCondition` (query, string, optional) — Whether transitions with the condition Hide From User Condition are included in the response.
- `includeUnavailableTransitions` (query, string, optional) — Whether details of transitions that fail a condition are included in the response
- `sortByOpsBarAndStatus` (query, string, optional) — Whether the transitions are sorted by ops-bar sequence value first then category order (Todo, In Progress, Done) or only by ops-bar sequence value.

## Original description

Returns either all transitions or a transition that can be performed by the user on an issue, based on the issue's status.

Note, if a request is made for a transition that does not exist or cannot be performed on the issue, given its status, the response will return any empty transitions list.

This operation can be accessed anonymously.

**[Permissions](#permissions) required: A list or transition is returned only when the user has:**

 *  *Browse projects* [project permission](https://confluence.atlassian.com/x/yodKLg) for the project that the issue is in.
 *  If [issue-level security](https://confluence.atlassian.com/x/J4lKLg) is configured, issue-level security permission to view the issue.

However, if the user does not have the *Transition issues* [ project permission](https://confluence.atlassian.com/x/yodKLg) the response will not list any transitions.
