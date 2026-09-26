---
tags:
  - api/request
  - api/service/atlassian
  - api/app/jira
  - api/resource/plans
  - api/operation/update
  - api/effect/write
  - api/permission/global-admin
up: "[[MCP - Jira v3]]"
app: "Jira v3"
method: PUT
path: "/rest/api/3/plans/plan/{planId}"
category: "Plans"
writes_data: true
tool_note: "[[jira_update_plan]]"
---
# Jira v3 - Update plan

**Update plan** — `PUT /rest/api/3/plans/plan/{planId}`

- Run by the tool [[jira_update_plan]].
- Official documentation: https://developer.atlassian.com/cloud/jira/platform/rest/v3/

```http
PUT {{service.url}}/rest/api/3/plans/plan/{{param:planId}}?useGroupId={{param:useGroupId}}
Authorization: {{service.auth_token}}
Content-Type: application/json-patch+json

{{param:body}}
```

## Parameters

- `planId` (path, string, required) — The ID of the plan.
- `useGroupId` (query, string, optional) — Whether to accept group IDs instead of group names. Group names are deprecated.
- `body` (body, array, required) — JSON request body. See the example in the request note.

## Body (example)

```json
[{"op": "replace", "path": "/scheduling/estimation", "value": "Days"}]
```

## Original description

Updates any of the following details of a plan using [JSON Patch](https://datatracker.ietf.org/doc/html/rfc6902).

 *  name
 *  leadAccountId
 *  scheduling
    
     *  estimation with StoryPoints, Days or Hours as possible values
     *  startDate
        
         *  type with DueDate, TargetStartDate, TargetEndDate or DateCustomField as possible values
         *  dateCustomFieldId
     *  endDate
        
         *  type with DueDate, TargetStartDate, TargetEndDate or DateCustomField as possible values
         *  dateCustomFieldId
     *  inferredDates with None, SprintDates or ReleaseDates as possible values
     *  dependencies with Sequential or Concurrent as possible values
 *  issueSources
    
     *  type with Board, Project or Filter as possible values
     *  value
 *  exclusionRules
    
     *  numberOfDaysToShowCompletedIssues
     *  issueIds
     *  workStatusIds
     *  workStatusCategoryIds
     *  issueTypeIds
     *  releaseIds
 *  crossProjectReleases
    
     *  name
     *  releaseIds
 *  customFields
    
     *  customFieldId
     *  filter
 *  permissions
    
     *  type with View or Edit as possible values
     *  holder
        
         *  type with Group or AccountId as possible values
         *  value

**[Permissions](#permissions) required:** *Administer Jira* [global permission](https://confluence.atlassian.com/x/x4dKLg).

*Note that "add" operations do not respect array indexes in target locations. Call the "Get plan" endpoint to find out the order of array elements.*
