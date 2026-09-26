---
tags:
  - api/request
  - api/service/atlassian
  - api/app/jira
  - api/resource/ui-modifications-apps
  - api/operation/update
  - api/effect/write
  - api/restriction/app-connect
up: "[[MCP - Jira v3]]"
app: "Jira v3"
method: PUT
path: "/rest/api/3/uiModifications/{uiModificationId}"
category: "UI modifications (apps)"
writes_data: true
---
# Jira v3 - Update UI modification

**Update UI modification** — `PUT /rest/api/3/uiModifications/{uiModificationId}`

- No dedicated tool: run it with `atlassian_request_write` passing `request:"Jira v3 - Update UI modification"`.
- **Restriction:** the documentation says only Connect/Forge apps can call this endpoint; a user token is expected to be rejected.
- Official documentation: https://developer.atlassian.com/cloud/jira/platform/rest/v3/

```http
PUT {{service.url}}/rest/api/3/uiModifications/{{param:uiModificationId}}
Authorization: {{service.auth_token}}
Content-Type: application/json

{{param:body}}
```

## Parameters

- `uiModificationId` (path, string, required) — The ID of the UI modification.
- `body` (body, object, required) — JSON request body. See the example in the request note.

## Body (example)

```json
{
  "contexts": [
    {
      "issueTypeId": "10000",
      "projectId": "10000",
      "viewType": "GIC"
    },
    {
      "issueTypeId": "10001",
      "projectId": "10000",
      "viewType": "IssueView"
    },
    {
      "issueTypeId": "10002",
      "projectId": "10000",
      "viewType": "IssueTransition"
    },
    {
      "issueTypeId": null,
      "portalId": "5",
      "projectId": null,
      "requestTypeId": "100",
      "viewType": "JSMRequestCreate"
    },
    {
      "issueTypeId": "10004",
      "projectId": "10000",
      "viewType": "IssueViewAgentView"
    },
    {
      "issueTypeId": "10004",
      "projectId": "10000",
      "requestTypeId": "20",
      "viewType": "GICAgentView"
    }
  ],
  "data": "{field: 'Story Points', config: {hidden: true}}",
  "name": "Updated Reveal Story Points"
}
```

## Original description

Updates a UI modification. UI modification can only be updated by Forge apps.

Each UI modification can define up to 1000 contexts. The same context can be assigned to maximum 100 UI modifications.

**Context types:**

 *  **Jira contexts:** For Jira view types, use `projectId` and `issueTypeId`. One field can act as a wildcard. Supported Jira views:
    
     *  `GIC` \- Jira global issue create
     *  `IssueView` \- Jira issue view
     *  `IssueTransition` \- Jira issue transition
 *  **Jira Service Management contexts:** For Jira Service Management view types, use `portalId` and `requestTypeId`. Wildcards are not supported. Supported JSM views:
    
     *  `JSMRequestCreate` \- Jira Service Management request create portal view
 *  **Agent view contexts:** For Agent view types, use `projectId` and `issueTypeId` like Jira contexts, and optionally set `requestTypeId`. `portalId` must not be set. One of `projectId`, `issueTypeId`, or `viewType` can act as a wildcard. Supported Agent views:
    
     *  `GICAgentView` \- Agent view variant of Jira global issue create
     *  `IssueViewAgentView` \- Agent view variant of Jira issue view
     *  `IssueTransitionAgentView` \- Agent view variant of Jira issue transition

**[Permissions](#permissions) required:**

 *  *None* if the UI modification is created without contexts.
 *  *Browse projects* [project permission](https://confluence.atlassian.com/x/yodKLg) for one or more projects, if the UI modification is created with contexts.

The new `write:app-data:jira` OAuth scope is 100% optional now, and not using it won't break your app. However, we recommend adding it to your app's scope list because we will eventually make it mandatory.
