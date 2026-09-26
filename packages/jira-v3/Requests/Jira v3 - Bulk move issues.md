---
tags:
  - api/request
  - api/service/atlassian
  - api/app/jira
  - api/resource/issue-bulk-operations
  - api/operation/action
  - api/effect/write
up: "[[MCP - Jira v3]]"
app: "Jira v3"
method: POST
path: "/rest/api/3/bulk/issues/move"
category: "Issue bulk operations"
writes_data: true
tool_note: "[[jira_bulk_move_issues]]"
---
# Jira v3 - Bulk move issues

**Bulk move issues** — `POST /rest/api/3/bulk/issues/move`

- Run by the tool [[jira_bulk_move_issues]].
- Official documentation: https://developer.atlassian.com/cloud/jira/platform/rest/v3/

```http
POST {{service.url}}/rest/api/3/bulk/issues/move
Authorization: {{service.auth_token}}
Content-Type: application/json

{{param:body}}
```

## Parameters

- `body` (body, object, required) — JSON request body. See the example in the request note.

## Body (example)

```json
{
  "sendBulkNotification": true,
  "targetToSourcesMapping": {
    "PROJECT-KEY,10001": {
      "inferClassificationDefaults": false,
      "inferFieldDefaults": false,
      "inferStatusDefaults": false,
      "inferSubtaskTypeDefault": true,
      "issueIdsOrKeys": [
        "ISSUE-1"
      ],
      "targetClassification": [
        {
          "classifications": {
            "5bfa70f7-4af1-44f5-9e12-1ce185f15a38": [
              "bd58e74c-c31b-41a7-ba69-9673ebd9dae9",
              "-1"
            ]
          }
        }
      ],
      "targetMandatoryFields": [
        {
          "fields": {
            "customfield_10000": {
              "retain": false,
              "type": "raw",
              "value": [
                "value-1",
                "value-2"
              ]
            },
            "description": {
              "retain": true,
              "type": "adf",
              "value": {
                "content": [
                  {
                    "content": [
                      {
                        "text": "New description value",
                        "type": "text"
                      }
                    ],
                    "type": "paragraph"
                  }
                ],
                "type": "doc",
                "version": 1
              }
            },
            "fixVersions": {
              "retain": false,
              "type": "raw",
              "value": [
                "10009"
              ]
            },
            "labels": {
              "retain": false,
              "type": "raw",
              "value": [
                "label-1",
                "label-2"
              ]
            }
          }
        }
      ],
      "targetStatus": [
        {
          "statuses": {
            "10001": [
              "10002",
              "10003"
            ]
          }
        }
      ]
    }
  }
}
```

## Original description

Use this API to submit a bulk issue move request. You can move multiple issues from multiple projects in a single request, but they must all be moved to a single project, issue type, and parent. You can't move more than 1000 issues (including subtasks) at once.

#### Scenarios: ####

This is an early version of the API and it doesn't have full feature parity with the Bulk Move UI experience.

 *  Moving issue of type A to issue of type B in the same project or a different project: `SUPPORTED`
 *  Moving multiple issues of type A in one or more projects to multiple issues of type B in one of the source projects or a different project: `SUPPORTED`
 *  Moving issues of multiple issue types in one or more projects to issues of a single issue type in one of the source project or a different project: **`SUPPORTED`**  
    E.g. Moving issues of story and task issue types in project 1 and project 2 to issues of task issue type in project 3
 *  Moving a standard parent issue of type A with its multiple subtask issue types in one project to standard issue of type B and multiple subtask issue types in the same project or a different project: `SUPPORTED`
 *  Moving standard issues with their subtasks to a parent issue in the same project or a different project without losing their relation: `SUPPORTED`
 *  Moving an epic issue with its child issues to a different project without losing their relation: `SUPPORTED`  
    This usecase is **supported using multiple requests**. Move the epic in one request and then move the children in a separate request with target parent set to the epic issue id  
      
    (Alternatively, move them individually and stitch the relationship back with the Bulk Edit API)

#### Limits applied to bulk issue moves: ####

When using the bulk move, keep in mind that there are limits on the number of issues and fields you can include.

 *  You can move up to 1,000 issues in a single operation, including any subtasks.
 *  The total combined number of fields across all issues must not exceed 1,500,000. For example, if each issue includes 15,000 fields, then the maximum number of issues that can be moved is 100.

**[Permissions](#permissions) required:**

 *  Global bulk change [permission](https://support.atlassian.com/jira-cloud-administration/docs/manage-global-permissions/).
 *  Move [issues permission](https://support.atlassian.com/jira-cloud-administration/docs/manage-project-permissions/) in source projects.
 *  Create [issues permission](https://support.atlassian.com/jira-cloud-administration/docs/manage-project-permissions/) in destination projects.
 *  Browse [project permission](https://support.atlassian.com/jira-cloud-administration/docs/manage-project-permissions/) in destination projects, if moving subtasks only.
 *  If [issue-level security](https://confluence.atlassian.com/x/J4lKLg) is configured, issue-level security permission to view the issue.
